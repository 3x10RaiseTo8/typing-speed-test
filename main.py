import curses
from curses import wrapper
from time import time
import random


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)  # Correct
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)  # Wrong
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal

    welcome(stdscr)

    while True:
        test(stdscr)
        stdscr.addstr(4, 0,
                      "You finished the test! Press ANY key to retake the test or 'ESC' to quit.")
        if ord(stdscr.getkey()) == 27:
            break


def welcome(stdscr):
    stdscr.clear()
    stdscr.addstr(
        "Welcome to the Typing Speed Test!\n\nPress any key to begin.")
    stdscr.refresh()
    stdscr.getkey()


def get_text():
    with open("texts.txt") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def display(stdscr, given, userinput, wpm):
    stdscr.addstr(given)
    stdscr.addstr(2, 0, f"WPM: {wpm}")

    for i, char in enumerate(userinput):
        color = curses.color_pair(
            1) if given[i] == char else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)


def test(stdscr):
    given = get_text()
    userinput = []
    wpm = 0
    start = time()

    stdscr.nodelay(True)

    while True:
        elapsed = max(time() - start, 1)
        wpm = round((len(userinput) / (elapsed / 60)) / 5)

        stdscr.clear()
        display(stdscr, given, userinput, wpm)
        stdscr.refresh()

        if "".join(userinput) == given:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        elif key in ["KEY_BACKSPACE", "\b", "\x7f"]:
            if userinput:
                userinput.pop()
        elif len(userinput) < len(given):
            userinput.append(key)


wrapper(main)
