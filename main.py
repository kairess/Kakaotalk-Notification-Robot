from dynamikontrol import Module
import pyautogui
import time

module = Module()

cx, cy = 2500, 100
w, h = 100, 600
r, g, b = 200, 110, 110
delay = 1

while True:
    img = pyautogui.screenshot(region=(cx, cy, w, h)) # (x, y, w, h)
    pixels = img.load()

    notify = False

    for x in range(w):
        for y in range(h):
            p = pixels[x, y]

            if p[0] > r and p[1] < g and p[2] < b:
                notify = True
                break
        if notify:
            break

    if notify:
        module.motor.angle(85)
    else:
        module.motor.angle(0)

    time.sleep(delay)
