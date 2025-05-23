# 🛠️ Compiler Simulator
A simple compiler simulator that demonstrates the phases of compilation—from lexical analysis to target code generation for arithmetic expressions. This project includes both a desktop GUI (built with Tkinter) and a web application (built with Flask) to showcase the compilation process.

---

## 🚀 Features
- **Lexical Analysis**: Tokenizes source code into meaningful units.
- **Syntax Analysis**: Parses tokens to construct an Abstract Syntax Tree (AST).
- **Semantic Analysi**s: Performs type checking and constant folding.
- **Intermediate Code Generation**: Converts the AST into three-address code.
- **Target Code Generation**: Generates pseudo-assembly code from the intermediate representation.
- **Desktop GUI**: A polished, modern interface using Tkinter and ttk, complete with a clear button, status bar, and file operations.
- **Web Application**: A responsive web interface built with Flask and Bootstrap for online code compilation and output display.

---

## 📁 Project Structure
```
Compiler_Simulator/
├── GUI/
│   ├── app.py
│   └── Compiler/
│       ├── lexical_analysis.py
│       ├── syntax_analysis.py
│       ├── semantic_analysis.py
│       ├── intermediate_code_generation.py
│       ├── code_generation.py
│       └── compile_source.py
└── Web App/
    ├── app.py
    ├── requirements.txt  
    └── templates/
        └── index.html            
```
---

## 🧰 Prerequisites
1. Python 3.x
2. The following Python packages:
    - Flask
    - Tkinter (usually included with standard Python installations)
3. You can install the required Python packages using pip:
```
pip install -r requirements.txt
```

---

## 🔧 Installation
1. Clone the Repository:
```
git clone https://github.com/kshitij7704/Compiler_Simulator.git
cd compiler_simulator
```
2. Set Up the Environment:
Create and activate a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate # For Mac
venv\Scripts\activate # For Windows
pip install -r requirements.txt
```

---

## 🖥️ Usage
### 💻 Desktop GUI Version
1. The GUI version uses Tkinter to provide a standalone desktop application.
2. Run the GUI Application:
```
cd GUI
python app.py
```
#### Features:
1. Enter source code into the provided text area.
2. Click the Compile button to process the code.
3. The output is displayed step by step (lexical analysis, AST, intermediate code, etc.) in a styled output area.
4. Use the Clear button to reset the input and output fields.

### 🌐 Web Application Version
1. The web app version uses Flask and Bootstrap for a responsive online interface.
2. Run the Flask Application:
```
cd Web App
python app.py
```
3. Access the Web App:
    - Open your browser and navigate to http://127.0.0.1:5000.
      
####  🔄 Workflow:
1. Input source code via a responsive textarea.
2. Click Compile to process the code.
3. The compilation output is displayed with detailed phase-by-phase results in an attractive output card.
4. Use the Clear button to reset the code input and output display.
5. Additional file operations (open/save) and a menu bar are available.

---

## 🧠 Supported Language Features
The simulator currently supports:
- Arithmetic expressions
- Basic identifiers and constants
- Operators: +, -, *, /, and parentheses for grouping

---

## 🤝 Contributing
Contributions, bug fixes, and feature suggestions are welcome. Feel free to open an issue or submit a pull request.
