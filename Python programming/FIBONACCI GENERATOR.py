import tkinter as tk
from tkinter import messagebox

def generate_fibonacci():
    try:
        count = int(entry.get())
        if count <= 0:
            messagebox.showerror("Error", "Please enter a positive integer")
            return
        
        a, b = 0, 1
        result = "Fibonacci sequence:\n"
        
        for i in range(count):
            result += f"{a}\n"
            a, b = b, a + b
        
        output_text.delete(1.0, tk.END)  
        output_text.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")


root = tk.Tk()
root.title("Fibonacci Sequence Generator")


root.geometry("400x400")
root.resizable(False, False)


label = tk.Label(root, text="How many Fibonacci numbers do you want?")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate", command=generate_fibonacci)
generate_button.pack(pady=10)

output_text = tk.Text(root, height=15, width=30)
output_text.pack(pady=10)

root.mainloop()