from actions import timer, open_gwent, start_seasonal, mulligan, \
    activate_leader, activate_token, play_card, pass_round, forfeit


@timer
def leader_token(times):
    for _ in range(times):
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


def play_gwent(games, leader, normal):
    open_gwent()
    for _ in range(games):
        start_seasonal()
        leader_token(leader)
        play(normal)
        forfeit()


if __name__ == '__main__':
    play_gwent(2, 10, 15)
