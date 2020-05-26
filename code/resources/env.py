import pyautogui
import sys, os
import lang.lang as lang
import numpy as np
import cv2, time
from pynput import keyboard

screen = [1920, 1080]
ratio = [1, 1]
refresh = [375, 203]
buttons = [[170, 275], [270, 275], [370, 275]] # [x,y] default
regions = [[126, 261, 92, 25], [224, 261, 92, 25], [322, 261, 92, 25]] # [x, y, width, height]
center_region = [960, 540, 200, 200]

watchYou = [1050, 777]
continueYou = [1005, 740]
skipVideo = [1330, 710] # lucky guess
lotery = [1090, 330]

closeVideo = [1340, 380]
xButton = [1148, 412] # buy lottery ticket
closeButton = [960, 610] # limit exceed
restartVideo = [880, 707]
cancelVideo = [1033, 707]
errors = [885, 650] # sudenly error

_if_widget = [None, None, None] # present, open, position
name_images = [] # assoc_1, assoc_2, continue_last, bonus_cant_already, lotery_free, lotery_bonus, bonus_you, video_present, secure_bonus, skip_buy_ticket, bonus_money, bonus_prestige, sudenly_error
_stop = False

path = '' # for images

def init(resolution, Language='en'):
    res = [pyautogui.size().width, pyautogui.size().height]
    global ratio, screen, path, name_images
    if res != resolution:
        print("Be sincere and enter your real resolution in settings:", res)
        sys.exit() # stop the program
    ratio = [resolution[0]/screen[0], resolution[1]/screen[1]]
    screen = resolution
    path = "lang//" + Language + "//img"
    if ratio == [1,1]:
        print("Unchanged resolution")

    name_images = lang.lang(Language)
    os.chdir(os.path.abspath(path))

    if image_on_screen(name_images[0]): # assoc_1
        _if_widget[0] = True
        if image_on_screen(name_images[1]): # assoc_2
            _if_widget[1] = True
            x, y = image_on_screen(name_images[1], 0.8, True) # assoc_2 | position
            #print("[x,y]",[x,y])
            if [x,y] == [114, 195]:
                _if_widget[2] = True
                print("Widget is in the position")
            else:
                _if_widget[2] = False
        else:
            _if_widget[1] = False
            _if_widget[2] = False
    else:
        _if_widget[0] = False
        _if_widget[1] = False
        _if_widget[2] = False

