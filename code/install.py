import subprocess, sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencv-python'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pynput'])
