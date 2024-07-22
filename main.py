import json
import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.todo_list = ToDoList()

        self.task_title_label = tk.Label(master, text="Task Title:")
        self.task_title_label.grid(row=0, column=0, padx=10, pady=10)

        self.task_title_entry = tk.Entry(master)
        self.task_title_entry.grid(row=0, column=1, padx=10, pady=10)

        self.task_details_label = tk.Label(master, text="Task Details:")
        self.task_details_label.grid(row=1, column=0, padx=10, pady=10)

        self.task_details_entry = tk.Entry(master)
        self.task_details_entry.grid(row=1, column=1, padx=10, pady=10)

        self.priority_label = tk.Label(master, text="Priority:")
        self.priority_label.grid(row=2, column=0, padx=10, pady=10)

        self.priority_entry = tk.Entry(master)
        self.priority_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.list_button = tk.Button(master, text="List Tasks", command=self.list_tasks)
        self.list_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.complete_button = tk.Button(master, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.remove_button = tk.Button(master, text="Remove Completed Tasks", command=self.remove_completed_tasks)
        self.remove_button.grid(row=6, column=0, columnspan=2, pady=10)

    def get_task_index(self):
        try:
            task_index = simpledialog.askinteger("Task Index", "Enter the task index:")
            return task_index if task_index is not None and task_index > 0 else None
        except ValueError:
            return None

    def list_tasks(self):
        tasks = self.todo_list.list_tasks()
        if not tasks:
            messagebox.showinfo("To-Do List", "To-Do List is empty.")
        else:
            messagebox.showinfo("To-Do List", tasks)

    def complete_task(self):
        task_index = self.get_task_index()
        if task_index is not None:
            self.todo_list.complete_task(task_index)
            messagebox.showinfo("Success", "Task marked as completed.")
        else:
            messagebox.showerror("Error", "Please select a task.")

    def remove_completed_tasks(self):
        self.todo_list.remove_completed_tasks()
        messagebox.showinfo("Success", "Completed tasks removed.")

    def add_task(self):
        title = self.task_title_entry.get()
        details = self.task_details_entry.get()
        priority = self.priority_entry.get()
        if title and details and priority:
            self.todo_list.add_task(title, details, priority)
            self.list_tasks()
            messagebox.showinfo("Success", "Task added successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

class ToDoList:
    def __init__(self, filename="todolist.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                tasks = json.load(file)
            return tasks
        except FileNotFoundError:
            return {"tasks": []}

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, title, details, priority):
        new_task = {"title": title, "details": details, "priority": priority, "completed": False}
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def list_tasks(self):
        return "\n".join([f"{index + 1}. {task['title']} - Priority: {task['priority']} - Status: {'Completed' if task['completed'] else 'Pending'}" for index, task in enumerate(self.tasks["tasks"])])

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks["tasks"]):
            self.tasks["tasks"][task_index - 1]["completed"] = True
            self.save_tasks()

    def remove_completed_tasks(self):
        completed_tasks = [task for task in self.tasks["tasks"] if task["completed"]]
        if not completed_tasks:
            messagebox.showinfo("No Completed Tasks", "There are no completed tasks to remove.")
            return

        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if not task["completed"]]
        self.save_tasks()
        messagebox.showinfo("Success", "Completed tasks removed.")


def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
