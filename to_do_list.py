import tkinter as tk
from tkinter import messagebox, ttk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List")
        self.root.geometry("450x500")
        self.root.configure(bg="#fefefe")

        self.tasks = []

        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 10), padding=6)
        style.configure("TLabel", background="#fefefe")

        self.heading = ttk.Label(self.root, text="My To-Do List", font=("Segoe UI", 20, "bold"), anchor="center")
        self.heading.pack(pady=15)

        self.entry_frame = tk.Frame(self.root, bg="#fefefe")
        self.entry_frame.pack(pady=10)

        self.task_var = tk.StringVar()
        self.task_input = ttk.Entry(self.entry_frame, width=30, textvariable=self.task_var, font=("Segoe UI", 11))
        self.task_input.grid(row=0, column=0, padx=5)
        self.task_input.insert(0, "Enter your task...")

        # Clear placeholder when clicked
        self.task_input.bind("<FocusIn>", self.clear_placeholder)
        self.task_input.bind("<FocusOut>", self.add_placeholder)

        self.add_btn = ttk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=1, padx=5)

        # Scrollable listbox
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(self.list_frame, height=12, width=45, font=("Segoe UI", 11),
                                  yscrollcommand=self.scrollbar.set, selectbackground="#cce7ff", bd=0, highlightthickness=1,
                                  relief="solid", selectmode=tk.SINGLE)
        self.listbox.pack()
        self.scrollbar.config(command=self.listbox.yview)

        self.btn_frame = tk.Frame(self.root, bg="#fefefe")
        self.btn_frame.pack(pady=10)

        self.update_btn = ttk.Button(self.btn_frame, text="Update", command=self.update_task)
        self.update_btn.grid(row=0, column=0, padx=10)

        self.delete_btn = ttk.Button(self.btn_frame, text="Delete", command=self.delete_task)
        self.delete_btn.grid(row=0, column=1, padx=10)

    def clear_placeholder(self, event):
        if self.task_input.get() == "Enter your task...":
            self.task_input.delete(0, tk.END)

    def add_placeholder(self, event):
        if not self.task_input.get():
            self.task_input.insert(0, "Enter your task...")

    def add_task(self):
        task = self.task_input.get().strip()
        if task and task != "Enter your task...":
            self.tasks.append(task)
            self.refresh_list()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Field", "Please enter a valid task.")

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, 1):
            self.listbox.insert(tk.END, f"{idx}. {task}")

    def update_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            new_text = self.task_input.get().strip()
            if new_text and new_text != "Enter your task...":
                self.tasks[selected_index] = new_text
                self.refresh_list()
                self.task_input.delete(0, tk.END)
            else:
                messagebox.showwarning("Empty Field", "Please enter updated task text.")
        except IndexError:
            messagebox.showerror("No Selection", "Please select a task to update.")

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            del self.tasks[selected_index]
            self.refresh_list()
        except IndexError:
            messagebox.showerror("No Selection", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
