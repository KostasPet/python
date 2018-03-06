import pyautogui
import commands
from random import randint
import os
import time

locations = {
'worldSwitch' : [-146,451,-55,480],
'world384' : [373,156,455,170],
'existingUser' : [242,262,374,291],
'login' : [82,292,214,322],
'afterLogin' : [121,262,340,342]
}

mainCords = None

def runGame():
    a = commands.getoutput('java -Xmx1024m -Djava.class.path=/home/pi/.jagex/runescape/bin/jagexappletviewer.jar -Dcom.jagex.config="http://oldschool.runescape.com/jav_config.ws" jagexappletviewer')
    print a
def runGameTest():
    a = commands.getoutput('java -cp -Djava.class.path=/home/pi/.jagex/runescape/bin/jagexappletviewer.jar -Dcom.jagex.config=http://oldschool.runescape.com/jav_config.ws -Xms512m -Xmx512m jagexappletviewer')
    print a

def screenSize():
    a = pyautogui.size()
    print a

def posision():
    a = pyautogui.position()
    print a
    return a

def random(arg1,arg2):
    return randint(arg1,arg2)

def screen():
    pyautogui.screenshot("screen.png")

def saveImgByLocation(Name,fileName):
    region = (
        locations[Name][0]+mainCords[0],
        locations[Name][1]+mainCords[1],
        locations[Name][2]+mainCords[0]-(locations[Name][0]+mainCords[0]),
        locations[Name][3]+mainCords[1]-(locations[Name][1]+mainCords[1])
        )
    im = pyautogui.screenshot(region=region)
    image = 'Storage/'+fileName+'.png'
    im.save(image)

def randomLocation(cords):
    return (random(cords[0],cords[2]),random(cords[1],cords[3]))
    
def locate(image):
    location = pyautogui.locateOnScreen(image)
    cords = (location[0],location[1],location[2]+location[0],location[3]+location[1])
    return cords

def move(location):
    pyautogui.moveTo(location[0],location[1],1,pyautogui.easeInBounce)
    pyautogui.click()

def showCords(Name):
    cords = (
    locations[Name][0] + mainCords[0],
    locations[Name][1] + mainCords[1],
    locations[Name][2] + mainCords[0],
    locations[Name][3] + mainCords[1]
             )
    a = randomLocation(cords)
    pyautogui.moveTo(a[0],a[1])
    
def makeImage(FileName):
    
    print "You have 5seconds"
    time.sleep(2)
    print "3"
    time.sleep(1)
    print "2"
    time.sleep(1)
    print "1"
    time.sleep(1)
    a = posision()
    print "First point!"
    
    print "You have 5seconds"
    time.sleep(2)
    print "3"
    time.sleep(1)
    print "2"
    time.sleep(1)
    print "1"
    time.sleep(1)
    b = posision()
    
    saveImgByCords (a[0],a[1],b[0],b[1],FileName)
    print "New image!"

def pushThisButton(Name):
    cords = (
    locations[Name][0] + mainCords[0],
    locations[Name][1] + mainCords[1],
    locations[Name][2] + mainCords[0],
    locations[Name][3] + mainCords[1],
             )
    move(randomLocation(cords))

def write(text):
    pyautogui.typewrite(text,interval=0.25)

def press(button):
    pyautogui.press(button)

def MainCords():
    
    print "Set Window (2secs)"
    time.sleep(2)
    print "Starting!"
    
    a = locate("Storage/R.png")
    
    global mainCords
    mainCords = (a[0],a[1])
    return (a[0],a[1])

def getCords():

    print "You have 5seconds"
    time.sleep(2)
    print "3"
    time.sleep(1)
    print "2"
    time.sleep(1)
    print "1"
    time.sleep(1)
    a = posision()
    print "First point!"
    
    print "You have 5seconds"
    time.sleep(2)
    print "3"
    time.sleep(1)
    print "2"
    time.sleep(1)
    print "1"
    time.sleep(1)
    b = posision()
    
    cords = (a[0]-mainCords[0],a[1]-mainCords[1],b[0]-mainCords[0],b[1]-mainCords[1])
    print "location",cords
    
def test():
    pushThisButton('worldSwitch')
    pushThisButton('world384')
    pushThisButton('existingUser')
    write('kostuxxas@gmail.com')
    press('tab')
    write('Pukiss123')
    pushThisButton('login')
    time.sleep(10)
    pushThisButton('afterLogin')
    
    

