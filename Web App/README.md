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
Navigate to the Web App directory:

bash
Copy
Edit
cd "Compiler_Simulator/Web App"
Run the Flask application:

bash
Copy
Edit
python app.py
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000
