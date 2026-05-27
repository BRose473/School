from DisplayTime import get_time
from CheckActive import set_active, set_deactive, is_active

import tkinter as tk

def update_clock():

    current_time = get_time()

    if is_active():
        status_label.config(text="ACTIVE")
    else:
        status_label.config(text="INACTIVE")

    time_label.config(text=current_time)

    root.after(1000, update_clock)

def test_input():
    name = name_entry.get()
    task = task_entry.get()
    output_label.config(text=f"Hello {name}. Good luck with {task}")

#GUI
root = tk.Tk()
root.title("Session Dashboard")
root.geometry("400x200")

time_label = tk.Label(root, font=("Arial", 18))
time_label.pack(pady=10)

status_label = tk.Label(root, text="INACTIVE", font=("Arial", 14))
status_label.pack(pady = 10)

start_button = tk.Button(root, text="Start", command=set_active)
start_button.pack(pady=5)


stop_button = tk.Button(root, text="Stop", command=set_deactive)
stop_button.pack(pady=5)

name_label = tk.Label(root, text="Name")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

task_label = tk.Label(root, text="Task")
task_label.pack()

task_entry = tk.Entry(root)
task_entry.pack()

test_button = tk.Button(root, text="Submit", command=test_input)
test_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

update_clock()

root.mainloop()
