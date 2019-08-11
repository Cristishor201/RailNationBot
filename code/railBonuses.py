import pyautogui, time, os
import cv2
import numpy as np
from datetime import datetime as date
import logging #=============================== testing
today =  date.now().strftime("_%d-%M-%Y_%H-%M")
logging.basicConfig(filename='errorsLogs'+ today + '.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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

def if_widget_open(): # verify if the widget it's open
    if image_on_screen('association_2.JPG') == True:
        return True
    else:
        return False

def if_widget_position(): # verify position of widget on the screen
    x, y = image_on_screen('association_2.JPG', 0.8, True)
    if (x == 122) and (y == 200): # default position
        return True
    else:
        return False

def update_widget(word): # update setup widget (if required)
    if word == 'widget1':
        pyautogui.click(80, 998)
        time.sleep(1)
        pyautogui.click(80, 836)
        time.sleep(3)
    elif word == 'widget2':
        pyautogui.click(80, 998) # widget is minified
        time.sleep(3)
    elif word == 'position':
        # default - 122 - 200
        x, y = image_on_screen('association_2.JPG', 0.8, True)
        refresh[0] = x + 195 # update refresh_x
        refresh[1] = y + 7 # update refresh_y
        x1 = x+195 ; y1 = y + 7

        buttons[0][0] = x1 - 150 # button_1_x
        buttons[0][1] = y1 + 65  # button_1_y
        x1 -= 150 ; y1 += 65
        buttons[1][0] = x1 + 78  # button_2_x
        buttons[1][1] = y1       # button_2_y
        x1 += 75
        buttons[2][0] = x1 + 78  # button_3_x
        buttons[2][1] = y1       # button_3_y
        
        regions[0] = [x+11, y+60, 70, 30] # first region
        x += 11 ; y +=60
        regions[1] = [x+76, y, 70, 30] # second region
        x += 76
        regions[2] = [x+78, y, 70, 30] # second region
        print("\nupdate manually if you want for faster reload:\nrefresh=" + str(refresh))
        print("buttons= [" + str(buttons[0]) + "," + str(buttons[1]) + "," + str(buttons[2]) + "]")
        print("regions= [" + str(regions[0]) + "," + str(regions[1]) + "," + str(regions[2]) + "]\n")
        
    else:
        return False

def if_green_btn():
    ################################################ mai trebuie aici
    return True

def image_in_region(image, region, precision=0.8): # region screen option
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
        return True  # image match

def color_in_region(region, color_list=([40, 90, 40],[56, 128, 60]), precision=0.8): # if is color in region image
    x, y, width, height = region
    img = pyautogui.screenshot(region=(x, y, width, height))
    lower, upper = color_list

    lower = np.array(lower, dtype="uint8") # np array
    upper = np.array(upper, dtype="uint8")
    img = np.array(img, dtype="uint8")
    
    mask = cv2.inRange(img, lower, upper)
    print(mask)
    cv2.imshow('mask', mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return None

def image_on_screen(image, precision=0.8, link=False): # full screen option
    img = pyautogui.screenshot()

    #img.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(img)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if link == True: # if I want to take the position of image
        return max_loc
    if max_val < precision:
        return False # image is not founded
    else:
        return True # image match

def bonus(x, y): # [x, y] of the button
    pyautogui.click(x, y, interval=1)
    
    #============================================== begining of testing
    if (image_on_screen('video_not_load.jpg', 0.9) == True): # if video don't load after waiting for it
        logging.critical("--- D1 - video_not_load")

        if (image_on_screen('video_not_load.jpg', 0.9) == True): # if video don't load after waiting for it
            logging.critical("--- D2 - video_not_load")
            reloadVideo() # need of reload
            time.sleep(31)
        
    #============================================== end of testing
    
    if (image_on_screen('bonus_cant.jpg') == True)or(image_on_screen('Bonus_colected_already.jpg') == True):
        #exeed limit account & bonus collected already
        pyautogui.click(closeButton)
    if image_on_screen('lotery_free.jpg') == True: # free ticket from others
        pyautogui.click(lotery)
        time.sleep(3)
        
    pyautogui.click(1160, 399, interval=0.3) # close reduction lotery tickets

def video(x, y): # [x, y] of the button
    ok = False # skiping video
    pyautogui.click(x, y, interval=1)
    time.sleep(8.5)
    if image_on_screen('skip.jpg') == True:  # skip video if it can
        pyautogui.click(skipVideo)
        ok = True
        time.sleep(3)
    #if is no video / blank screen
    '''
    if (image_on_screen('video_not_load.jpg', 0.9) == True) or (image_on_screen('no_video.jpg', 0.9) == True):
        print("--- A1 - video_not_load / no_video")
        reloadVideo() # need of reload
        time.sleep(8.5)

        if image_on_screen('skip.jpg') == True: # skip the video if it can
            pyautogui.click(skipVideo)
            time.sleep(3)
        if (image_on_screen('video_not_load.jpg') == True) or (image_on_screen('no_video.jpg', 0.92) == True):
            print("--- A2 - video_not_load / no_video")
            reloadVideo()
            
        time.sleep(31)
    else:
        if ok == False: # if already I skip it
            time.sleep(31)
            
    if (image_on_screen('video_not_load.jpg', 0.9) == True): # if video don't load after waiting for it
        print("--- A3 - video_not_load")
        reloadVideo() # need of reload
        time.sleep(31)
    '''
    #===================================== begining of testing
    if (image_on_screen('video_not_load.jpg', 0.9) == True):
        logging.debug("--- A1 - video_not_load")
        reloadVideo() # need of reload
        time.sleep(8.5)

        if image_on_screen('skip.jpg') == True: # skip the video if it can
            pyautogui.click(skipVideo)
            time.sleep(3)
        if (image_on_screen('video_not_load.jpg') == True): 
            logging.debug("--- A2 - video_not_load")
            reloadVideo()
            
        time.sleep(31)
    elif (image_on_screen('no_video.jpg', 0.9) == True):
        logging.debug("--- A1 - no_video")
        reloadVideo() # need of reload
        time.sleep(8.5)

        if (image_on_screen('no_video.jpg', 0.92) == True):
            logging.debug("--- A2 - no_video")
            reloadVideo()

        time.sleep(31)
    else:
        if ok == False: # if already I skip it
            time.sleep(31)

    if (image_on_screen('video_not_load.jpg', 0.9) == True): # if video don't load after waiting for it
        logging.info("--- A3 - video_not_load")

    if (image_on_screen('no_video.jpg', 0.92) == True):
            logging.info("--- A2 - no_video")
    #============================================ end testing
    
    if image_on_screen('watch_bonus_you.jpg') == True:
        pyautogui.click(watchYou[0], watchYou[1], interval=1)
        time.sleep(8.5)
        if image_on_screen('skip.jpg') == True: # skip the video if it can
            pyautogui.click(skipVideo)
            time.sleep(3)
        else:
            time.sleep(26.5)
    #============================================ begining of testing
    if (image_on_screen('video_not_load.jpg', 0.9) == True): # if video don't load before second
        logging.warning("--- B1 - video_not_load")
        reloadVideo() # need of reload
        time.sleep(8.5)

        if (image_on_screen('video_not_load.jpg', 0.9) == True): # if video don't load after waiting for it
            logging.warning("--- B2 - video_not_load")
            reloadVideo() # need of reload
        time.sleep(31)
    #============================================= end of testing
    
    if image_on_screen('Continue_last.jpg') == True:
        pyautogui.click(continueYou)
        time.sleep(3)
    if image_on_screen('lotery_free.jpg') == True:
        pyautogui.click(lotery)
        time.sleep(5)
        
    pyautogui.click(1160, 399, interval=0.3) # close reduction lotery tickets


def reloadVideo():
    pyautogui.click(closeVideo)
    time.sleep(4)
    pyautogui.click(restartVideo)

if __name__ == "__main__":
    print("Program started at " + date.now().strftime("%H:%M"))

    if if_widget_present() == False:
        update_widget('widget1') # install the widget
    
    if if_widget_open() == False:
       update_widget('widget2') # open the widget
    
    if if_widget_position() == False:
        update_widget('position') # update the position
    
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
                    time.sleep(2)  #================================ testing
                if (image_on_screen('video_not_load.jpg', 0.9) == True): # if video don't load after waiting for it
                    logging.error("--- C1 - video_not_load")
            pyautogui.click(refresh[0], refresh[1]) # refresh btn
            time.sleep(2)
        #       else: continue
        #if ctrl + esc -> break
        #pasive loop - print the time when is passive, every 15 min

    except KeyboardInterrupt:
        print("Program stoped by user.")
    finally:
        print("Program ended at " + date.now().strftime("%H:%M"))
