import pyautogui, time, os
import cv2
import numpy as np

os.chdir('C://Users//Cristian//Documents//GitHub//RailNationBot//code//img') #change here with your path

stationBonus = [[1147, 722], [1503, 653], [1728, 489]] # [x,y]
stationVideo = [[1141, 663], [1492, 589], [1723, 433]]

watchYou = [1044, 788]
continueYou = [1006, 747]
theNext = [1009, 934]
theBack = [907, 933]
lotery = [1101, 311]

closeVideo = [1440, 325]
restartVideo = [879, 712]

def soundOff():
    pyautogui.moveTo(1780, 1051, duration=1)
    pyautogui.click()
    pyautogui.moveTo(1790, 907, duration=0.7)
    pyautogui.click()

def imagesearch(image, precision=0.8):
    im = pyautogui.screenshot()
    #im.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1,-1]
    return max_loc

def appearIMG(file):
    pos = imagesearch(file)
    if pos[0] != -1:
        return True
    else:
        return False

def appearNext(file):
    pos = imagesearch(file)
    if pos[0] != -1:
        return True
    else:
        return False

def station(): # colect all rewards from one station
    time.sleep(2)
    for i in range(3):
        pyautogui.click(stationBonus[i][0], stationBonus[i][1], interval=1)
        
        if (appearIMG('lotery_free.jpg') == True): # free ticket from others
            pyautogui.click(lotery[0], lotery[1], interval=3)
            time.sleep(3)
        
        pyautogui.click(1160, 399, interval=0.3) # close reduction lotery tickets

def Bonus():
    time.sleep(2)
    for j in range(3):
        pyautogui.click(stationVideo[j][0], stationVideo[j][1], interval=1)
        time.sleep(35)

        # search for image
        if appearIMG('video_not_load.jpg') == True: #if video doesn't starting
            reloadVideo()
            time.sleep(35)
        if appearIMG('watch_bonus_you.jpg') == True:
            pyautogui.click(watchYou[0], watchYou[1], interval=1)
            time.sleep(35)
        if appearIMG('Continue_last.jpg') == True:
            pyautogui.click(continueYou[0], continueYou[1], interval=1)
            time.sleep(3)
        if (appearIMG('lotery_free.jpg') == True):
            pyautogui.click(lotery[0], lotery[1], interval=3)
            time.sleep(3)
        
        pyautogui.click(1160, 399, interval=0.3) # close reduction lotery tickets

def reloadVideo():
    pyautogui.click(closeVideo[0], closeVideo[1])
    time.sleep(4)
    pyautogui.click(restartVideo[0], restartVideo[1])
    time.sleep(4)

soundOff() # close sound
'''
#### Station 1 time (first)
station() # for me at the begining
pyautogui.moveTo(theNext[0], theNext[1], duration=1)
pyautogui.click()

while(appearIMG('close_mode_while.jpg') == True): # while I don't reach my station
    station()
    pyautogui.moveTo(theNext[0], theNext[1], duration=1)
    pyautogui.click()
    time.sleep(3)
    
    if(appearIMG('close_mode_while.jpg') == False):
        break
'''
#### Watch video 1 time (first)
Bonus() # for me at the begining
pyautogui.moveTo(theNext[0], theNext[1], duration=1)
pyautogui.click()

while(appearIMG('close_mode_while.jpg') == True): # while I don't reach my station
    Bonus()
    pyautogui.moveTo(theNext[0], theNext[1], duration=1)
    pyautogui.click()
    time.sleep(3)
    
    if(appearIMG('close_mode_while.jpg') == False):
        break

#### Station 2 times (second)
station() # for me at the begining
pyautogui.moveTo(theNext[0], theNext[1], duration=1)
pyautogui.click()

while(appearNext('close_mode_while.jpg') == True): # while I don't reach my station
    station()
    pyautogui.moveTo(theNext[0], theNext[1], duration=1)
    pyautogui.click()
    time.sleep(3)
    
    if(appearIMG('close_mode_while.jpg') == False):
        break

#### Watch video 2 times (second)
Bonus() # for me at the begining
pyautogui.moveTo(theNext[0], theNext[1], duration=1)
pyautogui.click()

while(appearIMG('close_mode_while.jpg') == True): # while I don't reach my station
    Bonus()
    pyautogui.moveTo(theNext[0], theNext[1], duration=1)
    pyautogui.click()
    time.sleep(3)
    
    if(appearIMG('close_mode_while.jpg') == False):
        break

soundOff() # turn on the sound
print("All bonuses has been collected successfully !")
