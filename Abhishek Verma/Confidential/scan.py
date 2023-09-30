import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Custom Window Size")

# Set the window size to 1280x720
window_width = 1280
window_height = 720
root.geometry(f"{window_width}x{window_height}")

def change_background_color(color):
    root.configure(background=color)


root.configure(background="#f5f0f5")

change_color_button = tk.Button(root, text="Change Background Color", command=lambda: change_background_color("lightblue"))
change_color_button.pack()





# Create a button and position it using place
button = tk.Button(root, text="Placed Button")
button.place(x=50, y=50)  # Adjust x, y as needed



# Start the main event loop
root.mainloop()
