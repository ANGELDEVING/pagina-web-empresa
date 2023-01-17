import pyautogui as pt
import time

limit = input("cantidad de mensajes")
mensagge = input("Mensaje")
i = 0

time.sleep(3)

while i < int(limit):
    pt.typewrite(mensagge)
    pt.press("enter")
    i += 1