import tkinter as tk

def toggle_message():
    if label_message["text"]:
        label_message.config(text="")  # Clear message
    else:
        label_message.config(text="App Running Successfully")  # Show message

# Create main window
root = tk.Tk()
root.title("DevOps Application")
root.geometry("300x200")

# Heading label
label_heading = tk.Label(root, text="DevOps Application", font=("Arial", 14, "bold"))
label_heading.pack(pady=10)

# Message label
label_message = tk.Label(root, text="", font=("Arial", 12))
label_message.pack(pady=10)

# Button to toggle message
btn_toggle = tk.Button(root, text="Toggle Message", command=toggle_message)
btn_toggle.pack(pady=10)

# Run the application
root.mainloop()
