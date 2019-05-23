from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

### hardware
led1 = LED(17)
led2 = LED(27)
led3 = LED(23)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

### defininf function LED's
def led1Toggle():
    if led1.is_lit:
        led1.off()
        ledButton["text"] = "Turn ON LED"
    else:
        led1.on()
        ledButton["text"] = "Turn OFF LED"
            
def led2Toggle():
    if led2.is_lit:
        led2.off()
        ledButton["text"] = "Turn ON LED"
    else:
        led2.on()
        ledButton["text"] = "Turn OFF LED"

def led3Toggle():
    if led3.is_lit:
        led3.off()
        ledButton["text"] = "Turn ON LED"
    else:
        led3.on()
        ledButton["text"] = "Turn OFF LED"
            
def close():
    RPi.GPIO.cleanup()
    win.destroy()
    

ledButton = Button(win, text = 'Turn ON LED', font = myFont, command = led1Toggle, bg = 'bisque2', height = 3, width = 24)
ledButton.grid(row=0,column=1)
ledButton = Button(win, text = 'Turn ON LED', font = myFont, command = led2Toggle, bg = 'bisque2', height = 3, width = 24)
ledButton.grid(row=1,column=1)
ledButton = Button(win, text = 'Turn ON LED', font = myFont, command = led3Toggle, bg = 'bisque2', height = 3, width = 24)
ledButton.grid(row=2,column=1)
exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 3, width = 6)
exitButton.grid(row=3,column=1)

win.protocol("WM_DELET_WINDOW", close)
win.mainloop()#loop forever