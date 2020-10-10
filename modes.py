from actions import timer, open_gwent, start_seasonal, forfeit, intro, midgame, quit_game, start_ranked


games_played = 0


@timer
def play_gwent(games=1, minutes_per_game=8, ranked='Seasonal'):
    global games_played
    play_card_duration = 20.766496400000
    if type(minutes_per_game) is float:
        minutes_per_game = int(minutes_per_game) + 1
    leader = 7
    seconds = (minutes_per_game * 60) - (127 + leader * 30.7629)
    normal = seconds // play_card_duration
    open_gwent()
    for _ in range(games):
        if ranked == 'Seasonal':
            start_seasonal()
        else:
            start_ranked()
        intro(leader)
        midgame(normal)
        forfeit()
        games_played += 1
    quit_game()
    return 'play_gwent'


@timer
def just_forfeit(games=1):
    open_gwent()
    for _ in range(games):
        start_seasonal()
        midgame(1)
        forfeit()
    quit_game()
    return 'just_forfeit'


if __name__ == '__main__':
    play_gwent(40, 12)
