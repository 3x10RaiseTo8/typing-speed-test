# typing-speed-test

This is a basic Command Line Interface (CLI) application which records typing speed of the user in Words per Minute (WPM). The application randomizes text from `text.txt` file and measures typing speed in runtime. The test is successful only if the user enters the exact text match, hence mistakes are NOT ignored. Based on `curses` module.

## How to use

Download and extract this repository in a folder. Open any terminal application and navigate to that folder. Run `main.py` file in Python `3.x`. Press `escape` to exit.

`Curses` module comes preinstalled with Python on Mac and Linux, but not on Windows. For running this code on Windows machine, do `pip install windows-curses` first.

Add new lines in `text.txt` to customise test.
