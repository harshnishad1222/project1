# import all the important libraries----------------

import pygame
from pygame import mixer
from tkinter import *
import os

#functions for Buttons------------------------------

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

#Title----------------------------------------------
root=Tk()
#root.geometry("360x360")
root.title("DX Player")
#root.config(bg="gray")
root.iconbitmap(r'E:\Harsh python\project\c') 

mixer.init()
songstatus=StringVar()
songstatus.set("Choosing")

#plalist--------------------------------------------

playlist=Listbox(root,selectmode=SINGLE,bg="#1A1A1A",fg="white",font=("Consolas",15),width=40)
playlist.grid(columnspan=5, padx=7,pady=7)
os.chdir(r'D:\Songs\sobhit')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

#Buttons--------------------------------------------


playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('Consolas',15),bg="green",fg='white')
playbtn.grid(row=1,column=0,pady=7)

playbtn=Button(root,text="Pause",command=pausesong)
playbtn.config(font=('Consolas',15),bg="#EEB422",fg='white')
playbtn.grid(row=1,column=1)

playbtn=Button(root,text="Stop",command=stopsong)
playbtn.config(font=('Consolas',15),bg="red",fg='white')
playbtn.grid(row=1,column=2)

playbtn=Button(root,text="Resume",command=resumesong)
playbtn.config(font=('Consolas',15),bg="Dodgerblue2",fg='white')
playbtn.grid(row=1,column=3)

mainloop()