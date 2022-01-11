import schedule
import time
import webbrowser
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

 

def open_link(link):
    webbrowser.open(link)

def meeting():
    open_link('import schedule')


def open_link(link):
    webbrowser.open(link)

def meeting():
   
    open_link("https://zoom.us/j/98861346537?pwd=K3cxWnJQT201c0MxV0RNdE9xOU9kUT09")

schedule.every().tuesday.at("09:03").do(meeting)
schedule.every().monday.at("22:24").do(meeting)


while 1:
    schedule.run_pending()
    time.sleep(1)



