from tkinter import *
import utils
from utils import modes


def gui():
    window = Tk()
    window.title("G(w)entBot v0.1")
    window.iconbitmap("favicon.ico")


    frame_minutes = Frame()
    frame_games = Frame()
    frame_buttons = Frame()

    label_minutes = Label(master=frame_minutes, text="Minutes Per Game:")
    label_minutes.grid(row=0, column=0)
    label_games = Label(master=frame_games, text="       Games To Play:")
    label_games.grid(row=1, column=0)
    label_kegs = Label(master=frame_games, text="           Open Kegs:")
    label_kegs.grid(row=2, column=0)

    entry_minutes = Entry(master=frame_minutes)
    entry_minutes.grid(row=0, column=1)
    entry_games = Entry(master=frame_games)
    entry_games.grid(row=1, column=1)
    entry_kegs = Entry(master=frame_games)
    entry_kegs.grid(row=2, column=1)

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

    def kegs():
        try:
            times = int(entry_kegs.get())
        except ValueError:
            times = 1
        utils.open_kegs(times)

    button_seasonal = Button(master=frame_buttons, text="Play Seasonal Mode", command=play)
    button_seasonal.grid(row=0, column=0)
    button_levelup = Button(master=frame_buttons, text="Just Level Up", command=level_up)
    button_levelup.grid(row=0, column=2)
    button_levelup = Button(master=frame_buttons, text="Open Kegs", command=kegs)
    button_levelup.grid(row=0, column=3)

    frame_minutes.pack()
    frame_games.pack()
    frame_buttons.pack()

    window.wm_attributes("-topmost", 1)
    window.lift()
    window.mainloop()
