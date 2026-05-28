from DisplayTime import get_time
from CheckActive import set_active, set_deactive, is_active

import tkinter as tk
import csv

def update_clock():

    current_time = get_time()

    if is_active():
        status_label.config(text="ACTIVE")
    else:
        status_label.config(text="INACTIVE")

    time_label.config(text=current_time)

    root.after(1000, update_clock)

def test_input():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    book_title = book_title_entry.get()
    publisher = publisher_entry.get()
    series_num = series_num_entry.get()

    output_label.config(text=f"Sumbitted {book_title} by {first_name} {last_name} to CSV file")

    book_list = [book_title, publisher, series_num, first_name, last_name]
    with open('booklisttest.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(book_list)
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    book_title_entry.delete(0, tk.END)
    publisher_entry.delete(0, tk.END)
    series_num_entry.delete(0, tk.END)

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

book_title_label = tk.Label(root, text="Book Title")
book_title_label.pack()

book_title_entry = tk.Entry(root)
book_title_entry.pack()

publisher_label = tk.Label(root, text="Publisher")
publisher_label.pack()

publisher_entry = tk.Entry(root)
publisher_entry.pack()

first_name_label = tk.Label(root, text="Author First Name")
first_name_label.pack()

first_name_entry = tk.Entry(root)
first_name_entry.pack()

last_name_label = tk.Label(root, text="Author Last Name")
last_name_label.pack()

last_name_entry = tk.Entry(root)
last_name_entry.pack()

series_num_label = tk.Label(root, text="Series Number")
series_num_label.pack()

series_num_entry = tk.Entry(root)
series_num_entry.pack()

test_button = tk.Button(root, text="Submit", command=test_input)
test_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

update_clock()

root.mainloop()