def image_on_screen(img_str,precision=0.8, position=False ): # statica
    img = pyautogui.screenshot()

    img_rgb = np.array(img)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(img_str, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    __, max_val, __, max_loc = cv2.minMaxLoc(res)
    if position == True: # if I want to take the position of image
        return max_loc
    if max_val < precision:
        return False # image is not founded
    else:
        return True # image match

def image_in_region(image, region, precision=0.8): # region screen option
    x, y, width, height = region
    img = pyautogui.screenshot(region=(x, y, width, height))

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

def update_ratio(val_list):
    global ratio
    return [int(val_list[0]*ratio[0]), int(val_list[1]*ratio[1])]

def update():
    global ratio, name_images
    py = [[74, 998],[74, 848],[447, 377],[92, 25]]
    if ratio != [1, 1]:
        ###### closeButton ??? - #exeed limit account & bonus collected already
        center_region[0:] = update_ratio(center_region[:2]) + update_ratio(center_region[2:])
        watchYou[0:] = update_ratio(watchYou)
        continueYou[0:] = update_ratio(continueYou)
        skipVideo[0:] = update_ratio(skipVideo)
        lotery[0:] = update_ratio(lotery)
        closeVideo[0:] = update_ratio(closeVideo)
        restartVideo[0:] = update_ratio(restartVideo)
        cancelVideo[0:] = update_ratio(cancelVideo)
        xButton[0:] = update_ratio(xButton)
        closeButton[0:] = update_ratio(closeButton)
        errors[0:] = update_ratio(errors)

        for i in range(len(py)):
            py[i][0] = int(py[i][0] * ratio[0])
            py[i][1] = int(py[i][1] * ratio[1])

    if _if_widget[0] == False: # present
        pyautogui.click(py[0]) # plus add widget button
        time.sleep(1)
        pyautogui.click(py[1]) # click association
        time.sleep(3)
        pyautogui.moveTo(py[2]) # corner right-down widget
        pyautogui.drag(0,10,1)
    elif _if_widget[1] == False: # open
        pyautogui.click(py[0])
        time.sleep(3)

    if _if_widget[2] == False or ratio != [1, 1]: # position or ratio
        x, y = image_on_screen(name_images[1], 0.8, True)
        refresh[0] = int((x + 261)* ratio[0]) # update refresh_x
        refresh[1] = int((y + 8)* ratio[1]) # update refresh_y
        x1, y1 = [int((x+56)*ratio[0]), int((y+80)*ratio[1])]
        x2, y2 = [int((x+12)*ratio[0]), int((y+66)*ratio[1])]
        for i in range(3):
            buttons[i] = [x1, y1] ; x1= int((x1 +100)*ratio[0])
            regions[i] = [x2, y2, py[3][0], py[3][1]] ; x2 = int((x2 + py[3][0] + 6)*ratio[0])

        print("refresh", refresh)
        print("regions:",regions)
        print("buttons", buttons)

def __region_capture(region, name='testarea'):
    img = pyautogui.screenshot(region=region)
    img.save(name + '.jpg')

def button(item):
    pyautogui.click(buttons[item])
    time.sleep(2)

def refreshing():
    pyautogui.click(refresh)
    time.sleep(2)

def watch_bonus_you():
    pyautogui.click(watchYou)
    time.sleep(2)

def region(item):
    return regions[item]

def video_active():
    if image_on_screen(name_images[8]):
        return True
    else:
        return False

def continue_you():
    if image_on_screen(name_images[2]) == True:
        pyautogui.click(continueYou)
        time.sleep(1)
    elif image_on_screen(name_images[9]) == True: # don't buy ticket
        pyautogui.click(xButton)
        time.sleep(1)

def video_lotery():
    if image_on_screen(name_images[4]) == True: # ticket from video watched
        pyautogui.click(xButton)
        time.sleep(1)

def bonus_lotery():
    if image_on_screen(name_images[5]) == True: # ticket won
        pyautogui.click(lotery)
        time.sleep(1)

def bonus_cant():
    if image_on_screen(name_images[3]) == True: #bonus can't OR bonus collected already
        pyautogui.click(closeButton)
        time.sleep(0.5)
        return True
    return False

def bonus():
    if image_in_region(name_images[10], regions[0]): # take bonus 1 (money)
        pyautogui.click(buttons[0])
        time.sleep(1)
        if bonus_cant():
            print("can't collect bonus")
            time.sleep(1) # for skiping standbye
        else:
            return True
    if image_in_region(name_images[10], regions[1]): # take bonus 2 (money)
        pyautogui.click(buttons[1])
        time.sleep(1)
        if bonus_cant():
            print("can't collect bonus")
            time.sleep(1) # for skiping standbye
        else:
            return True
    if image_in_region(name_images[11], regions[2]): # take bonus 3 (prestige)
        pyautogui.click(buttons[2])
        time.sleep(1)
        if bonus_cant():
            print("prestige collected already")
            time.sleep(1) # for skiping standbye
        else:
            return True
    return False

def video(item):
    if image_in_region(name_images[7], regions[item]):
        return True
    else:
        return False

def f_stop():
    return _stop

def _key_press(key):
    global _stop
    if key == keyboard.Key.esc:
        _stop = True
        return False

def errors():
    if image_on_screen(name_images[12]):
        pyautogui.click(errors)
        time.sleep(1)
