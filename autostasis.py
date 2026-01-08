import pyautogui
import time
import read_health

threshold = 8

while True:
    current_health = int(read_health.read())
    print(current_health)
    if current_health < threshold:
        print("pulled")
        pyautogui.keyDown('1')
        pyautogui.keyUp('1')
        pyautogui.rightClick()
        time.sleep(30)
    time.sleep(0.01)