from tkinter import *
from utils import modes


def gui():
    window = Tk()
    window.title("G(w)entBot v0.1")

    frame = Frame()
    label = Label(master=frame, text="")
    label.pack()
    frame.pack()
    frame_minutes = Frame()
    frame_games = Frame()
    frame_buttons = Frame()

    label_minutes = Label(master=frame_minutes, text="Minutes Per Game (Default=8): ")
    label_minutes.grid(row=0, column=0)
    label_games = Label(master=frame_games, text="       Games To Play (Default=1): ")
    label_games.grid(row=1, column=0)

    entry_minutes = Entry(master=frame_minutes)
    entry_minutes.grid(row=0, column=1)
    entry_games = Entry(master=frame_games)
    entry_games.grid(row=1, column=1)

    def play():
        try:
            times = int(entry_games.get())
            minutes = int(entry_minutes.get())
        except ValueError:
            times = 1
            minutes = 8
        modes.play_gwent(times, minutes)

    def level_up():
        try:
            times = int(entry_games.get())
        except ValueError:
            times = 1
        modes.just_forfeit(times)

    button_seasonal = Button(master=frame_buttons, text="Play Seasonal Mode", command=play)
    button_seasonal.grid(row=0, column=0)
    empty_label = Label(master=frame_buttons, text=" "*4)
    empty_label.grid(row=0, column=1)
    button_levelup = Button(master=frame_buttons, text="Just Level Up", command=level_up)
    button_levelup.grid(row=0, column=2)

    frame_minutes.pack()
    frame_games.pack()
    frame_buttons.pack()

    frame2 = Frame()
    label2 = Label(master=frame2, text=" ")
    label2.pack()
    frame2.pack()

    window.mainloop()
