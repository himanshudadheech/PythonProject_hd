import random
import tkinter
from typing import Sized

#for open
import schedule
import time
import datetime
import webbrowser
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
#end

#metting start

url = input('enter meeting url : ')
timee = input('enter time hh:mm :')

def open_link(url):
    webbrowser.open(url)

def meeting():
   #url = input('enter url')
  # timee = input('enter time : hh:mm')
   open_link(url)
  
schedule.every().tuesday.at(timee).do(meeting)
#schedule.every().friday.at("8:36").do(meeting)

while 1:
    schedule.run_pending()
    time.sleep(1)
#end





main_window = tkinter.Tk()
main_window.title("join")
main_window.geometry('500x300') #window Sized
padd=50
chk1=tkinter.IntVar()
chk2=tkinter.IntVar()
chk3=tkinter.IntVar()



main_window['padx'] = padd #padding
title_text = tkinter.Label(text='join')
title_text.grid(row=0,column=0)

display_result=tkinter.Entry()
display_result.grid(row=1,column=0)

chkone = tkinter.Checkbutton(text='6 character',onvalue=6,offvalue=0,variable=chk1)
chkone.grid(row=2,column=0)

chktwo = tkinter.Checkbutton(text='10 character',onvalue=10,offvalue=0,variable=chk2)
chktwo.grid(row=3,column=0)

chkthree = tkinter.Checkbutton(text='12 character',onvalue=12,offvalue=0,variable=chk3)
chkthree.grid(row=4,column=0)

join=tkinter.Button(text='join', command=meeting)
join.grid(row=5,column=0)

main_window.mainloop()
