import datetime
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

root.mainloop()
