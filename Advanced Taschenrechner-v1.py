import math
import tkinter as tk
from tkinter import messagebox

# Grundfunktionen
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Fehler: Division durch Null"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Fehler: Negative Zahl unter der Wurzel"
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x):
    if x <= 0:
        return "Fehler: Logarithmus nur für positive Zahlen"
    return math.log(x)

def exp(x):
    return math.exp(x)

# Funktion zur Umrechnung von Speicherdaten-Typen (Dezimal und Binär)
def convert_storage(value, from_unit, to_unit):
    units_decimal = ['B', 'KB', 'MB', 'GB', 'TB']
    units_binary = ['B', 'KiB', 'MiB', 'GiB', 'TiB']
    
    # Umrechnung zwischen den Dezimal-Einheiten
    if from_unit in units_decimal and to_unit in units_decimal:
        from_index = units_decimal.index(from_unit)
        to_index = units_decimal.index(to_unit)
        difference = to_index - from_index
        return value * (1000 ** difference)
    
    # Umrechnung zwischen den Binär-Einheiten
    elif from_unit in units_binary and to_unit in units_binary:
        from_index = units_binary.index(from_unit)
        to_index = units_binary.index(to_unit)
        difference = to_index - from_index
        return value * (1024 ** difference)
    
    # Umrechnung zwischen Dezimal- und Binär-Einheiten
    elif from_unit in units_decimal and to_unit in units_binary:
        from_index = units_decimal.index(from_unit)
        to_index = units_binary.index(to_unit)
        difference = to_index - from_index
        return value * (1024 ** difference) / 1000
    
    # Umrechnung zwischen Binär- und Dezimal-Einheiten
    elif from_unit in units_binary and to_unit in units_decimal:
        from_index = units_binary.index(from_unit)
        to_index = units_decimal.index(to_unit)
        difference = to_index - from_index
        return value * (1000 ** difference) / 1024

    return value  # Falls keine gültige Umrechnung gefunden wird

# Button-Klick-Handler
def button_click(value):
    current_text = entry_var.get()
    if current_text != value:  # Wenn der Wert nicht bereits im Eingabefeld ist, füge ihn hinzu
        entry_var.set(current_text + str(value))

def clear_entry():
    entry_var.set("")

def calculate():
    try:
        expression = entry_var.get()
        
        # Ersetze das Wurzelsymbol '√' durch 'math.sqrt(' und schließe es mit einer Klammer
        if '√' in expression:
            expression = expression.replace("√", "math.sqrt(") + ")"
        
        # Ersetze Potenzzeichen (^) durch ** für Python
        expression = expression.replace("^", "**")
        
        # Berechne das Ergebnis
        result.set(eval(expression))
    except Exception as e:
        messagebox.showerror("Fehler", "Ungültige Eingabe.")

def handle_keypress(event):
    key = event.keysym
    if key in "1234567890" and entry_var.get() != key:
        button_click(key)
    elif key == "Return":  # Enter
        calculate()
    elif key == "BackSpace":
        clear_entry()
    elif key == "plus" or key == "+":
        button_click("+")
    elif key == "minus" or key == "-":
        button_click("-")
    elif key == "asterisk" or key == "*":
        button_click("*")
    elif key == "slash" or key == "/":
        button_click("/")
    elif key == "equal" or key == "=":
        calculate()
    elif key == "period" or key == ".":
        button_click(".")
    elif key == "shift_R" or key == "shift_L":
        button_click("√")  # Für die Quadratwurzel mit Shift

# Tkinter-Setup
root = tk.Tk()
root.title("Advance Calculator")

# Setze ein dunkles Hintergrund- und Textdesign
root.configure(bg="#2e2e2e")  # Dunkelgrauer Hintergrund für das Fenster
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bg="#444444", fg="white", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 20), bg="#2e2e2e", fg="white")
result_label.grid(row=1, column=0, columnspan=4)

# Buttons für die Speicherdaten-Umrechnung
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('^', 5, 3),
    ('√', 6, 0), ('sin', 6, 1), ('cos', 6, 2), ('tan', 6, 3),
    ('log', 7, 0), ('exp', 7, 1), ('C', 7, 2), ('=', 7, 3),
    ('B->KB', 8, 0), ('KB->MB', 8, 1), ('MB->GB', 8, 2), ('GB->TB', 8, 3),
    ('B->KiB', 9, 0), ('KiB->MiB', 9, 1), ('MiB->GiB', 9, 2), ('GiB->TiB', 9, 3),
    ('KB->B', 10, 0), ('MB->KB', 10, 1), ('GB->MB', 10, 2), ('TB->GB', 10, 3),
    ('KiB->B', 11, 0), ('MiB->KiB', 11, 1), ('GiB->MiB', 11, 2), ('TiB->GiB', 11, 3)
]

