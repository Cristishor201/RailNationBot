import pyautogui, time, os
import cv2
import numpy as np
from datetime import datetime as date

os.chdir('.//img')

refresh = [317, 207]
buttons = [[168, 275], [244, 275], [322, 275]] # [x,y] default
regions = [[133, 260, 70, 30], [209, 260, 70, 30], [287, 260, 70, 30]] # [x, y, width, height]
center_region = [960, 540, 200, 200]

watchYou = [1044, 788]
continueYou = [1006, 747]
skipVideo = [1419, 725]
lotery = [1101, 311]
stop = False # initialy -----------------------------------------------------

closeVideo = [1440, 325]
closeButton = [959, 614]
restartVideo = [879, 712]

def if_widget_present(): # verify at init if the widget it's on home screen
    pyautogui.press('esc')
    pyautogui.press('esc') # quit to the main menu if necessary

    if image_on_screen('association_1.JPG') == True:
        return True
    else:
        return False

def if_widget_position(): # verify position of widget on the screen
    if image_on_screen('association_2.JPG') == True:
        return True
    else:
        return False

def update_widget(word): # update setup widget (if required)
    if word == 'widget':
        print("update widget")
    elif word == 'position':
        print("update position of widget")
    ################################################ mai trebuie aici
    return None

def if_green_btn():
    ################################################ mai trebuie aici
    return True

def image_in_region(image, region=(0, 0, 1, 1), precision=0.8): # region screen option
    x, y, width, height = region
    img = pyautogui.screenshot(region=(x, y, width, height))
                          
    #img.save('testarea.png') #usefull for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(img)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return False # image is not founded
    else:
        print('image in region')
        return True  # image match

def image_on_screen(image, precision=0.8): # full screen option
    img = pyautogui.screenshot()

    #img.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(img)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return False # image is not founded
    else:
        print('image on screen')
        return True  # image match

def bonus(x, y): # [x, y] of the button
    pyautogui.click(x, y, interval=1)

    if (image_on_screen('bonus_cant.jpg') == True)or(image_on_screen('Bonus_colected_already.jpg') == True):
        #exeed limit account & bonus collected already
        pyautogui.click(closeButton[0], closeButton[1])
    if image_on_screen('lotery_free.jpg') == True: # free ticket from others
        pyautogui.click(lotery[0], lotery[1], interval=3)
        time.sleep(3)
        
    pyautogui.click(1160, 399, interval=0.3) # close reduction lotery tickets

def video(x, y): # [x, y] of the button
    ok = False # skiping video
    pyautogui.click(x, y, interval=1)
    time.sleep(8.5)
    if image_on_screen('skip.jpg') == True:  # skip video if it can
        pyautogui.click(skipVideo[0], skipVideo[1])
        ok = True
        time.sleep(3)
    #if is no video / blank screen
    if (image_on_screen('video_not_load.jpg') == True) or (image_on_screen('no_video.jpg', 0.9) == True):
        reloadVideo() # need of reload
        time.sleep(8.5)

        if image_on_screen('skip.jpg') == True: # skip the video if it can
            pyautogui.click(skipVideo[0], skipVideo[1])
            time.sleep(3)
        if (image_on_screen('video_not_load.jpg') == True) or (image_on_screen('no_video.jpg', 0.9) == True):
            reloadVideo()
            
        time.sleep(31)
    else:
        if ok == False: # if already I skip it
            time.sleep(31)
    
    if image_on_screen('watch_bonus_you.jpg') == True:
        pyautogui.click(watchYou[0], watchYou[1], interval=1)
        time.sleep(8.5)
        if image_on_screen('skip.jpg') == True: # skip the video if it can
            pyautogui.click(skipVideo[0], skipVideo[1])
            time.sleep(3)
        else:
            time.sleep(26.5)
     
    if image_on_screen('Continue_last.jpg') == True:
        pyautogui.click(continueYou[0], continueYou[1], interval=1)
        time.sleep(3)
    if image_on_screen('lotery_free.jpg') == True:
        pyautogui.click(lotery[0], lotery[1], interval=3)
        time.sleep(3)
        
    pyautogui.click(1160, 399, interval=0.3) # close reduction lotery tickets


def reloadVideo():
    pyautogui.click(closeVideo[0], closeVideo[1])
    time.sleep(4)
    pyautogui.click(restartVideo[0], restartVideo[1])

#try:
    #while True: # infinite loop
        #collect
#except FailSafeException:
    #print("Program stoped by user.")

if __name__ == "__main__":
    print("Program started at " + date.now().strftime("%H:%M"))

    if if_widget_present() == True:
        # open it
        print("open the widget...")
    else:
        update_widget(widget) # update widget

    if if_widget_position() == True:
        # do nothing. it's ok
        print("it's ok")
    else:
        update_widget(position) # update the position of it
        
    try:
        #refresh btn
        pyautogui.click(refresh[0], refresh[1])
        time.sleep(2)
        #while True: # pasive loop
        
        while if_green_btn() == True: # while is a green button:
            for i in range(3):
        #       if btn(1) == $_img:
        #           bonus(x, y) # button
        #           time.sleep(1.5)
        #       elif btn(2) == $_img:
        #           bonus(x, y) # button
        #           time.sleep(1.5)
        #       elif btn(3) == *_img:
                #if image_in_region('image_prestige.jpg', regions[2]) == True:
                #    print("True")
        #           bonus(x, y) # button
        #           time.sleep(1.5)
                if image_in_region('video_present.jpg', regions[i]) == True: # if is video
                    video(buttons[i][0], buttons[i][1]) # video
                else:
                    bonus(buttons[i][0], buttons[i][1])
                    time.sleep(2)
            pyautogui.click(refresh[0], refresh[1]) # refresh btn
            time.sleep(2)
        #       else: continue
        #if ctrl + esc -> break
        #pasive loop - print the time when is passive, every 15 min

        
    except FailSafeException:
        print("Program stoped by user.")
    except KeyboardInterrupt:
        print("Program stoped by user.")
    finally:
        print("Program ended at " + date.now().strftime("%H:%M"))

    

