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