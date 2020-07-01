
import pyautogui    #importing pyautogui. It is library in python to make the computer to press the keys itself
#every key has a reference to use.
#Key reference link  <href="https://pyautogui.readthedocs.io/en/latest/keyboard.html">

from PIL import ImageGrab,Image         #PIL library for taking a screenshot of the screen and to identify
                                        #cactus and bird coming in opposite direction
import time
from numpy import asarray
def hit(key):       #defining hit function whenever a cactus or bird found
    pyautogui.keyDown(key)      #holds the key
    return
def iscolloid(data):        #
    #for cactus
    for i in range(488,495):        #these loops for finding the cactus on the screen whenerever the data of
                                    #the loop colloid with the data of cactus its calls "hit " function
        for j in range(235,265):
            if data[i,j]<100:
                hit("up")
                return
            #for bird
    for i in range(488,495):    #similarly for bird
        for j in range(180,235):
            if data[i,j]<100:
                hit("down")
                return
    return False

if __name__=="__main__":
    print("the dino game is about to start in 3 sec")
    time.sleep(3)       # starting game after 3sec because it take time to navigate from script activity to chrome
    hit("up")           #for starting game
    while True:
        image=ImageGrab.grab().convert('L')         #taking screenshot of the activity and converting the RGB into gray
        data=image.load()       #loading image
        iscolloid(data)         #calling iscolloid function to check whether colloid with cactus or bird
