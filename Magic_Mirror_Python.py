import tkinter as tk
from tkinter import *

startupscreen = tk.Tk()
startupscreen.title('Magic Mirror: Python Mod')
welcometext = tk.Label(startupscreen, font = ('caviar dreams', 40), bg='black', fg='white')
startupscreen.configure(background='black')
startupscreen.overrideredirect(True)
welcometext.config(text='Mirror: Vuoristo Mod')
welcometext.pack(side=LEFT, padx= 120, pady=80)
# Gets the requested values of the height and widht.
windowWidth = startupscreen.winfo_reqwidth()
windowHeight = startupscreen.winfo_reqheight()
# Gets both half the screen width/height and window width/height
positionRight = int(startupscreen.winfo_screenwidth()/3 - windowWidth/2)
positionDown = int(startupscreen.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
startupscreen.geometry("+{}+{}".format(positionRight, positionDown))
startupscreen.update()

import time
from newsapi import NewsApiClient
import os

decrypt = list()
global iteration
global timecount
global repull
global sleep
iteration = 0
timecount = 0
repull = 0
sleep = 0


while True:


    def tick(time1=''):
        time2 = time.strftime("%H")
        if time2 != time1:
            time1 = time2
            clock_frame.config(text=time2)
        clock_frame.after(200, tick)

    def tickk(time3=''):
        time4 = time.strftime(":%M:%S")
        if time4 != time3:
            time3 = time4
            clock_frame2.config(text=time4)
        clock_frame2.after(200, tickk)


    #This function waits for a certain amount of 'tocks' and then initiates 'newsheader' -function
    def tock():
        global timecount
        global repull
        global sleep
        global decrypt
        newstitle.after(200, tock)
        if timecount < 20:
            timecount +=1
        else:
            timecount = 0
            newsheader()
        if repull < 200:
            repull +=1
        else:
            repull = 0
            headlines = api.get_top_headlines(sources='bbc-news')
            payload = headlines
            decrypt = (payload['articles'])
            maxrange = len(decrypt)
        if sleep < 800:
            sleep+=1
        else:
            sleep = 0
            motiondetector()

    api = NewsApiClient(api_key='API_KEY')

    #This sequence decrypts the info feed for the script
    headlines = api.get_top_headlines(sources='bbc-news')
    #print(headlines)
    payload = headlines
    decrypt = (payload['articles'])
    maxrange = len(decrypt)

    #This function iterates over the news headlines. Iteration is the news number, 'itemlist' brings out only the title.
    def newsheader():
        global iteration
        global decrypt
        itemlist = decrypt[iteration]
        #print(itemlist['title'])
        newstitle.config(text=itemlist['title'])
        source.config(text=itemlist['author'])
        if iteration < 9:
            iteration +=1
        else:
            iteration = 0


    root = tk.Tk()
    root.title('Mirror')

    masterclock = tk.Label(root)
    masterclock.pack(anchor=NW, fill=X, padx=45)
    masterclock.configure(background='black')
    clock_frame = tk.Label(root, font = ('caviar dreams', 130), bg='black', fg='white')
    clock_frame.pack(in_=masterclock, side=LEFT)
    clock_frame2 = tk.Label(root, font = ('caviar dreams', 70), bg='black', fg='white')
    clock_frame2.pack(in_=masterclock, side=LEFT, anchor = N, ipady=15)
    newstitle = tk.Label(root, font = ('caviar dreams', 30), bg='black', fg='white')
    newstitle.pack(side=BOTTOM, anchor=W, fill=X)
    source = tk.Label(root, font = ('caviar dreams', 20), bg='black', fg='white')
    source.pack(side=BOTTOM, anchor=W, fill=X)

    newsheader()
    tick()
    tickk()
    tock()

    root.attributes("-fullscreen", True)
    root.configure(background='black')
    startupscreen.destroy()
    root.mainloop()
