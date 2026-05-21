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

update_clock()

root.mainloop()
