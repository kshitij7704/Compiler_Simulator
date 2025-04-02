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