# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 00:44:44 2020

@author: DELL
"""

from tkinter import *

import os
import matplotlib
import gtts

import playsound
root=Tk()
root.title('Text to Speech')
root.geometry("350x300")
root.minsize(width=300,height=300)
root.configure(bg='ghost white')
Label(root,text="Text To Speech",fg='white smoke',bg='black').place()
Label(root,text="enter text",fg='white smoke',bg='black').place(x=20,y=60)
msg=StringVar()
Entryf=Entry(root,textvariable=msg,width='50')
Entryf.place(x=20,y=100)
def exit():
    root.destroy()
def reset():
    msg.set("")
Button(root, text = "PLAY" , font = 'arial 15 bold', width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold',command=exit, bg = 'OrangeRed1').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold',command=reset).place(x=175 , y =140)

def play():
    ms=Entryf.get()
    s=gTTS(text=ms)
    s.save("file.mp3")
    os.system("mpg 321 file.mp3")
    
root.mainloop()   


    
