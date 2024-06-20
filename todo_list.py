import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_done():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(task_index, {'bg':'blue'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

def clear_list():
    listbox_tasks.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create GUI components
frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, bg="yellow")
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_mark_done = tk.Button(root, text="Mark Done", width=48, command=mark_done)
button_mark_done.pack()

button_clear_list = tk.Button(root, text="Clear List", width=48, command=clear_list)
button_clear_list.pack()

root.mainloop()
