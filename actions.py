from time import sleep, perf_counter
from pyautogui import press, typewrite, mouseDown, mouseUp, moveTo
import pyautogui
from random import randint
# from cards import deck
import cv2 as cv
import numpy as np
import os

pyautogui.PAUSE = 0.5
SCREEN_SIZE = pyautogui.size()
X_SIZE = pyautogui.size()[0]
Y_SIZE = pyautogui.size()[1]
# Seconds it takes for Gwent to open
OPEN_GWENT_WAIT_TIME = 60
# How many times to press enter to reach the main screen
OPEN_GWENT_ENTER_PRESS = 4
# Time it takes Gwent to start the game
START_SEASONAL_LOAD_TIME = 50
PLAYER_LEFT_X = round(X_SIZE * 0.19270833333333334)
PLAYER_RIGHT_X = round(X_SIZE * 0.8229166666666666)
PLAYER_TOP_Y = round(Y_SIZE * 0.4444444444444444)
PLAYER_BOTTOM_Y = round(Y_SIZE * 0.8055555555555556)
try:
    GWENT_WINDOW_NAME = pyautogui.getWindowsWithTitle('Gwent')[0]
except IndexError:
    GWENT_WINDOW_NAME = None
CURRENT_DECK = ['Old_Speartip_Awake', 'Living_Armor', 'Yghern', 'Naglfar',
                'Old_Speartip_Asleep', 'Cave_Troll', 'Katakan',
                'Protofelder', 'Golyat', 'Tatterwing', 'The_Beast',
                'Kikimore_Worker', 'Ice_Troll', 'Drowner',
                'Endrega_Larva', 'Noonwraith', 'Endrega_Warrior', 'Bruxa']


def timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        finish = perf_counter()
        print(result, f'{(finish - start):0.12f}')
        return result

    return wrapper


def scr(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if 'screenshots' not in os.listdir(os.getcwd()):
            os.mkdir('screenshots')
        i = 0
        while f"{result}{i}.png" in os.listdir("screenshots"):
            i += 1
        pyautogui.screenshot().save(os.path.join(os.getcwd(), 'screenshots', f"{result}{i}.png"))

    return wrapper


def switch_windows():
    global GWENT_WINDOW_NAME
    if not GWENT_WINDOW_NAME:
        open_gwent()
        GWENT_WINDOW_NAME = pyautogui.getWindowsWithTitle('Gwent')[0]
    if pyautogui.getActiveWindowTitle()[0] == 'Gwent':
        return True
    try:
        GWENT_WINDOW_NAME.activate()
        GWENT_WINDOW_NAME.maximize()
        pyautogui.screenshot()
    except IndexError:
        return False
    return False


def ingame_click(x=None, y=None, button='left', clicks=1, intervals=0.0):
    for _ in range(clicks):
        mouseDown(x, y, button)
        mouseUp(x, y, button)
        sleep(intervals)


@scr
@timer
def open_gwent():
    if len(pyautogui.getWindowsWithTitle('Gwent')) == 0:
        press('winleft')
        typewrite('gwent')
        press('enter')
        sleep(OPEN_GWENT_WAIT_TIME)
        switch_windows()
        ingame_click(x=960, y=1020, clicks=OPEN_GWENT_ENTER_PRESS, intervals=0.7)
        ingame_click(x=900, y=600)
    return 'open'


@timer
def start_seasonal():
    switch_windows()
    sleep(1)
    ingame_click(x=1400, y=555, clicks=2, intervals=0.5)
    ingame_click(x=700, y=555, clicks=2, intervals=0.5)
    sleep(START_SEASONAL_LOAD_TIME)
    pyautogui.screenshot()
    return 'seasonal'


@timer
def start_ranked():
    switch_windows()
    sleep(1)
    ingame_click(x=500, y=500, clicks=2, intervals=0.5)
    sleep(START_SEASONAL_LOAD_TIME)
    pyautogui.screenshot()
    return 'ranked'


@timer
def mulligan():
    switch_windows()
    cards = [(900, 520), (1200, 520), (1500, 520)]
    for _ in range(3):
        card = cards[randint(0, 2)]
        moveTo(x=card[0], y=card[1])
        press('enter')
        pyautogui.screenshot()
    return 'mulligan'


@timer
def activate_leader():
    switch_windows()
    moveTo(x=240, y=700)
    press('enter', presses=3, interval=0.5)
    sleep(1.5)
    moveTo(x=960, y=700)
    press('enter', presses=3, interval=0.5)
    return 'leader'


@scr
@timer
def activate_token():
    switch_windows()
    moveTo(1100, 550)
    press('enter', presses=3)
    moveTo(900, 550)
    press('enter', presses=3)
    moveTo(850, 550)
    return 'token'


@scr
@timer
def play_card():
    switch_windows()
    cards = [(800, 960), (900, 960), (600, 960), (700, 960), (800, 960),
             (900, 960), (1000, 960), (1100, 960), (1200, 960), (1300, 960)]
    card = cards[5:8][randint(0, 2)]
    moveTo(x=card[0], y=card[1])
    press('enter', presses=3, interval=0.5)
    sleep(0.7)
    moveTo(x=randint(PLAYER_LEFT_X, PLAYER_RIGHT_X),
           y=randint(PLAYER_TOP_Y, PLAYER_BOTTOM_Y))
    press('enter', presses=3, interval=0.5)
    x = 990
    y = 800
    for i in range(3):
        moveTo(x=x - (130 * i), y=600)
        press('enter', presses=3, interval=0.5)
        moveTo(x=x - (130 * i), y=y)
        press('enter', presses=3, interval=0.5)
    return 'pay card'


@scr
@timer
def pass_round():
    switch_windows()
    press('space', presses=2, interval=0.2)
    return 'pass'


@scr
@timer
def forfeit(send_gg=True):
    switch_windows()
    ingame_click(30, 550, intervals=0.2)
    ingame_click(350, 900, intervals=0.2)
    ingame_click(180, 180, intervals=0.2)
    ingame_click(900, 600, intervals=0.2)
    if send_gg:
        ingame_click(950, 910, intervals=0.2)
    ingame_click(970, 1030, clicks=3, intervals=1)
    ingame_click(880, 1020, clicks=2, intervals=3)
    ingame_click(850, 1040, clicks=3, intervals=1)
    pyautogui.screenshot()
    return 'forfeit'


def quit_game():
    GWENT_WINDOW_NAME.close()


@scr
@timer
def open_kegs(kegs):
    switch_windows()
    cards = [(600, 330), (960, 330), (1300, 330)]
    ingame_click(x=1620, y=50, intervals=7)
    ingame_click(x=900, y=1030, intervals=2)
    for _ in range(kegs):
        switch_windows()
        card = cards[randint(0, 2)]
        ingame_click(x=960, y=330, clicks=2, intervals=0.05)
        ingame_click(card[0], card[1], intervals=1.3)
        ingame_click(x=960, y=1030, intervals=1.5)
    return 'open kegs'


@scr
@timer
def intro(times):
    for _ in range(int(times)):
        mulligan()
        activate_leader()
        activate_token()
        play_card()
        pass_round()
    return 'Intro Combo - '


@scr
@timer
def midgame(times):
    for _ in range(int(times)):
        mulligan()
        play_card()
        pass_round()
    return 'Midgame Combo - '


if __name__ == '__main__':
    locate_card()
