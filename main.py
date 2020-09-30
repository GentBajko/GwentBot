from actions import timer, open_gwent, start_seasonal, mulligan, \
    activate_leader, activate_token, play_card, pass_round, forfeit


@timer
def leader_token(times):
    for _ in range(1, times):
        mulligan()
        activate_leader()
        activate_token()
        play_card()
        pass_round()


@timer
def play(times):
    for _ in range(times):
        mulligan()
        play_card()
        pass_round()


def play_gwent(games, minutes_per_game=7):
    play_ratio = 0.7755102040816326
    leader_ratio = 0.22448979591836735
    if type(minutes_per_game) is float:
        minutes_per_game = int(minutes_per_game) + 1
    normal = (((((minutes_per_game * 60) - 110) * play_ratio) // 60) + 1)
    leader = (((((minutes_per_game * 60) - 110) * leader_ratio) // 60) + 1)
    open_gwent()
    for _ in range(games):
        start_seasonal()
        leader_token(leader)
        play(normal)
        forfeit()


if __name__ == '__main__':
    play_gwent(2, 7)
