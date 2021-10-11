import pyautogui
import schedule 
import time
import random

rand_min = random.randrange(41, 49) #interval minutes you want the pyautogui to join your meet
rand_sec1 = random.randrange(1, 3) #interval second 1
rand_sec2 = random.randrange(3, 7) #interval second 2

print(f"06:{rand_min}")#schedule and pyatogui will automate in 06:xx
print(rand_sec1, rand_sec2)

def main():#main function to join meet
    time.sleep(1)
    pyautogui.press('win', interval=0.5)#click windows key by pyautogui
    time.sleep(1)
    pyautogui.typewrite('chrome', interval=0.5)#auto type chrome by pyautogui(you can change it into edge or other browser)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.typewrite('link')  #google meet link (autotype), you can change into your google meet link
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'd')  # Press the Ctrl-E hotkey combination.
    pyautogui.hotkey('ctrl', 'e')  # Press the Ctrl-E hotkey combination.
    time.sleep(5)
    pyautogui.click(1450,635)
    time.sleep(1)
    pyautogui.click(1785,975)
    time.sleep(1)
    pyautogui.click(1785,835)
    pyautogui.typewrite("hadir") 
    time.sleep(2)
    pyautogui.press('enter', interval=0.5)
    time.sleep(2)
    pyautogui.click(1900,20)
    time.sleep(2)

schedule.every().day.at(f"06:{rand_min}").do(main)# to schedule everyday at some fixed time

while True:
    schedule.run_pending()
    time.sleep(10)
