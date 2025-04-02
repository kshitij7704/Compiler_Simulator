from .lexical_analysis import lexical_analysis
from .syntax_analysis import syntax_analysis
from .semantic_analysis import semantic_analysis
from .intermediate_code_generation import intermediate_code_generation
from .code_generation import code_generation

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