'''
# This code is a simple calculator that performs addition, subtraction, multiplication, and division using a GUI with tkinter.
import tkinter as tk
from tkinter import messagebox

def evaluate_expression():
    expr = entry.get()
    try:
        # Only allow safe evaluation
        result = eval(expr, {"__builtins__": None}, {})
        result_label.config(text=f"Result: {result}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except Exception:
        messagebox.showerror("Error", "Invalid expression.")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

calc_button = tk.Button(root, text="Calculate", command=evaluate_expression)
calc_button.grid(row=1, column=0, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()

'''


# This code is a simple calculator that performs addition, subtraction, multiplication, and division. This code is without GUI and uses basic input/output in the console.
def Addition(x,y):
    return x+y
def Subtraction(x,y):
    return x-y
def Multiplication(x,y):
    return x*y
def Division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1/2/3/4) ?: ")
if choice =='1':
    print(f"{x} + {y} = {Addition(x,y)}")
elif choice =='2':
    print(f"{x} - {y} = {Subtraction(x,y)}")
elif choice =='3':
    print(f"{x} * {y} = {Multiplication(x,y)}")
elif choice =='4':
    try:
        print(f"{x} / {y} = {round(Division(x,y),3)}")
    except ZeroDivisionError as e:
        print(e)
else:
    print("Invalid choice. Please select a valid operation (1/2/3/4).")



    
