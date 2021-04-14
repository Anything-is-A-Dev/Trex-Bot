import pyautogui
import time
import keyboard


# these are the width,height,x,y values of the place the bot patrols to find cactus, and the delay time
width = 120
height = 150
x = 450
y = 188
slep = 0.2

# This is a space function that preses space
def space():
    keyboard.press("space")
    time.sleep(0.1)
    keyboard.release("space")



# This is the main loop
while keyboard.is_pressed("q") == False:
   if pyautogui.locateOnScreen('cactus.png', region=(x, y, width , height), confidence= 0.8,) != None:
       time.sleep(slep) # adds a delay of 0.3 secs
       space()




   elif pyautogui.locateOnScreen('smol_cactus.png',region=(x, y, width , height), confidence=0.8) != None:
       time.sleep(slep)
       space()




   elif pyautogui.locateOnScreen('double_cactus.png',region=(x, y , width , height), confidence=0.8) != None:
       time.sleep(slep)
       space()



   elif pyautogui.locateOnScreen('triple.png', region=(x, y, width, height), confidence=0.8) != None:
       time.sleep(slep)# adds a delay of 0.3 secs
       space()







