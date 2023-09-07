# Calculator 
import tkinter as tk

def calculate():
     number_one = float(entry_1.get())
     number_two = float(entry_2.get())
     operation = operation_var.get()
    
     if operation == '+':
         result = number_one + number_two
     elif operation == '-':
         result = number_one - number_two
     elif operation == '*':
         result = number_one * number_two
     elif operation == '/':
         result = number_one / number_two
     else:
         result = 'Syntax Error'
        
     result_label.config(text=result)
        
root = tk.Tk()

number_label_1 = tk.Label(root, text="Number 1:")
number_label_1.grid(row=0, column=0)

entry_1 = tk.Entry(root)
entry_1.grid(row=0, column=1)

number_label_2 = tk.Label(root, text="Number 2:")
number_label_2.grid(row=1, column=0)

entry_2 = tk.Entry(root)
entry_2.grid(row=1, column=1)

operation_var = tk.StringVar(value='+')
operation_label = tk.Label(root, text="Operation:")
operation_label.grid(row=2, column=0)

operation_option_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operation_option_menu.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=1)

root.mainloop()


