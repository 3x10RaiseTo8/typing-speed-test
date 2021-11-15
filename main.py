import curses
from curses import wrapper
from time import time
import random


def main(stdscr):

    # Initialization of color pairs
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)  # Correct
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)  # Wrong
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal

    # The welcome screen
    welcome(stdscr)

    # Gives test until user presses ESC
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

    # Gets random text from a file
    with open("text.txt") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def display(stdscr, given, userinput, wpm):

    # Displays text to be written and live WPM
    stdscr.addstr(given)
    stdscr.addstr(2, 0, f"WPM: {wpm}")

    # Logic for correct and incorrect character input
    for i, char in enumerate(userinput):
        color = curses.color_pair(
            1) if given[i] == char else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)


def test(stdscr):

    # Loading essential variables in memory
    given = get_text()
    userinput = []
    wpm = 0
    start = time()

    # Constantly asks for input, returns error if not provided (Required for LIVE update of WPM)
    stdscr.nodelay(True)

    while True:

        # Word per minute calculation using time module
        elapsed = max(time() - start, 1)
        wpm = round((len(userinput) / (elapsed / 60)) / 5)

        # Live update of text on screen
        stdscr.clear()
        display(stdscr, given, userinput, wpm)
        stdscr.refresh()

        # Checks if the user completed the test
        if "".join(userinput) == given:
            stdscr.nodelay(False)
            break

        # If no key input, stop the error and continue
        try:
            key = stdscr.getkey()
        except:
            continue

        # Escape to quit
        if ord(key) == 27:
            break

        # Backspace to delete
        elif key in ["KEY_BACKSPACE", "\b", "\x7f"]:
            if userinput:
                userinput.pop()

        # User cannot enter more characters that the given text
        elif len(userinput) < len(given):
            userinput.append(key)


# Calling the main function in a wrapper which sets up curses module
wrapper(main)
