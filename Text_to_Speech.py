# import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound
import os


# Initializing Window

root = Tk()
root.geometry('350x300')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('Text To Speech')


# Heading

Label(root, text = 'Text To Speech' , font='Arabic_Transparent 20 bold' , bg = 'white smoke').pack()
Label(root, text = 'Vineeth Sai' , font ='Arabic_Transparent 15 bold', bg = 'Yellow').pack(side = BOTTOM)


# Label

Label(root, text = 'Enter Text: ', font = 'Arabic_Transparent 15 bold', bg = 'white smoke').place(x=20,y=60)


# Text Variable

Msg = StringVar()


# Enter Text

entry_field = Entry(root, textvariable = Msg, width = '50')
entry_field.place(x = 20, height = 30, y = 100)


# Function Definition

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('vs.mp3')
    playsound('vs.mp3')
    os.remove('vs.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set('')


# Button

Button(root, text = '►' , font = 'Arabic_Transparent 15 bold', command = Text_to_speech, width = 4, bg = 'white').place(x=25 , y=140)
Button(root,text = '❌', font = 'Arabic_Transparent 15 bold' , command = Exit, bg = 'OrangeRed').place(x=100 , y=140)
Button(root, text = 'Reset', font = 'Arabic_Transparent 15 bold' , command = Reset, bg = 'white').place(x=175 , y =140)

root.mainloop()

