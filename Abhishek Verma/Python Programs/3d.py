



























import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    for i in range(101):
        progress_bar['value'] = i
        root.update_idletasks()  # Update the GUI
        time.sleep(0.1)  # Simulate some work being done
    progress_bar['value'] = 0

root = tk.Tk()
root.title("Progress Bar Example")

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=20)

start_button = tk.Button(root, text="Start Progress", command=start_progress)
start_button.pack()

root.mainloop()
