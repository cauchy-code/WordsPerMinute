import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)


def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        # Exit the loop if the user has completed typing the target text
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)  # Stop non-blocking input
            return wpm  # Return the final WPM

        try:
            key = stdscr.getkey()
        except:
            continue

        # Handle ESC key to quit
        if len(key) == 1 and ord(key) == 27:  # ESC key
            return None  # Signal to exit the test

        # Handle backspace
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        # Handle valid input
        elif len(current_text) < len(target_text):
            # Only accept valid inputs (matching current character in target)
            next_char = target_text[len(current_text)]
            if key == next_char:
                current_text.append(key)
            else:
                # If the key is incorrect, ignore it
                continue


def main(stdscr):
    # Initialize color pairs for text display
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm = wpm_test(stdscr)
        if wpm is None:  # Exit if ESC is pressed during the test
            break

        # Display completion message with final WPM
        stdscr.clear()
        stdscr.addstr(0, 0, f"You completed the text! Your final WPM is: {wpm}")
        stdscr.addstr(2, 0, "Press any key to try again, or ESC to quit.")
        stdscr.refresh()

        # Wait for a key press to restart or quit
        key = stdscr.getkey()
        if len(key) == 1 and ord(key) == 27:  # ESC key to quit
            break


wrapper(main)

