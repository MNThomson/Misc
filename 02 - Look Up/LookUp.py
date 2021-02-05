from time import sleep
from notifypy import Notify
try:
	import pywintypes
except:
	pass

def notify(title, message):
	notification = Notify()
	notification.title = title
	notification.message = message
	notification.icon = "LookU.png"
	notification.send(block=False)

while True:
	notify("Look Up!", "This is your reminder about looking up for 20s")
	sleep(1200)