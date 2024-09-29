import tkinter as tk

class TaskManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.tasks = []

        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.mark_button = tk.Button(self.root, text="Mark Task as Complete", command=self.mark_task)
        self.mark_button.pack()

        self.save_button = tk.Button(self.root, text="Save Task List", command=self.save_task_list)
        self.save_button.pack()

    def add_task(self):
        task = input("Enter a new task: ")
        self.tasks.append(task)
        self.task_listbox.insert(tk.END, task)

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()[0]
        old_task = self.tasks[selected_task_index]
        new_task = input(f"Enter the new task (current: {old_task}): ")
        self.tasks[selected_task_index] = new_task
        self.task_listbox.delete(selected_task_index)
        self.task_listbox.insert(selected_task_index, new_task)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()[0]
        del self.tasks[selected_task_index]
        self.task_listbox.delete(selected_task_index)

    def mark_task(self):
        selected_task_index = self.task_listbox.curselection()[0]
        old_task = self.tasks[selected_task_index]
        new_task = f"[X] {old_task}"
        self.tasks[selected_task_index] = new_task
        self.task_listbox.delete(selected_task_index)
        self.task_listbox.insert(selected_task_index, new_task)

    def save_task_list(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        print("Task list saved!")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TaskManager()
    game.run()