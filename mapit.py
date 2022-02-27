import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

# use cmd and run mapit.py and write there an adress or just copy some adress and run mapit.py
# if there is no adress then it will take yours
