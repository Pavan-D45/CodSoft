import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Calculator")
        self.geometry("400x600")
        self.configure(bg='#f0f0f0')

        self.create_widgets()

    def create_widgets(self):
        # Create and place the display entry
        self.display = tk.Entry(self, font=('Arial', 28), borderwidth=2, relief='solid', bg='#eaeaea', justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky='nsew')

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create buttons and place them in the grid
        for i, button in enumerate(buttons):
            if button == '=':
                btn = tk.Button(self, text=button, font=('Arial', 22), bg='#4CAF50', fg='white', command=self.calculate)
            else:
                btn = tk.Button(self, text=button, font=('Arial', 22), bg='#ffffff', command=lambda b=button: self.on_button_click(b))
            row = (i // 4) + 1
            col = i % 4
            btn.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')

        # Adjust the grid weights
        for r in range(5):
            self.grid_rowconfigure(r, weight=1)
        for c in range(4):
            self.grid_columnconfigure(c, weight=1)

    def on_button_click(self, char):
        current_text = self.display.get()
        if char in '0123456789.':
            self.display.insert(tk.END, char)
        elif char in '+-*/':
            if current_text and current_text[-1] not in '+-*/':
                self.display.insert(tk.END, char)
        elif char == '=':
            self.calculate()

    def calculate(self):
        try:
            expression = self.display.get()
            # Use eval to compute the result of the arithmetic expression
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            self.display.delete(0, tk.END)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()