import tkinter as tk
from tkinter import messagebox
import json
import os

# Define the path for storing tasks
TASKS_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    description = task_entry.get()
    if description:
        tasks = load_tasks()
        tasks.append({'description': description, 'completed': False})
        save_tasks(tasks)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task description cannot be empty.")

# Mark a task as completed
def complete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks = load_tasks()
        tasks[selected_index]['completed'] = True
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected to mark as completed.")

# Update the task list in the GUI
def update_task_list():
    task_listbox.delete(0, tk.END)
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        status = '✔️' if task['completed'] else '❌'
        task_listbox.insert(tk.END, f"{i + 1}. {task['description']} {[status]}")

# GUI setup
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")
root.configure(bg='#f0f0f0')

# Define font styles
title_font = ('Helvetica', 16, 'bold')
button_font = ('Helvetica', 12, 'bold')
entry_font = ('Helvetica', 12)

# Header Label
header_label = tk.Label(root, text="To-Do List", font=title_font, bg='#f0f0f0')
header_label.pack(pady=10)

# Entry field for new tasks
task_entry = tk.Entry(root, width=40, font=entry_font, bd=2, relief=tk.RAISED)
task_entry.pack(pady=10)

# Add Task Button
add_task_button = tk.Button(root, text="Add Task", command=add_task, font=button_font, bg='#4CAF50', fg='white', bd=0, relief=tk.RAISED)
add_task_button.pack(pady=5)

# Complete Task Button
complete_task_button = tk.Button(root, text="Complete Task", command=complete_task, font=button_font, bg='#2196F3', fg='white', bd=0, relief=tk.RAISED)
complete_task_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15, font=entry_font, bd=2, relief=tk.SUNKEN, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)

# Load initial tasks
update_task_list()

# Start the GUI event loop
root.mainloop()
