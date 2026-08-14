import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

entry = tk.Entry(root, width=100)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

listbox = tk.Listbox(root, width=200, height=300)
listbox.pack(pady=10)



root.mainloop()
