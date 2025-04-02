import re
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "test-key"

# ------------------------
# Lexical Analysis
# ------------------------
def lexical_analysis(source_code):
    token_specification = [
        ('NUMBER',   r'\d+(\.\d+)?'),
        ('ID',       r'[A-Za-z_]\w*'),
        ('ASSIGN',   r'='),
        ('PLUS',     r'\+'),
        ('MINUS',    r'-'),
        ('MUL',      r'\*'),
        ('DIV',      r'/'),
        ('LPAREN',   r'\('),
        ('RPAREN',   r'\)'),
        ('SEMI',     r';'),
        ('SKIP',     r'[ \t]+'),
        ('NEWLINE',  r'\n'),
        ('MISMATCH', r'.'),
    ]
    tokens = []
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, source_code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start + 1
        if kind == 'NUMBER':
            tokens.append(('NUMBER', value, line_num, column))
        elif kind == 'ID':
            tokens.append(('ID', value, line_num, column))
        elif kind in ('ASSIGN', 'PLUS', 'MINUS', 'MUL', 'DIV', 'LPAREN', 'RPAREN', 'SEMI'):
            tokens.append((kind, value, line_num, column))
        elif kind == 'NEWLINE':
            line_num += 1
            line_start = mo.end()
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Lexical Error: Unexpected character {value!r} at line {line_num} column {column}')
    tokens.append(('EOF', None, line_num, column))
    return tokens

# ------------------------
# Parser (Syntax Analysis)
# ------------------------
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def current_token(self):
        if self.index < len(self.tokens):
            return self.tokens[self.index]
        return ('EOF', None, -1, -1)

    def error(self, expected):
        token = self.current_token()
        token_type, token_value, line, column = token
        raise SyntaxError(f"Syntax Error: Expected {expected} at line {line} column {column}, got '{token_value}' ({token_type}).")

    def eat(self, token_type):
        token = self.current_token()
        if token[0] == token_type:
            self.index += 1
            return token
        else:
            self.error(token_type)

    def parse_program(self):
        statements = []
        while self.current_token()[0] != 'EOF':
            while self.current_token()[0] == 'SEMI':
                self.eat('SEMI')
            if self.current_token()[0] == 'EOF':
                break
            stmt = self.statement()
            statements.append(stmt)
            if self.current_token()[0] == 'SEMI':
                self.eat('SEMI')
            else:
                token = self.current_token()
                raise SyntaxError(f"Syntax Error: Missing semicolon at line {token[2]} column {token[3]}.")
        return statements

    def statement(self):
        token = self.eat('ID')
        var_name = token[1]
        self.eat('ASSIGN')
        expr_node = self.expression()
        return {'type': 'assignment', 'target': var_name, 'expression': expr_node}

    def expression(self):
        node = self.term()
        while self.current_token()[0] in ('PLUS', 'MINUS'):
            token = self.current_token()
            if token[0] == 'PLUS':
                self.eat('PLUS')
                node = {'type': 'binary_op', 'operator': '+', 'left': node, 'right': self.term()}
            elif token[0] == 'MINUS':
                self.eat('MINUS')
                node = {'type': 'binary_op', 'operator': '-', 'left': node, 'right': self.term()}
        return node

    def term(self):
        node = self.factor()
        while self.current_token()[0] in ('MUL', 'DIV'):
            token = self.current_token()
            if token[0] == 'MUL':
                self.eat('MUL')
                node = {'type': 'binary_op', 'operator': '*', 'left': node, 'right': self.factor()}
            elif token[0] == 'DIV':
                self.eat('DIV')
                node = {'type': 'binary_op', 'operator': '/', 'left': node, 'right': self.factor()}
        return node

    def factor(self):
        token = self.current_token()
        if token[0] == 'NUMBER':
            self.eat('NUMBER')
            return {'type': 'number', 'value': float(token[1]) if '.' in token[1] else int(token[1])}
        elif token[0] == 'ID':
            self.eat('ID')
            return {'type': 'identifier', 'name': token[1]}
        elif token[0] == 'LPAREN':
            self.eat('LPAREN')
            node = self.expression()
            self.eat('RPAREN')
            return node
        else:
            self.error("NUMBER, identifier, or '('")

