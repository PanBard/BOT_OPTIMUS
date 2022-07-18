import pyautogui
from time import sleep, time

pyautogui.press('win')
sleep(0.5)
pyautogui.write('cmd')
pyautogui.press('enter')
sleep(1)
pyautogui.write('cd Desktop')

pyautogui.press('enter')

pyautogui.write('cd boty')

pyautogui.press('enter')

pyautogui.write('cd BOT_OPTIMUS')

pyautogui.press('enter')
pyautogui.write('del cascade.xml')
pyautogui.press('enter')
pyautogui.write('cd ..')
pyautogui.press('enter')
pyautogui.write('cd 008_cascade_classifier')
pyautogui.press('enter')
pyautogui.write('cd cascade')
pyautogui.press('enter')
pyautogui.write('copy cascade.xml C:\\Users\\konie\\Desktop\\boty\\BOT_OPTIMUS')
pyautogui.press('enter')

