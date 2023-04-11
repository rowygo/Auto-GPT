# Import necessary modules
import keyboard
import time
import pywinauto

# Define actions for various hotkeys
def toggle_mic():
    pywinauto.mouse.click(button='middle')
    time.sleep(0.05)
    pywinauto.mouse.click(button='middle')

def toggle_flashlight():
    keyboard.press_and_release('t')

# Set up hotkeys
keyboard.add_hotkey('F11', toggle_mic)
keyboard.add_hotkey('F12', toggle_flashlight)

# Start the event listener
keyboard.wait()
