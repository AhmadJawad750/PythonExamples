import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Input field
entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        button = tk.Button(row_frame, text=btn_text, font="Arial 18", relief="ridge", border=2)
        button.pack(side=tk.LEFT, expand=True, fill="both")
        button.bind("<Button-1>", click)

root.mainloop()
