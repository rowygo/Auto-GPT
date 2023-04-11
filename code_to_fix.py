import os

file_path = r"C:\Users\rowyg\Desktop\New folder (2)\Phasmophobia.py"
script_text = """import datetime
import time
import winsound
from tkinter import *

def countdown(t):
    while t:
        seconds = t % 60
        if seconds <= 9:
            seconds = '0' + str(seconds)
        display = str(seconds)
        countdownLabel['text'] = display
        root.update()
        time.sleep(1)
        t -= 1
    else:
        countdownLabel['text'] = 'Game Over'
        for i in range(5):
            winsound.Beep(1000, 500)

root = Tk()
root.geometry('150x150')
root.title('Phasmophobia Tracker')

countdownLabel = Label(root, font=('Verdana', 15, 'bold'), bg='white', fg='black')
countdownLabel.pack(fill=BOTH, expand=1)

t = 375
countdown(t)

root.mainloop()"""

# create the directory if it doesn't exist
if not os.path.exists(os.path.dirname(file_path)):
    os.makedirs(os.path.dirname(file_path))

# write the script to the file
with open(file_path, 'w') as file:
    file.write(script_text)

print(f"Successfully wrote script to file: {file_path}")
