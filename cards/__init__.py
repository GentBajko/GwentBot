import os
import pyautogui
import cv2 as cv
from actions import switch_windows

game_modes = {'seasonal_mode.png': os.path.join(os.getcwd(), 'cards', 'seasonal_mode.png'),
              'standard_mode.png': os.path.join(os.getcwd(), 'cards', 'standard_mode.png')}

deck = {1: ['cards\\Endrega_Larva.png', 'cards\\Drowner.png'],
        2: ['cards\\Cave_Troll.png'],
        3: ['cards\\Bruxa.png', 'cards\\Ice_Troll.png'],
        4: ['cards\\Yghern.png', 'cards\\Katakan.png'],
        5: ['cards\\Noonwraith.png', 'cards\\Kikimore_Warrior.png', 'cards\\Endrega_Warrior.png'],
        6: ['cards\\Protofelder.png', 'cards\\The_Beast.png'],
        7: ['cards\\Naglfar.png', 'cards\\Tatterwing.png'],
        8: ['cards\\Old_Speartip_Asleep.png', 'cards\\Golyat.png'],
        9: ['cards\\Living_Armor.png'],
        10: ['cards\\Old_Speartip_Awake.png']}

deck = {1: ['Endrega_Larva.png', 'Drowner.png'],
        2: ['Cave_Troll.png'],
        3: ['Bruxa.png', 'Ice_Troll.png'],
        4: ['Yghern.png', 'Katakan.png'],
        5: ['Noonwraith.png', 'Kikimore_Warrior.png', 'Endrega_Warrior.png'],
        6: ['Protofelder.png', 'The_Beast.png'],
        7: ['Naglfar.png', 'Tatterwing.png'],
        8: ['Old_Speartip_Asleep.png', 'Golyat.png'],
        9: ['Living_Armor.png'],
        10: ['Old_Speartip_Awake.png']}

CURRENT_DECK = ['Old_Speartip_Awake', 'Living_Armor', 'Yghern', 'Naglfar',
                'Old_Speartip_Asleep', 'Cave_Troll', 'Katakan',
                'Protofelder', 'Golyat', 'Tatterwing', 'The_Beast',
                'Kikimore_Worker', 'Ice_Troll', 'Drowner',
                'Endrega_Larva', 'Noonwraith', 'Endrega_Warrior', 'Bruxa']


def locate_card():
    switch_windows()
    pyautogui.screenshot().save('current_screen.png')
    locations = {1: [], 2: [], 3: [], 4: [], 5: [],
                 6: [], 7: [], 8: [], 9: [], 10: []}
    for weight, cards in deck.items():
        for i in range(len(cards)):
            screen = cv.imread('current_screen.png', cv.IMREAD_ANYDEPTH)
            gwent_img = cv.imread(deck[weight][i], cv.IMREAD_ANYDEPTH)
            result = cv.matchTemplate(screen, gwent_img, cv.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            if max_val > 0.6:
                print(max_val, max_loc, cards[i])
                locations[weight].append((cards[i], max_loc))
    locations = {k: v for k, v in locations.items() if len(v) != 0}
    return locations


if __name__ == '__main__':
    print(locate_card())
