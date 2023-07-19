import pyautogui as p
from tkinter import *
import threading
import sys

def exit():
    sys.exit()

def ricerca():
    global pisello

    pisello=True

    lista = ["szaboEarn.png","playstore.png"]

    while pisello is True:
        for element in lista:
            try:
                x, y, z, l =p.locateOnScreen(element, confidence=0.9)

                if element != "playstore.png":
                    p.moveTo(x+5,y+5, duration=.1)
                    p.leftClick()
                else:
                   
                    x2, y2, z, l =p.locateOnScreen("playstoreSkip.png", confidence=0.9)
                    p.moveTo(x2+5,y2+5, duration=.1)
                    p.leftClick()

            except:
                label['text'] =f'''
                not found: {element}
                '''

def stop():
    global pisello
    pisello=False

def start_thread():
    thread = threading.Thread(target=ricerca)
    thread.start()


root = Tk()
root.title('TuaMadre')
root.geometry('250x250')

button = Button(root, text='start', command=start_thread)
button.pack()

button1 = Button(root, text='stop', command=stop)
button1.pack()

button2 = Button(root, text='exit', command=exit)
button2.pack()

label = Label(root, bg='white', fg='black', text='')
label.pack(fill="both", expand="yes")

root.mainloop()