from utils import timer, open_gwent, start_seasonal, forfeit, intro, midgame


@timer
def play_gwent(games=1, minutes_per_game=8):
    play_ratio = 0.7755102040816326
    # leader_ratio = 0.22448979591836735
    if type(minutes_per_game) is float:
        minutes_per_game = int(minutes_per_game) + 1
    leader = 4
    seconds = (minutes_per_game * 60) - (102 + leader * 30.7629)
    normal = ((seconds * play_ratio) // 60) * 4
    # leader = (((seconds * leader_ratio) // 60) + 1) * 2
    open_gwent()
    for _ in range(games):
        start_seasonal()
        intro(leader)
        midgame(normal)
        forfeit()
    return 'play_gwent'


@timer
def just_forfeit(games=1):
    open_gwent()
    for _ in range(games):
        start_seasonal()
        midgame(1)
        forfeit()
    return 'just_forfeit'


if __name__ == '__main__':
    play_gwent(1, 9)
