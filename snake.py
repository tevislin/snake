import curses

# create window
curses.initscr()
win = curses.newwin(20, 60, 0, 0)  # y, x
win.keypad(1)  # because I want to use the key pad
curses.noecho()  # because we don't want the game to resond to other characters
curses.curs_set(0)
win.border(0)
win.nodelay(1)

#snake and food
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)


win.addch(food[0], food[1], "#")
# game logic
score = 0

ESC = 27
key = curses.KEY_RIGHT


while key != ESC:
    event = win.getch()

    for c in snake:
        win.addch(c[0], c[1], "*")

    win.addch(food[0], food[1], "#")

curses.endwin()
print(f"Final score = {score}")
