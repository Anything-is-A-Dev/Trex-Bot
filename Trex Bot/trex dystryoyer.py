import pyautogui
import time
import keyboard




# This is a space function that preses space
def space():
    keyboard.press("space")
    time.sleep(0.01)
    keyboard.release("space")

# these are the width,height,x,y values of the place the bot patrols to find cactus
width = 180
height = 150
x = 540
y = 188

# This is the main loop
while keyboard.is_pressed("q") == False:
   if pyautogui.locateOnScreen('cactus.png', region=(x, y, width , height), confidence= 0.8,) != None:
       time.sleep(0.3) # adds a delay of 0.3 secs
       space()



   elif pyautogui.locateOnScreen('smol_cactus.png',region=(x, y, width , height), confidence=0.8) != None:
       time.sleep(0.3)# adds a delay of 0.3 secs
       space()




   elif pyautogui.locateOnScreen('double_cactus.png',region=(x, y , width , height), confidence=0.8) != None:
       time.sleep(0.3)# adds a delay of 0.3 secs
       space()


   elif pyautogui.locateOnScreen('triple.png', region=(x, y, width, height), confidence=0.8) != None:
       time.sleep(0.2)# adds a delay of 0.3 secs
       space()


