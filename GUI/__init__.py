import tkinter.ttk as ttk
import tkinter
import actions
import modes
from ttkthemes import ThemedTk


def gui():
    window = ThemedTk(theme='ubuntu')
    window.title("G(w)entBot")
    window.iconbitmap("favicon.ico")
    styles = ttk.Style()
    styles.theme_use(themename=None)

    frame_minutes = ttk.Frame()
    frame_games = ttk.Frame()
    frame_buttons = ttk.Frame()

    label_minutes = ttk.Label(master=frame_minutes, text="    Minutes / Game:")
    label_minutes.grid(row=0, column=0)
    label_games = ttk.Label(master=frame_games, text="    Games To Play:")
    label_games.grid(row=1, column=0)
    label_kegs = ttk.Label(master=frame_games, text="        Open Kegs:")
    label_kegs.grid(row=2, column=0)

    entry_minutes = ttk.Entry(master=frame_minutes)
    entry_minutes.grid(row=0, column=1)
    entry_minutes.insert(0, 10)
    entry_games = ttk.Entry(master=frame_games)
    entry_games.grid(row=1, column=1)
    entry_games.insert(0, 1)
    entry_kegs = ttk.Entry(master=frame_games)
    entry_kegs.grid(row=2, column=1)

    combobox = ttk.Combobox(master=frame_buttons, values=['Seasonal', 'Ranked'])
    combobox.grid(row=0, column=1)
    combobox.insert(0, 'Seasonal')

    def play():
        game_mode = combobox.get()
        try:
            times = int(entry_games.get())
            minutes = int(entry_minutes.get())
        except ValueError:
            times = 1
            minutes = 8
        modes.play_gwent(times, minutes, game_mode)

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
        actions.open_kegs(times)

    button_seasonal = ttk.Button(master=frame_buttons, text="Play", command=play)
    button_seasonal.grid(row=0, column=0)
    button_levelup = ttk.Button(master=frame_buttons, text="Level Up", command=level_up)
    button_levelup.grid(row=1, column=0)
    button_levelup = ttk.Button(master=frame_buttons, text="Open Kegs", command=kegs)
    button_levelup.grid(row=1, column=1)

    frame_minutes.pack()
    frame_games.pack()
    frame_buttons.pack()

    window.wm_attributes("-topmost", 1)
    window.mainloop()
