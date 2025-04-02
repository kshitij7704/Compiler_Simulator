from Compiler.compile_source import compile_source
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog

# ------------------------
# GUI Setup with Enhanced Styling
# ------------------------
def compile_code():
    source = code_input.get("1.0", tk.END).strip()
    if not source:
        messagebox.showwarning("Input Required", "Please enter some source code.")
        return
    result = compile_source(source)
    output_area.config(state=tk.NORMAL)
    output_area.delete("1.0", tk.END)
    output_area.insert(tk.END, result)
    output_area.config(state=tk.DISABLED)
    status_var.set("Compilation finished successfully.")

def clear_text():
    code_input.delete("1.0", tk.END)
    output_area.config(state=tk.NORMAL)
    output_area.delete("1.0", tk.END)
    output_area.config(state=tk.DISABLED)
    status_var.set("Cleared input and output.")

def open_file():
    file_path = filedialog.askopenfilename(title="Open Source File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            code_input.delete("1.0", tk.END)
            code_input.insert(tk.END, file.read())
        status_var.set(f"Loaded file: {file_path}")

def save_output():
    file_path = filedialog.asksaveasfilename(title="Save Output", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(output_area.get("1.0", tk.END))
        status_var.set(f"Output saved to: {file_path}")

# Main window with ttk styling
root = tk.Tk()
root.title("Enhanced Compiler Simulator")
root.geometry("950x750")
root.configure(bg="#EEF2F7")

# Configure style
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", background="#EEF2F7", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11, "bold"), foreground="#FFFFFF", background="#007ACC")
style.map("TButton", background=[("active", "#005F9E")])
style.configure("TFrame", background="#EEF2F7")

# Create menu bar
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save Output", command=save_output)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Enhanced Compiler Simulator\n\nCreated with Tkinter and ttk."))
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

# Main frame with padding
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Title label
title_label = ttk.Label(main_frame, text="Enhanced Compiler Simulator", font=("Segoe UI", 20, "bold"))
title_label.pack(pady=(0, 15))

# Input label
input_label = ttk.Label(main_frame, text="Enter Source Code (supports multiple statements):")
input_label.pack(anchor="w", pady=(0, 5))

# Source code input area
code_input = scrolledtext.ScrolledText(main_frame, height=10, wrap=tk.WORD, font=("Consolas", 12), bg="#F7F9FB")
code_input.pack(fill=tk.BOTH, expand=False, pady=(0, 15))

# Button frame
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill=tk.X, pady=(0, 15))

compile_button = ttk.Button(button_frame, text="Compile", command=compile_code)
compile_button.pack(side=tk.LEFT, padx=(0, 10))

clear_button = ttk.Button(button_frame, text="Clear", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=(0, 10))

exit_button = ttk.Button(button_frame, text="Exit", command=root.quit)
exit_button.pack(side=tk.LEFT)

# Output label
output_label = ttk.Label(main_frame, text="Compilation Output:")
output_label.pack(anchor="w", pady=(0, 5))

# Output area
output_area = scrolledtext.ScrolledText(main_frame, height=20, wrap=tk.WORD, font=("Consolas", 12), bg="#F7F9FB", state=tk.DISABLED)
output_area.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

# Status bar
status_var = tk.StringVar(value="Ready")
status_bar = ttk.Label(root, textvariable=status_var, relief=tk.SUNKEN, anchor="w", font=("Segoe UI", 10))
status_bar.pack(fill=tk.X, side=tk.BOTTOM)

root.mainloop()