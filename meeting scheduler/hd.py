from logging import root
import tkinter as tk 

from tkinter import simpledialog
from tkinter import*
import schedule
import time
import datetime

import webbrowser
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

import sys
 




root = Tk()




#root.withdraw()

root.geometry ("200x100")

# the input dialog
url = simpledialog.askstring(title="Link",
                                  prompt="link")


timee = simpledialog.askstring(title="Time",
                                  prompt="time:")


print("enter link is", url)
print("enter time is", timee)


def open_link(url):
    webbrowser.open(url)
    exit()
def meeting():
   #url = input('enter url')
  # timee = input('enter time : hh:mm')
   open_link(url)
  
schedule.every().day.at(timee).do(meeting)


while 1:
    schedule.run_pending()
    time.sleep(1)
    
#end

