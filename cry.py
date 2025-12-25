# thank god python is pee pee poo poo easy
# i said this and now my code deosnt even work im crine

import pyautogui
import time
import keyboard
import pydirectinput as pdi


death = "death.png", # im used to coding in javascript with easy objects shut up
emperor = "emperor.png",
fortune = "fortune.png",
lovers = "lovers.png",
magician = "magician.png"
retry = "retry.png"

stage = 0


def moveToPercent(x_percent, y_percent, duration=0): # ai wrote this lmao
    width, height = pyautogui.size()
    x = int(width * (x_percent / 100))
    y = int(height * (y_percent / 100))
    pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)

def region_percent(x_pct, y_pct, w_pct, h_pct): # this too im such a vibe coder
    screen_w, screen_h = pyautogui.size()
    return (
        int(screen_w * x_pct / 100),
        int(screen_h * y_pct / 100),
        int(screen_w * w_pct / 100),
        int(screen_h * h_pct / 100),
    )

def move_rel_percent(x_pct, y_pct, duration=0, ): # youll never guess
    w, h = pyautogui.size()
    x_offset = int(w * x_pct / 100)
    y_offset = int(h * y_pct / 100)
    pyautogui.moveRel(x_offset, y_offset, duration=duration, tween=pyautogui.easeInOutQuad)

def fixStupid():
    pdi.moveRel(1, 0)
    pdi.moveRel(-1, 0)

def clickMyCard(location):
    pyautogui.moveTo(pyautogui.center(location))
    move_rel_percent(0, 10, 1)

    fixStupid()
    pyautogui.click()

def mouseExitMenu():
    moveToPercent(50, 50, 0.1)
    fixStupid()
    pyautogui.click()


cardRegion = region_percent(
    x_pct=12,   # 12% from left
    y_pct=22,   # 22% from top
    w_pct=75,   # 75% of screen width
    h_pct=13    # 13% of screen height
)

retryRegion = region_percent(
    x_pct=35,
    y_pct=60,
    w_pct=20,
    h_pct=20
)

#left, top, w, h = cardRegion
#pyautogui.moveTo(left, top)
#pyautogui.dragTo(left + w, top + h, duration=1.5)
def initMacro():
    moveToPercent(54, 18, 0.2)
    fixStupid()
    pyautogui.click()

    moveToPercent(70, 48, 1.5)
    fixStupid()
    pyautogui.click()

    time.sleep(2)
    findMyCard(magician)

    time.sleep(.3)
    pdi.press("6")
    pdi.press("6")
    pdi.press("6")

    time.sleep(1.5)

    moveToPercent(78, 49)
    fixStupid()
    pyautogui.click()
    time.sleep(9)
    pdi.press("e")
    

def findMyCard(name):
    global stage

    if name == magician:
        try:
            location = pyautogui.locateOnScreen( # if this doesnt work i will cry
                    "magician.png",
                    region=cardRegion,
                    confidence=0.65
                )
            if location:
                clickMyCard(location)
                stage += 1
                
        except pyautogui.ImageNotFoundException:
            
            findMyCard(lovers)
    if name == lovers:
        try:
            location = pyautogui.locateOnScreen( # these are the worst coding practices ever
                    "lovers.png",
                    region=cardRegion,
                    confidence=0.65
                )
            if location:
                clickMyCard(location)
                stage += 1
                
        except pyautogui.ImageNotFoundException:
            
            findMyCard(death)
    if name == death:
        try:
            location = pyautogui.locateOnScreen( # these are the worst coding practices ever
                    "death.png",
                    region=cardRegion,
                    confidence=0.65
                )
            if location:
                clickMyCard(location)
                stage += 1
                
        except pyautogui.ImageNotFoundException:
            
            findMyCard(emperor)
    if name == emperor:
        try:
            location = pyautogui.locateOnScreen( # these are the worst coding practices ever
                    "emperor.png",
                    region=cardRegion,
                    confidence=0.65
                )
            if location:
                clickMyCard(location)
                stage += 1
                
        except pyautogui.ImageNotFoundException:
            
            findMyCard(fortune)
    if name == fortune:
        try:
            location = pyautogui.locateOnScreen( # these are the worst coding practices ever
                    "fortune.png",
                    region=cardRegion,
                    confidence=0.65
                )
            if location:
                clickMyCard(location)
                stage += 1
                
        except pyautogui.ImageNotFoundException:
            "good code practices"


