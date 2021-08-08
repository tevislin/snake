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
    win.addstr(0, 2, 'Score' + str(score) + '')
    win.timeout(150 - (len(snake))//5 + len(snake)//10 %
                120)  # incrrease speed of the snake

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    # CHECKING KEYS
    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    # calculate the next coordinates
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    for c in snake:
        win.addch(c[0], c[1], "*")

    win.addch(food[0], food[1], "#")

curses.endwin()
print(f"Final score = {score}")