def syntax_analysis(tokens):
    parser = Parser(tokens)
    return parser.parse_program()

# ------------------------
# Semantic Analysis
# ------------------------
def semantic_analysis(ast_list):
    def fold(node):
        if node['type'] == 'binary_op':
            left = fold(node['left'])
            right = fold(node['right'])
            if left['type'] == 'number' and right['type'] == 'number':
                op = node['operator']
                if op == '+':
                    value = left['value'] + right['value']
                elif op == '-':
                    value = left['value'] - right['value']
                elif op == '*':
                    value = left['value'] * right['value']
                elif op == '/':
                    if right['value'] == 0:
                        raise RuntimeError("Semantic Error: Division by zero.")
                    value = left['value'] / right['value']
                return {'type': 'number', 'value': value}
            else:
                return {'type': 'binary_op', 'operator': node['operator'], 'left': left, 'right': right}
        else:
            return node

    for ast in ast_list:
        ast['expression'] = fold(ast['expression'])
    return ast_list

# ------------------------
# Intermediate Code Generation
# ------------------------
def intermediate_code_generation(ast_list):
    code_lines = []
    temp_counter = 1

    def generate(node):
        nonlocal temp_counter
        if node['type'] == 'number':
            return str(node['value'])
        elif node['type'] == 'identifier':
            return node['name']
        elif node['type'] == 'binary_op':
            left = generate(node['left'])
            right = generate(node['right'])
            temp = f"t{temp_counter}"
            temp_counter += 1
            code_lines.append(f"{temp} = {left} {node['operator']} {right}")
            return temp
        else:
            raise RuntimeError("Unknown node type in code generation.")

    for ast in ast_list:
        result = generate(ast['expression'])
        code_lines.append(f"{ast['target']} = {result}")
    return "\n".join(code_lines)

# ------------------------
# Code Generation (Target Code)
# ------------------------
def code_generation(intermediate_code):
    assembly_lines = []
    lines = intermediate_code.splitlines()
    for line in lines:
        if '=' in line:
            lhs, rhs = line.split('=')
            lhs = lhs.strip()
            rhs = rhs.strip()
            if re.fullmatch(r'\d+(\.\d+)?', rhs):
                assembly_lines.append(f"LOAD_CONST R1, {rhs}")
                assembly_lines.append(f"STORE R1, {lhs}")
            else:
                assembly_lines.append(f"// Computed: {rhs} stored in {lhs}")
    return "\n".join(assembly_lines)

# ------------------------
# Compiler Simulator (Combined)
# ------------------------
def compile_source(source_code):
    output_lines = []
    output_lines.append("Source Code:")
    output_lines.append(source_code)
    try:
        tokens = lexical_analysis(source_code)
        output_lines.append("\n[Lexical Analysis Output]")
        for token in tokens:
            output_lines.append(str(token))
        ast_list = syntax_analysis(tokens)
        output_lines.append("\n[Syntax Analysis Output (ASTs)]")
        for ast in ast_list:
            output_lines.append(str(ast))
        ast_list = semantic_analysis(ast_list)
        output_lines.append("\n[Semantic Analysis Output (ASTs with Semantic Info)]")
        for ast in ast_list:
            output_lines.append(str(ast))
        interm_code = intermediate_code_generation(ast_list)
        output_lines.append("\n[Intermediate Code]")
        output_lines.append(interm_code)
        target_code = code_generation(interm_code)
        output_lines.append("\n[Target Code Generation]")
        output_lines.append(target_code)
    except (SyntaxError, RuntimeError) as e:
        output_lines.append("\nError:")
        output_lines.append(str(e))
    return "\n".join(output_lines)

# ------------------------
# Flask Routes
# ------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        source_code = request.form.get("source_code", "")
        if not source_code.strip():
            flash("Please enter some source code.", "warning")
            return redirect(url_for("index"))
        result = compile_source(source_code)
        return render_template("index.html", source_code=source_code, output=result)
    return render_template("index.html", source_code="", output="")

if __name__ == "__main__":
    app.run(debug=True)
