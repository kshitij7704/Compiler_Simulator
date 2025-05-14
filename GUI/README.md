# 🖥️ Compiler Simulator – Desktop GUI Application
This is the desktop GUI version of the Compiler Simulator, offering a rich, interactive interface for visualizing the entire compilation process of simple arithmetic expressions. Built with Tkinter and ttk, it provides an intuitive, standalone application to explore compiler design concepts in action.

## 🔍 Features
- **Lexical Analysis**: Breaks down source code into tokens.
- **Syntax Analysis**: Constructs an Abstract Syntax Tree (AST).
- **Semantic Analysis**: Performs type checking and constant folding.
- **Intermediate Code Generation**: Outputs simplified three-address code.
- **Target Code Generation**: Converts intermediate code to pseudo-assembly.
- Interactive GUI

## 📁 Project Structure
```
GUI/
├── app.py                        # Main GUI entry point
└── Compiler/
    ├── lexical_analysis.py       # Lexical analyzer
    ├── syntax_analysis.py        # Parser and AST generator
    ├── semantic_analysis.py      # Type checking and folding
    ├── intermediate_code_generation.py
    ├── code_generation.py        # Assembly code generator
    └── compile_source.py         # Compiler pipeline coordinator
```

## 🧰 Prerequisites
1. Python 3.x
2. Tkinter (usually bundled with Python)
3. Install dependencies using:
   ```
   pip install -r requirements.txt
   ```
⚠️ Note: requirements.txt may not list Tkinter as it comes pre-installed with most Python distributions.

## ⚙️ Setup & Run
1. Navigate to the GUI directory:
   ```
   cd "Compiler_Simulator/GUI"
   ```
2. Run the application:
   ```
   python app.py
   ```


## 🖋️ Usage Instructions
1. **Enter Source Code**: Input arithmetic expressions into the main text area.
2. **Click "Compile"**: Initiates the compilation pipeline.
3. **View Output**: Results from each compiler phase (token list, AST, intermediate code, and target code) are displayed in a structured, scrollable output section.
4. **Clear**: Resets all inputs and outputs.


## 🧠 Example 
### Input
```
a = 3 + 5 * (2 - 1)
```
### Sample Output: 
1. Tokens:
   ```
    ['a', '=', '3', '+', '5', '*', '(', '2', '-', '1', ')']
   ```
3. Intermediate Code:
    ```
    t1 = 2 - 1
    t2 = 5 * t1
    t3 = 3 + t2
    a = t3
    ```
4. Target Code (pseudo-assembly):
    ```
    LOAD 2
    SUB 1
    STORE t1
    LOAD 5
    MUL t1
    STORE t2
    LOAD 3
    ADD t2
    STORE a
    ```

## 🎯 Ideal For
1. Students and educators learning compiler design.
2. Demonstrating compiler phases in classrooms.
3. Building on to support advanced language features.

## 🤝 Contributing
Pull requests, bug reports, and suggestions are welcome. Contributions help improve the project for everyone!
