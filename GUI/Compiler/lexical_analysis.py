import re

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