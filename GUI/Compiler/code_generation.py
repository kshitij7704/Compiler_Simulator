import re

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