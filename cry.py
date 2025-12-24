# thank god python is pee pee poo poo easy
# i said this and now my code deosnt even work im crine

import pyautogui
import time
import keyboard
import win32api
import win32con

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

cardRegion = region_percent(
    x_pct=12,   # 70% from left
    y_pct=22,   # 10% from top
    w_pct=75,   # 20% of screen width
    h_pct=13    # 15% of screen height
)


left, top, w, h = cardRegion
#pyautogui.moveTo(left, top)
#pyautogui.dragTo(left + w, top + h, duration=1.5)



death = "death.png", # im used to coding in javascript with easy objects shut up
emperor = "emperor.png",
fortune = "fortune.png",
lovers = "lovers.png",
magician = "magician.png"

time.sleep(2)

while True:
    if keyboard.is_pressed('g'):  # hold G to quit
        print("Stopped by hotkey")
        break
    try:
        location = pyautogui.locateOnScreen( # if this doesnt work i will cry
                magician,
                region=cardRegion,
                confidence=0.65
            )
        if location:
            pyautogui.moveTo(pyautogui.center(location))
            move_rel_percent(0, 12, 1)
            x, y = pyautogui.position()

            pyautogui.click()
            
    except pyautogui.ImageNotFoundException:
        print("magician card not found")
        time.sleep(2)


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
