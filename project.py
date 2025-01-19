# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:02:26 2025

@author: hilal
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:42:14 2025

@author: hilal
"""

import os
import platform

# Dictionary to store ASCII art for each character
ascii_art = {
    'a': [
        "           ",
        "           ",
        "   __ _    ",
        "  / _` |   ",
        " | (_| |   ",
        "  \\__,_|   ",
        "           ",
        "           "
    ],
    'b': [
        "  _        ",
        " | |       ",
        " | |__     ",
        " | '_ \\    ",
        " | |_) |   ",
        " |_.__/    ",
        "           ",
        "           "
    ],
    'c': [
        "           ",
        "           ",
        "   ___     ",
        "  / __|    ",
        " | (__     ",
        "  \\___|    ",
        "           ",
        "           "
    ],
    'd': [
        "      _    ",
        "     | |   ",
        "   __| |   ",
        "  / _` |   ",
        " | (_| |   ",
        "  \\__,_|   ",
        "           ",
        "           "
    ],
    'e': [
        "           ",
        "           ",
        "   ___     ",
        "  / _ \\    ",
        " |  __/    ",
        "  \\___|    ",
        "           ",
        "           "
    ],
    'f': [
        "   __      ",
        "  / _|     ",
        " | |_      ",
        " |  _|     ",
        " | |       ",
        " |_|       ",
        "           ",
        "           "
    ],
    'g': [
        "           ",
        "           ",
        "   __ _    ",
        "  / _` |   ",
        " | (_| |   ",
        "  \\__, |   ",
        "   __/ |   ",
        "  |___/    "
    ],
    'h': [
        "  _        ",
        " | |       ",
        " | |__     ",
        " | '_ \\    ",
        " | | | |   ",
        " |_| |_|   ",
        "           ",
        "           "
    ],
    'i': [
        "  _        ",
        " (_)       ",
        "  _        ",
        " | |       ",
        " | |       ",
        " |_|       ",
        "           ",
        "           "
    ],
    'j': [
        "    _      ",
        "   (_)     ",
        "    _      ",
        "   | |     ",
        "   | |     ",
        "   | |     ",
        "  _/ |     ",
        " |__/      "
    ],
    'k': [
        "  _        ",
        " | |       ",
        " | | __    ",
        " | |/ /    ",
        " |   <     ",
        " |_|\_\    ",
        "           ",
        "           "
    ],
    'l': [
        "  _        ",
        " | |       ",
        " | |       ",
        " | |       ",
        " | |       ",
        " |_|       ",
        "           ",
        "           "
    ],
    'm': [
        "               ",
        "               ",
        "  _ __ ___     ",
        " | '_ ` _ \\    ",
        " | | | | | |   ",
        " |_| |_| |_|   ",
        "               ",
        "               "
    ],
    'n': [
        "           ",
        "           ",
        "  _ __     ",
        " | '_ \\    ",
        " | | | |   ",
        " |_| |_|   ",
        "           ",
        "           "
    ],
    'o': [
        "           ",
        "           ",
        "   ___     ",
        "  / _ \\    ",
        " | (_) |   ",
        "  \\___/    ",
        "           ",
        "           "
    ],
    'p': [
        "           ",
        "           ",
        "  _ __     ",
        " | '_ \\    ",
        " | |_) |   ",
        " | .__/    ",
        " | |       ",
        " |_|       "
    ],
    'q': [
        "           ",
        "           ",
        "   __ _    ",
        "  / _` |   ",
        " | (_| |   ",
        "  \\__, |   ",
        "     | |   ",
        "     |_|   "
    ],
    'r': [
        "           ",
        "           ",
        "  _ __     ",
        " | '__|    ",
        " | |       ",
        " |_|       ",
        "           ",
        "           "
    ],
    's': [
        "           ",
        "           ",
        "  ___      ",
        " / __|     ",
        " \\__ \\     ",
        " |___/     ",
        "           ",
        "           "
    ],
    't': [
        "  _        ",
        " | |       ",
        " | |_      ",
        " | __|     ",
        " | |_      ",
        "  \\__|     ",
        "           ",
        "           "
    ],
    'u': [
        "           ",
        "           ",
        "  _   _    ",
        " | | | |   ",
        " | |_| |   ",
        "  \\__,_|   ",
        "           ",
        "           "
    ],
    'v': [
        "           ",
        "           ",
        " __   __   ",
        " \\ \\ / /   ",
        "  \\ V /    ",
        "   \\_/     ",
        "           ",
        "           "
    ],
    'w': [
        "               ",
        "               ",
        " __      __    ",
        " \\ \\ /\\ / /    ",
        "  \\ V  V /     ",
        "   \\_/\\_/      ",
        "               ",
        "               "
    ],
    'x': [
        "           ",
        "           ",
        " __  __    ",
        " \\ \\/ /    ",
        "  >  <     ",
        " /_/\\_\\    ",
        "           ",
        "           "
    ],
    'y': [
        "           ",
        "           ",
        "  _   _    ",
        " | | | |   ",
        " | |_| |   ",
        "  \\__, |   ",
        "   __/ |   ",
        "  |___/    "
    ],
    'z': [
        "           ",
        "           ",
        "  ____     ",
        " |_  /     ",
        "  / /      ",
        " /___|     ",
        "           ",
        "           "
    ],
    ' ': [" " * 11] * 8,
    '.': [
        "           ",
        "           ",
        "           ",
        "           ",
        "   _       ",
        "  (_)      ",
        "           ",
        "           "
    ],
    '!': [
        "   _       ",
        "  | |      ",
        "  | |      ",
        "  | |      ",
        "  |_|      ",
        "  (_)      ",
        "           ",
        "           "
    ],
    '?': [
        "   ___     ",
        "  |__ \\    ",
        "     ) |   ",
        "    / /    ",
        "   |_|     ",
        "   (_)     ",
        "           ",
        "           "
    ],
    # Add remaining uppercase letters, numbers, and symbols
}

# Function to clear the console
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Function to print ASCII art side-by-side
def print_ascii_art(text):
    rows = [""] * 8  # Maximum height of ASCII art
    for char in text.lower():
        art = ascii_art.get(char, ["[??]"] * 8)  # Handle undefined characters
        for i, line in enumerate(art):
            rows[i] += line + "  "
    for row in rows:
        print(row)

# Main program
if __name__ == "__main__":
    clear_console()
    print("Welcome to the ASCII Art Generator!")
    while True:
        user_input = input("Enter text to generate ASCII art (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print_ascii_art(user_input)
