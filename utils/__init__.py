from time import sleep, perf_counter
from pyautogui import press, keyDown, keyUp, typewrite, mouseDown, mouseUp
import pyautogui
from random import randint

pyautogui.PAUSE = 0.5
SCREEN_SIZE = pyautogui.size()
# Seconds it takes for Gwent to open
OPEN_GWENT_WAIT_TIME = 40
# How many times to press enter to reach the main screen
OPEN_GWENT_ENTER_PRESS = 4
# Time it takes Gwent to start the game
START_SEASONAL_LOAD_TIME = 50
PLAYER_LEFT_X = 370
PLAYER_RIGHT_X = 1580
PLAYER_TOP_Y = 480
PLAYER_BOTTOM_Y = 870
GWENT_WINDOW_NAME = None


def timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        finish = perf_counter()
        print(result, f'{(finish - start):0.12f}')
        return result
    return wrapper


def switch_windows():
    global GWENT_WINDOW_NAME
    print(pyautogui.getActiveWindowTitle())
    if pyautogui.getActiveWindowTitle() == 'Gwent':
        return True
    sleep(10)
    try:
        GWENT_WINDOW_NAME = pyautogui.getWindowsWithTitle('Gwent')[1]
        GWENT_WINDOW_NAME.activate()
        GWENT_WINDOW_NAME.maximize()
    except IndexError:
        return False
    return False


def ingame_click(x=None, y=None, button='left', clicks=1, intervals=0.0):
    for _ in range(clicks):
        mouseDown(x, y, button)
        mouseUp(x, y, button)
        sleep(intervals)


def open_gwent():
    if not switch_windows():
        press('winleft')
        typewrite('gwent')
        press('enter')
        sleep(OPEN_GWENT_WAIT_TIME)
        switch_windows()
        ingame_click(x=960, y=1020, clicks=OPEN_GWENT_ENTER_PRESS, intervals=0.7)
        ingame_click(x=900, y=600)


def start_seasonal():
    switch_windows()
    ingame_click(x=1400, y=555, intervals=1)
    ingame_click(x=700, y=555)
    sleep(START_SEASONAL_LOAD_TIME)


def mulligan():
    switch_windows()
    cards = [(900, 520), (1200, 520), (1500, 520)]
    for _ in range(5):
        card = cards[randint(0, 2)]
        ingame_click(x=card[0], y=card[1])


def activate_leader():
    switch_windows()
    ingame_click(x=240, y=700, clicks=2)
    sleep(3)
    ingame_click(x=950, y=570, clicks=2)


def activate_token():
    switch_windows()
    ingame_click(1100, 550)
    press('enter', presses=3)
    ingame_click(900, 550)
    press('enter', presses=3)
    ingame_click(850, 550)


def play_card():
    switch_windows()
    cards = [(800, 960), (900, 960), (600, 960), (700, 960), (800, 960),
             (900, 960), (1000, 960), (1100, 960), (1200, 960), (1300, 960)]
    card = cards[randint(0, 2)]
    ingame_click(x=card[0], y=card[1])
    sleep(0.7)
    ingame_click(x=randint(PLAYER_LEFT_X, PLAYER_RIGHT_X),
                 y=randint(PLAYER_TOP_Y, PLAYER_BOTTOM_Y), clicks=2)
    x = 990
    y = 800
    for i in range(2):
        ingame_click(x=x - (130 * i), y=600)
        ingame_click(x=x - (130 * i), y=y)
        press('enter', presses=3, interval=0.5)


def pass_round():
    switch_windows()
    press('space', presses=5, interval=0.5)
    sleep(10)


def forfeit(send_gg=True):
    switch_windows()
    ingame_click(0, 550, intervals=0.2)
    ingame_click(350, 900, intervals=0.2)
    ingame_click(180, 180, intervals=0.2)
    ingame_click(900, 600, intervals=0.2)
    sleep(10)
    if send_gg:
        ingame_click(950, 910, intervals=0.2)
    ingame_click(970, 1030, clicks=3, intervals=1)
    ingame_click(880, 1020, clicks=3, intervals=10)


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


def intro(times):
    for _ in range(1, times):
        mulligan()
        activate_leader()
        activate_token()
        play_card()
        pass_round()
    return 'leader_token'


def midgame(times):
    for _ in range(times):
        mulligan()
        play_card()
        pass_round()
    return 'play'


if __name__ == '__main__':
    forfeit()
