import pyautogui

#cords
y = 1000
heart_positions = [608,622,642,651,674,685,706,715,737,747,770,780,801,810,834,842,866,873,899,906]

def read():
    current = 0
    for i in range(20):
        r,g,b = pyautogui.pixel(heart_positions[i], y)
        if r==40 and g==40 and b==40: # If pixel is grey
            break    
        current+=1  

    return current
