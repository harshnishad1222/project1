
import pygame
from pygame import mixer
from tkinter import *
import os

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

root=Tk()
root.title("Music Player")

mixer.init()
songstatus=StringVar()
songstatus.set("Choosing")

#plalist-----------

playlist=Listbox(root,selectmode=SINGLE,bg="black",fg="White",font=("arial",15),width=40)
playlist.grid(columnspan=5)
os.chdir(r'D:\Songs\sobhit')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)


playbtn=Button(root,text="play",command=playsong)
playbtn.config(font=('arial,20'),bg="green",fg='white',padx=7,pady=7)
playbtn.grid(row=1,column=0)

playbtn=Button(root,text="Pause",command=pausesong)
playbtn.config(font=('arial,20'),bg="Dodgerblue2",fg='white',padx=7,pady=7)
playbtn.grid(row=1,column=1)

playbtn=Button(root,text="Stop",command=stopsong)
playbtn.config(font=('arial,20'),bg="red",fg='white',padx=7,pady=7)
playbtn.grid(row=1,column=2)

playbtn=Button(root,text="Resume",command=resumesong)
playbtn.config(font=('arial,20'),bg="Dodgerblue2",fg='white',padx=7,pady=7)
playbtn.grid(row=1,column=3)

mainloop()