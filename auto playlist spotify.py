#Passo 1: Entrar no spotify
#Passo 2: Entrar na playlist
#Passo 3: Dar play

import pyautogui
import time

pyautogui.PAUSE = 0.7

pyautogui.press("win")
pyautogui.write("spotify")
pyautogui.press("enter")
time.sleep(19)
pyautogui.click(x=231, y=508)
time.sleep(5)
pyautogui.click(x=721, y=585)
