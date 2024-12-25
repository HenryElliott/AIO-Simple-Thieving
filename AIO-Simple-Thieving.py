import pyautogui
import time
import random
import keyboard
import threading
from tkinter import Tk, Label, Button, StringVar, Frame, Text, Scrollbar, Canvas
from tkinter import font
from datetime import datetime

# IMPORTANT REPLACE WITH YOUR OWN COORDINATES!!!
# Coordinates for thieving (Coords 1) and fallback (Coords 2)
coords_1 = (625, 248)  # Replace x1, y1 with the actual Coords 1
coords_2 = (1448, 506)  # Replace x2, y2 with the actual Coords 2

running = False
start_time = None
runtime_var = None  
status_var = None

def random_sleep(min_time=1.5, max_time=1.5):
    """Pauses for a set or randomized time. Currently fixed to 1.5 seconds."""
    time.sleep(random.uniform(min_time, max_time))

def click(coords):
    pyautogui.moveTo(coords[0] + random.randint(-3, 3), coords[1] + random.randint(-3, 3), duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    log_action(f"Clicked on: {coords}")  
    print(f"Mouse clicked at: {coords}")  

def thieving_script():
    global running, start_time
    start_time = datetime.now()
    update_status("Running")
    log_action("Thieving script started.")
    print("Thieving script started. Press Ctrl+Shift+C to stop.")
    try:
        while running:
            for _ in range(28):
                if not running:  
                    break
                click(coords_1)
                random_sleep(1.5, 1.5)  

            if running:
                click(coords_2)
                random_sleep()
            update_runtime()
    except Exception as e:
        print(f"Error occurred: {e}")
    update_status("Stopped")
    log_action("Thieving script stopped.")
    print("Thieving script stopped.")

def toggle_script():
    global running
    if running:
        running = False
        update_status("Stopping...")
        log_action("Stopping the script...")
        print("Stopping thieving script...")
    else:
        running = True
        threading.Thread(target=thieving_script).start()

def update_runtime():
    if start_time:
        elapsed_time = datetime.now() - start_time
        runtime_var.set(f"Runtime: {str(elapsed_time).split('.')[0]}")  

def update_status(status):
    status_var.set(f"Status: {status}")

def log_action(action):
    log_text.insert('end', f"{action}\n")
    log_text.yview('end')  

def setup_gui():
    global runtime_var, status_var, log_text
    root = Tk()
    root.title("Thieving Script")
    root.geometry("500x400")
    root.configure(bg="#2C2F38")  
    root.resizable(False, False)  

    custom_font = font.Font(family="Roboto", size=12)
    title_font = font.Font(family="Roboto", size=18, weight="bold")

    frame = Frame(root, bg="#36393F", relief="solid", bd=2, padx=20, pady=20)
    frame.pack(padx=20, pady=20)

    Label(frame, text="Thieving Script", font=title_font, fg="#FFFFFF", bg="#36393F").grid(row=0, column=0, pady=10)

    status_var = StringVar()
    runtime_var = StringVar()

    status_label = Label(frame, textvariable=status_var, font=custom_font, fg="#FFFFFF", bg="#36393F")
    status_label.grid(row=1, column=0, pady=5)

    runtime_label = Label(frame, textvariable=runtime_var, font=custom_font, fg="#FFFFFF", bg="#36393F")
    runtime_label.grid(row=2, column=0, pady=5)

    start_button = Button(frame, text="Start/Stop (Ctrl+Shift+C)", command=toggle_script, font=("Arial", 12), bg="#5865F2", fg="#FFFFFF", relief="raised", bd=4)
    start_button.grid(row=3, column=0, pady=15, padx=10, ipadx=10, ipady=5)

    start_button.bind("<Enter>", lambda e: start_button.config(bg="#4752C4"))
    start_button.bind("<Leave>", lambda e: start_button.config(bg="#5865F2"))

    log_text = Text(root, width=40, height=10, font=("Courier", 10), wrap="word", bg="#2C2F38", fg="#FFFFFF", bd=2, padx=10, pady=10)
    log_text.pack(padx=20, pady=20)

    scrollbar = Scrollbar(root, command=log_text.yview)
    log_text.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    update_status("Stopped")
    runtime_var.set("Runtime: 00:00:00")

    def refresh_gui():
        if running:
            update_runtime()
        root.after(1000, refresh_gui)  

    refresh_gui()
    root.mainloop()

keyboard.add_hotkey('ctrl+shift+c', toggle_script)

if __name__ == "__main__":
    threading.Thread(target=setup_gui).start()
    print("Press Ctrl+Shift+C to start/stop the script.")
    keyboard.wait('esc')  