def tryTryAgain(): # good naming conventions
    pyautogui.click()
    time.sleep(5)
    try:
        location = pyautogui.locateOnScreen( # these are the worst coding practices ever
                "retry.png",
                region=retryRegion,
                confidence=0.65
            )
        if location:

            pyautogui.moveTo(pyautogui.center(location))
            fixStupid()
            pyautogui.click()

            main()
    except:
        tryTryAgain()

    """
    try:
        while True:
            x, y = pyautogui.position()
            screen_w, screen_h = pyautogui.size()
            x_pct = (x / screen_w) * 100
            y_pct = (y / screen_h) * 100
            print(f"\r{ x_pct:.2f}% x, {y_pct:.2f}% y", end="")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopped")
    """

def main():
    global stage
    time.sleep(5)

    initMacro()

    time.sleep(12)

    findMyCard(magician)
    time.sleep(3.3)

    pdi.press("e")

    mouseExitMenu()

    time.sleep(.3)
    pdi.press("1")
    pdi.press("1")
    pdi.press("1")

    moveToPercent(27, 37) # ace placement1
    fixStupid()
    pyautogui.click()

    stage = 1

    while stage > 0:
        if keyboard.is_pressed('g'):  # hold G to quit
            print("Stopped by hotkey")
            break
        

        findMyCard(magician)

        time.sleep(.3)
        if (stage == 3):
            for i in range(10):
                pdi.press("e")
                time.sleep(.2)
            stage+=1
        if (stage == 5):
            pdi.press("e")
            pdi.press("e")
            pdi.press("e")
            mouseExitMenu()
            time.sleep(.3)

            pdi.press("4")
            pdi.press("4")
            pdi.press("4")

            moveToPercent(38, 56)
            fixStupid()
            pyautogui.click()
            pdi.press("e")
            pdi.press("e")
            pdi.press("e")
            pdi.press("e")
            pdi.press("e")
            pdi.press("e")

            time.sleep(17)

            mouseExitMenu()
            time.sleep(.3)

            pdi.press("3")
            pdi.press("3")
            pdi.press("3")

            time.sleep(.3)

            moveToPercent(50, 42)
            fixStupid()
            pyautogui.click()

            time.sleep(.3)
            mouseExitMenu()
            time.sleep(.3)

            stage+=1


        if (stage == 8):

            moveToPercent(38, 57)
            fixStupid()
            pyautogui.click()
            
            for i in range(10):
                pdi.press("e")
                time.sleep(.2)
            time.sleep(.5)

            mouseExitMenu()
            time.sleep(.3)

            pdi.press("3")
            pdi.press("3")
            pdi.press("3")

            time.sleep(.3)

            moveToPercent(43, 42)
            fixStupid()
            pyautogui.click()

            time.sleep(.3)
            mouseExitMenu()
            time.sleep(.3)

            pdi.press("3")
            pdi.press("3")
            pdi.press("3")

            time.sleep(.3)

            moveToPercent(42, 44)
            fixStupid()
            pyautogui.click()
            stage+=1
        if (stage == 10):
            time.sleep(.3)
            mouseExitMenu()
            time.sleep(.3)

            moveToPercent(38, 59)
            fixStupid()
            pyautogui.click()
            time.sleep(.3)

            pdi.press("e")
            pdi.press("e")
            pdi.press("e")
            stage+=1
        if (stage == 14):

            time.sleep(.3)
            mouseExitMenu()
            time.sleep(.3)

            pdi.press("2")
            pdi.press("2")
            pdi.press("2")

            moveToPercent(33, 59, .3)
            fixStupid()
            pyautogui.click()

            time.sleep(.3)
            for i in range(7):
                pdi.press("e")
                time.sleep(.2)

            stage+=1
        if (stage == 16):

            time.sleep(.3)
            mouseExitMenu()
            time.sleep(.3)

            pdi.press("5")
            pdi.press("5")
            pdi.press("5")

            moveToPercent(22, 59, .3)
            fixStupid()
            pyautogui.click()

            time.sleep(.3)
            pdi.press("e")
            pdi.press("e")
            stage+=1
        if stage == 19:
            break


        time.sleep(5)


    mouseExitMenu()
    moveToPercent(60, 50)
    fixStupid()
    tryTryAgain()
    
        

main()

"""
for img in images:
    location = pyautogui.locateOnScreen(
        img,
        region=cardRegion,
        confidence=0.8
    )
    if location:
        pyautogui.moveTo(pyautogui.center(location))
        move_rel_percent(0, 15)

        break
"""



