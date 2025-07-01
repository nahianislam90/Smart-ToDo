import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import csv
import os

# File to store tasks
TASKS_FILE = "tasks.csv"

# Create file with header if not exists
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Priority", "Due Date", "Due Time"])

# Create main window
root = tk.Tk()
root.title("Smart To-Do List")
root.geometry("500x350")
root.resizable(False, False)

# Task Title Label and Entry
tk.Label(root, text="Task Title *").pack(pady=(10, 0))
task_title_entry = tk.Entry(root, width=50)
task_title_entry.pack()

# Priority Label and Dropdown
tk.Label(root, text="Priority").pack(pady=(10, 0))
priority_var = tk.StringVar()
priority_var.set("Medium")  # default value
priority_menu = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")
priority_menu.pack()

# Due Date Label and Entry (YYYY-MM-DD)
tk.Label(root, text="Due Date (YYYY-MM-DD)").pack(pady=(10, 0))
due_date_entry = tk.Entry(root, width=50)
due_date_entry.pack()

# Due Time Label and Entry (HH:MM, 24-hour)
tk.Label(root, text="Due Time (HH:MM)").pack(pady=(10, 0))
due_time_entry = tk.Entry(root, width=50)
due_time_entry.pack()


def add_task():
    title = task_title_entry.get().strip()
    priority = priority_var.get()
    due_date = due_date_entry.get().strip()
    due_time = due_time_entry.get().strip()

    if not title:
        messagebox.showerror("Error", "Task Title is required.")
        return

    # Validate date format if entered
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror(
                "Error", "Due Date must be in YYYY-MM-DD format.")
            return

    # Validate time format if entered
    if due_time:
        try:
            datetime.strptime(due_time, "%H:%M")
        except ValueError:
            messagebox.showerror(
                "Error", "Due Time must be in HH:MM 24-hour format.")
            return

    # Save task to CSV
    with open(TASKS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([title, priority, due_date, due_time])

    messagebox.showinfo(
        "Task Added", f"Task '{title}' added with priority '{priority}' and due {due_date} {due_time}")

    # Clear inputs
    task_title_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    due_time_entry.delete(0, tk.END)
    priority_var.set("Medium")


def view_tasks():
    window = tk.Toplevel(root)
    window.title("Your Tasks")
    window.geometry("600x400")

    cols = ("Title", "Priority", "Due Date", "Due Time")
    tree = ttk.Treeview(window, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=140)
    tree.pack(fill=tk.BOTH, expand=True)

    # Load data from CSV
    with open(TASKS_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            tree.insert("", tk.END, values=row)


# Buttons
tk.Button(root, text="Add Task", command=add_task, width=20).pack(pady=10)
tk.Button(root, text="View Tasks", command=view_tasks, width=20).pack()

root.mainloop()