# Dunkle Buttons für alle
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 20), command=calculate, bg="#666666", fg="white", activebackground="#888888")
    elif text == "C":
        btn = tk.Button(root, text=text, font=("Arial", 20), command=clear_entry, bg="#666666", fg="white", activebackground="#888888")
    elif text == "√":
        btn = tk.Button(root, text=text, font=("Arial", 20), command=lambda: button_click("√"), bg="#666666", fg="white", activebackground="#888888")
    elif text == "sin":
        btn = tk.Button(root, text=text, font=("Arial", 20), command=lambda: button_click("sin("), bg="#666666", fg="white", activebackground="#888888")
    elif text == "cos":
        btn = tk.Button(root, text=text, font=("Arial", 20), command=lambda: button_click("cos("), bg="#666666", fg="white", activebackground="#888888")
    elif text == "tan":
        btn = tk.Button(root, text=text, font=("Arial", 20), command=lambda: button_click("tan("), bg="#666666", fg="white", activebackground="#888888")
    elif text == "log":
        btn = tk.Button(root, text=text, font=("Arial", 20), command=lambda: button_click("log("), bg="#666666", fg="white", activebackground="#888888")
    elif text == "exp":
        btn = tk.Button(root, text=text, font=("Arial", 20), command=lambda: button_click("exp("), bg="#666666", fg="white", activebackground="#888888")
    elif text in ['B->KB', 'KB->MB', 'MB->GB', 'GB->TB', 'B->KiB', 'KiB->MiB', 'MiB->GiB', 'GiB->TiB',
                  'KB->B', 'MB->KB', 'GB->MB', 'TB->GB', 'KiB->B', 'MiB->KiB', 'GiB->MiB', 'TiB->GiB']:
        btn = tk.Button(root, text=text, font=("Arial", 20), command=lambda t=text: handle_storage_conversion(t), bg="#666666", fg="white", activebackground="#888888")
    else:
        btn = tk.Button(root, text=text, font=("Arial", 20), command=lambda t=text: button_click(t), bg="#666666", fg="white", activebackground="#888888")
    
    btn.grid(row=row, column=col, sticky="nsew")

# Funktion zur Handhabung der Speicherdaten-Umrechnung
def handle_storage_conversion(conversion_type):
    try:
        value = float(entry_var.get().split()[0])  # Die Zahl ohne Einheiten
        if conversion_type == 'B->KB':
            result.set(f"{value / 1000} KB")
        elif conversion_type == 'KB->MB':
            result.set(f"{value / 1000} MB")
        elif conversion_type == 'MB->GB':
            result.set(f"{value / 1000} GB")
        elif conversion_type == 'GB->TB':
            result.set(f"{value / 1000} TB")
        elif conversion_type == 'B->KiB':
            result.set(f"{value / 1024} KiB")
        elif conversion_type == 'KiB->MiB':
            result.set(f"{value / 1024} MiB")
        elif conversion_type == 'MiB->GiB':
            result.set(f"{value / 1024} GiB")
        elif conversion_type == 'GiB->TiB':
            result.set(f"{value / 1024} TiB")
        
        # Rückwärtsumrechnungen
        elif conversion_type == 'KB->B':
            result.set(f"{value * 1000} B")
        elif conversion_type == 'MB->KB':
            result.set(f"{value * 1000} KB")
        elif conversion_type == 'GB->MB':
            result.set(f"{value * 1000} MB")
        elif conversion_type == 'TB->GB':
            result.set(f"{value * 1000} GB")
        elif conversion_type == 'KiB->B':
            result.set(f"{value * 1024} B")
        elif conversion_type == 'MiB->KiB':
            result.set(f"{value * 1024} KiB")
        elif conversion_type == 'GiB->MiB':
            result.set(f"{value * 1024} MiB")
        elif conversion_type == 'TiB->GiB':
            result.set(f"{value * 1024} GiB")
    except ValueError:
        messagebox.showerror("Fehler", "Ungültige Eingabe für die Umrechnung.")
    
root.mainloop()
