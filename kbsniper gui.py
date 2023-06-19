import tkinter as tk
import requests
from mojang import API
import threading
import time



stop_flag = False  # Initialize the stop_flag
update_interval = 2  # Update interval in seconds

def update_response():
    global stop_flag
    username = username_entry.get()
    key = key_entry.get()
    api = API()
    kbcats = api.get_uuid(username)

    while True:
        if stop_flag:
            break

        def get_info(call):
            return requests.get(call).json()

        kbc = f"https://api.hypixel.net/status?key={key}&uuid={kbcats}"
        ats = get_info(kbc)
        kbcat = ats["session"]
        response_label.config(text=kbcat)

        countdown = update_interval
        while countdown > 0:
            countdown_label.config(text=f"Next update in {countdown} seconds")
            time.sleep(1)
            countdown -= 1

def button_click():
    global stop_flag
    if not stop_flag:
        stop_flag = True  # Stop the update_response function
        button.config(text="Start")
    else:
        stop_flag = False  # Start the update_response function
        button.config(text="Stop")
        thread = threading.Thread(target=update_response)
        thread.start()

window = tk.Tk()
window.title("kb sniper")
window.attributes('-alpha',0.5)
window.configure(bg="#2e2e2e")

# Create a title label
title_label = tk.Label(window, text="kb sniper", fg="#855da6", font=("Arial", 24), bg="#2e2e2e")
title_label.pack(pady=20)

# Create a username label and entry
username_label = tk.Label(window, text="Username:", fg="#855da6", bg="#2e2e2e")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

key_label = tk.Label(window, text="Key:", fg="#855da6", bg="#2e2e2e")
key_label.pack()
key_entry = tk.Entry(window)
key_entry.pack()

# Create a response label
response_label = tk.Label(window, text="", font=("Arial", 12), bg="#2e2e2e")
response_label.pack(pady=10)

# Create a countdown label
countdown_label = tk.Label(window, text="", font=("Arial", 12), bg="#2e2e2e")
countdown_label.pack()

# Create a button
button = tk.Button(window, text="Start", bg="#212121", command=button_click)
button.pack()

window.mainloop()
