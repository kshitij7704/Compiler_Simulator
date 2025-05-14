# 🌐 Compiler Simulator – Web Application
This is the web-based interface for the Compiler Simulator project, designed to simulate the phases of a compiler—from lexical analysis to target code generation—within a modern, responsive web application built with Flask and Bootstrap.

## 🚀 Features
- **Lexical Analysis**: Tokenizes user input into recognizable symbols.
- **Syntax Analysis**: Builds an Abstract Syntax Tree (AST) from the tokens.
- **Semantic Analysis**: Checks types and performs constant folding.
- **Intermediate Code Generation**: Outputs simplified three-address code.
- **Target Code Generation**: Produces pseudo-assembly instructions.
- **Responsive UI**: Clean Bootstrap-based layout for smooth user experience.
- **Phase-by-Phase Output**: Clear, structured display of each compilation phase.
- **File I/O Support (optional)**: Ability to load/save code (can be integrated from the GUI version if needed).

## 📁 Project Structure
```
Web App/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
└── templates/
    └── index.html          # HTML template with Bootstrap UI
```

## 🧰 Prerequisites
1. Python 3.x
2. Flask
3. Install the required dependencies using:
  ```
  pip install -r requirements.txt
  ```

## ⚙️ Setup & Run
1. Navigate to the Web App directory:
    ```
    cd "Compiler_Simulator/Web App"
    ```
2. Run the Flask application:
    ```
    python app.py
    ```
3. Open your browser and go to:
    ```
    http://127.0.0.1:5000
    ```

## ✨ Usage
1. **Enter Source Code**: Type arithmetic expressions directly into the text area.
2. **Click "Compile"**: The input will be processed through all compiler phases.
3. **View Output**: Each stage (tokens, AST, intermediate code, assembly) is displayed clearly.
4. **Clear Button**: Resets the input/output fields for a fresh start.

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
2. Intermediate Code:
    ```
    t1 = 2 - 1
    t2 = 5 * t1
    t3 = 3 + t2
    a = t3
    ```
3. Target Code (pseudo-assembly):
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

## 📌 Notes
This version focuses on arithmetic expression parsing.
For a complete experience including a desktop GUI version, refer to the main repository.

## 🤝 Contributing
Got ideas or found a bug? Open an issue or submit a pull request!
