import random
import pyautogui as pg
import time
word = ('Hello!', 'How are you', 'Good')
time.sleep(8)
for i in range(500):
    a = random.choice(word)
    pg.write("Hey"+" " +a)
    pg.press('enter')
