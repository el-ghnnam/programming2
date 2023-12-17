import tkinter as tk
from tkinter import messagebox

def submit_form():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()

    # You can perform validation and store the data in a database/file.
    # For simplicity, this example just displays the entered data in the console.
    print("Username:", username)
    print("Password:", password)
    print("Email:", email)

    messagebox.showinfo("Registration Successful", "Registration successful!")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place labels and entry widgets for username, password, and email
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=10)

# Create and place a submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
