#Imports

import sys
import threading
import requests
import keyboard
import pyautogui
import time
from datetime import datetime
from keyboard import *
from pyautogui import *


#Ascii art to display when program is runned
print("""
  ______   _______     _       ____    ____  _____  ________  ____  ____  
.' ____ \ |_   __ \   / \     |_   \  /   _||_   _||_   __  ||_  _||_  _| 
| (___ \_|  | |__) | / _ \      |   \/   |    | |    | |_ \_|  \ \  / /   
 _.____`.   |  ___/ / ___ \     | |\  /| |    | |    |  _|      \ \/ /    
| \____) | _| |_  _/ /   \ \_  _| |_\/_| |_  _| |_  _| |_       _|  |_    
 \______.'|_____||____| |____||_____||_____||_____||_____|     |______|   
                                                                          


###################################
####### Spam people for fun #######
###################################

Created by Woox

github.com/WooxHimself

####################################




""")

#This captures the text user wants to spam

text = input("Enter text you want to spam: ")

#This captures how many messages user wants to send
messages = int (input("How many messages you want to spam? Maximum of 1000: "))


#If the message count is over 1000, the program will print error message and exit
if messages >=1000:
	print("The message count can't be bigger than 1000!")
	sys.exit()
#Prints this messages and pauses program for 10 seconds
print("You now have 10 seconds to select text field. Press CTRL+Z to cancel")
time.sleep(9.99999999999999)

#This is variable for current time
time = datetime.datetime.now()


#This creates loop for sending messages
for i in range(0,int(messages)):
  pyautogui.typewrite(text + '\n')

  #This prints time when message was sent
  print ("Message successfully sent! ",time.hour,":",time.minute,":",time.second, sep="")


#If there's error with sending messages, the program will exit itself and send error messagrs
else:
	print("Couldn't send the message! Check if you selected the text field correctly!")
	sys.exit(0)

#This prints message "Stopped!" when user press CTRL+C
def signal_handler(signal, frame):
    print('Stopped!')
    sys.exit(0)