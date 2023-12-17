import tkinter as tk
from time import strftime

def update_time():
    string_time = strftime('%H:%M:%S %p')
    label.config(text=string_time)
    label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label widget to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')

# Place the label widget in the center of the window
label.pack(anchor='center')

# Call the update_time function to update the time continuously
update_time()

# Run the Tkinter event loop
root.mainloop()

# here the list of color i can apply to clock
color_names = [
    'black', 'white', 'red', 'blue', 'green', 'yellow', 'orange',
    'purple', 'pink', 'brown', 'cyan', 'magenta', 'gray', 'lime green'
]