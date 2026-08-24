import tkinter as tk  # Import Tkinter

root = tk.Tk()  # Create main window

root.title("Student Management System")  # Set window title
root.geometry("800x600")

title_label = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 24, "bold"),
)
title_label.pack(pady=20)


def add_student():
    student_id = id_entry.get()
    name = name_entry.get()
    phone_number = phone_entry.get()

    print(student_id)
    print(name)
    print(phone_number)

    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)


add_button = tk.Button(
    root,
    text="Add Student",
    command=add_student,
)

add_button.pack(pady=10)

form_frame = tk.Frame(root)
form_frame.pack(pady=20)

id_label = tk.Label(form_frame, text="Student ID:")
id_label.grid(row=0, column=0, padx=10, pady=5)

id_entry = tk.Entry(form_frame)
id_entry.grid(row=0, column=1, padx=10, pady=5)

name_label = tk.Label(form_frame, text="Name:")
name_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = tk.Entry(form_frame)
name_entry.grid(row=1, column=1, padx=10, pady=5)

phone_label = tk.Label(form_frame, text="Phone Number:")
phone_label.grid(row=2, column=0, padx=10, pady=5)

phone_entry = tk.Entry(form_frame)
phone_entry.grid(row=2, column=1, padx=10, pady=5)

id_entry.get()

root.mainloop()
