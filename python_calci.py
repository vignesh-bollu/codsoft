import tkinter as tk

def add_to_display(value):
    current = display_var.get()
    if current == "Error":
        display_var.set("")
    display_var.set(current + value)

def clear_display():
    display_var.set("")

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="pink")

display_var = tk.StringVar(root, "")

display = tk.Entry(root, textvariable=display_var, font=("Helvetica", 24), justify="right", bg="white")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0

for text in button_texts:
    if text == 'C':
        tk.Button(root, text=text, font=("Helvetica", 16), bg="gray", command=clear_display).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == '=':
        tk.Button(root, text=text, font=("Helvetica", 16), bg="gray", command=calculate).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(root, text=text, font=("Helvetica", 16), bg="gray", command=lambda t=text: add_to_display(t)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
