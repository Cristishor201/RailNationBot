import pyautogui, time, os
import cv2
import numpy as np
from datetime import datetime as date
import logging #=============================== testing
from settings import setup
import resources.env as env
from lang.lang import lang
from pynput import keyboard
import psutil

today =  date.now().strftime("_%d-%m-%Y_%H-%M")

if __name__ == "__main__":
    ratio = [1, 1]
    ok = 0
    print("Program started at ", today)

    Resolution, Language = setup()
    if Resolution is None:
        Resolution = [pyautogui.size().width, pyautogui.size().height]
        print("myResolution= [{}][{}]".format(Resolution))

    env.init(Resolution, Language)
    env.update()
    print(date.now().strftime("%H-%M"), " - CPU - ", psutil.cpu_percent(), "%")

    with keyboard.Listener(on_press=env._key_press) as listener:
        while True: # main loop
            env.refreshing()
            start = time.perf_counter()
            for i in range(3):
                # check for bonus first
                bonus = env.bonus()

                env.bonus_lotery()
                if env.f_stop():
                    break
                if bonus:
                    continue

                if env.video(i):
                    env.button(i)
                    while True:
                        if env.f_stop():
                            break
                        time.sleep(2)
                        if env.video_active() == False:
                            break
                    time.sleep(1.5)
                    env.watch_bonus_you()
                    while True:
                        if env.f_stop():
                            break
                        time.sleep(2)
                        if env.video_active() == False:
                            break
                    env.continue_you()
                    env.video_lotery()
                    
            finish = time.perf_counter()
            if env.f_stop():
                break
            if round(finish-start, 2) < 2: # wait 15min
                print(date.now().strftime("%H-%M"),': waiting 15 min for bonus or video...')
                time.sleep(15*60)
                pyautogui.move(50, 0, duration=2) # escape from stand-by screen

        #while end
        listener.join()
    message = pyautogui.confirm(text="The program finished succesefully.", title='Finished', buttons=['OK', 'Cancel'])
