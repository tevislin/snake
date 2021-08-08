import curses

# create window
curses.initscr()
win = curses.newwin(20, 60, 0, 0)  # y, x
win.keypad(1)
