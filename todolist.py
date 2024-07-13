import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        self.root.configure(bg="#87CEEB")

        self.tasks = []

        self.task_number = 0

        self.task_list = tk.Listbox(self.root, width=40, height=10, bg="#F2F2F2", fg="#000000")
        self.task_list.pack(pady=20)

        self.task_entry = tk.Entry(self.root, width=40, bg="#F2F2F2", fg="#000000")
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add task", command=self.add_task, bg="#34A853", fg="#FFFFFF")
        self.add_button.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Delete task", command=self.delete_task, bg="#FF3D3D", fg="#FFFFFF")
        self.delete_button.pack(pady=10)

        self.update_button = tk.Button(self.root, text="Update task", command=self.update_task, bg="#34A853", fg="#FFFFFF")
        self.update_button.pack(pady=10)

        self.save_button = tk.Button(self.root, text="Save tasks", command=self.save_tasks, bg="#34A853", fg="#FFFFFF")
        self.save_button.pack(pady=10)

        self.load_button = tk.Button(self.root, text="Load tasks", command=self.load_tasks, bg="#34A853", fg="#FFFFFF")
        self.load_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task!= "":
            self.tasks.append(task)
            self.task_list.insert(self.task_number, task)
            self.task_number += 1
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except:
            messagebox.showinfo("Error", "Select a task to delete")

    def update_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.task_entry.get()
            if task!= "":
                self.task_list.delete(task_index)
                self.tasks[task_index] = task
                self.task_list.insert(task_index, task)
                self.task_entry.delete(0, tk.END)
        except:
            messagebox.showinfo("Error", "Select a task to update")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = file.read().splitlines()
            self.task_list.delete(0, tk.END)
            for task in self.tasks:
                self.task_list.insert(tk.END, task)
        except:
            messagebox.showinfo("Error", "No tasks to load")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()
