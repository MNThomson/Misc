# Look Up: Reminders Every 20 Minutes

## Background

When working on a computer for extended amounts of time, it is suggested to follow the 20-20-20 rule (just go Google it). The idea is that every 20 minutes you look at something that is over 20 feet for 20 seconds. This is your friendly reminder

## Installation

Clone this repository into any folder and install the required dependencies:
	```
	$ pip3 install -r requirements.txt`
	```
Build your own executable through [Pyinstaller](https://pypi.org/project/pyinstaller) with the command:
	```
	$ pyinstaller --onefile --noconsole --clean --distpath . --icon=LookUp.ico LookUp.py
	```