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
        """Parse multiple statements until EOF."""
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
        # statement -> ID ASSIGN expression
        token = self.eat('ID')
        var_name = token[1]
        self.eat('ASSIGN')
        expr_node = self.expression()
        return {'type': 'assignment', 'target': var_name, 'expression': expr_node}

    def expression(self):
        # expression -> term ((PLUS|MINUS) term)*
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
        # term -> factor ((MUL|DIV) factor)*
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
        # factor -> NUMBER | ID | LPAREN expression RPAREN
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