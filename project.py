
"""
Created on Sun Jan 12 14:42:14 2025

@author: hilal
"""

import os
import platform

# ASCII art dictionary to represent each character with a corresponding ASCII art representation
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
        "  _      ",
        " | |     ",
        " | |     ",
        " | |     ",
        " | |     ",
        " |_|     ",
        "         ",
        "         "
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
        "  |__ \\   ",
        "     ) |   ",
        "    / /    ",
        "   |_|     ",
        "   (_)     ",
        "           ",
        "           "
    ],
    '0': [
        "   ___     ",
        "  / _ \    ",
        " | | | |   ",
        " | | | |   ",
        " | |_| |   ",
        "  \___/    ",
        "           ",
        "           "
    ],
    '1': [
        "   __      ",
        " /_ |      ",
        "  | |      ",
        "  | |      ",
        "  | |      ",
        "  |_|      ",
        "           ",
        "           "
    ],
    '2': [
        "  ___      ",
        " |__ \     ",
        "    ) |    ",
        "   / /     ",
        "  / /_     ",
        " |____|    ",
        "           ",
        "           "
    ],
    '3': [
        "  ____     ",
        " |___ \    ",
        "   __) |   ",
        "  |__ <    ",
        "  ___) |   ",
        " |____/    ",
        "           ",
        "           "
    ],
    '4': [
        "  _  _     ",
        " | || |    ",
        " | || |_   ",
        " |__   _|  ",
        "    | |    ",
        "    |_|    ",
        "           ",
        "           "
    ],
    '5': [
        "  _____    ",
        " | ____|   ",
        " | |__     ",
        " |___ \    ",
        "  ___) |   ",
        " |____/    ",
        "           ",
        "           "
    ],
    '6': [
        "    __     ",
        "   / /     ",
        "  / /_     ",
        " | '_ \    ",
        " | (_) |   ",
        "  \___/    ",
        "           ",
        "           "
    ],
    '7': [
        "  ______    ",
        " |____  |   ",
        "     / /    ",
        "    / /     ",
        "   / /      ",
        "  /_/       ",
        "            ",
        "            "
    ],
    '8': [
        "   ___     ",
        "  / _ \    ",
        " | (_) |   ",
        "  > _ <    ",
        " | (_) |   ",
        "  \___/    ",
        "           ",
        "           "
    ],
    '9': [
        "   ___     ",
        "  / _ \    ",
        " | (_) |   ",
        "  \__, |   ",
        "    / /    ",
        "   /_/     ",
        "           ",
        "           "
    ],
    'A': [
        "            ",
        "     /\     ",
        "    /  \    ",
        "   / /\ \   ",
        "  / ____ \  ",
        " /_/    \_\ ",
        "            ",
        "            "
    ],
    'B': [
        "  ____  ",
        " |  _ \ ",
        " | |_) |",
        " |  _ < ",
        " | |_) |",
        " |____/ ",
        "        ",
        "        "
    ],
    'C': [
        "   _____ ",
        "  / ____|",
        " | |     ",
        " | |     ",
        " | |     ",
        "  \_____|",
        "         ",
        "         "
    ],
    'D': [
        "  _____  ",
        " |  __ \ ",
        " | |  | |",
        " | |  | |",
        " | |  | |",
        " |_____/ ",
        "         ",
        "         "
    ],
    'E': [
        "  ______ ",
        " |  ____|",
        " | |__   ",
        " |  __|  ",
        " | |____ ",
        " |______|",
        "         ",
        "         "
    ],
    'F': [
        "  ______ ",
        " |  ____|",
        " | |__   ",
        " |  __|  ",
        " | |     ",
        " |_|     ",
        "         ",
        "         "
    ],
    'G': [
        "   _____ ",
        "  / ____|",
        " | |  __ ",
        " | | |_ |",
        " | |__| |",
        "  \_____|",
        "         ",
        "         "
    ],
    'H': [
        "  _    _ ",
        " | |  | |",
        " | |__| |",
        " |  __  |",
        " | |  | |",
        " |_|  |_|",
        "         ",
        "         "
    ],
    'I': [
        "  _____ ",
        " |_   _|",
        "   | |  ",
        "   | |  ",
        "  _| |_ ",
        " |_____|",
        "        ",
        "        "
    ],
    'J': [
        "       _ ",
        "      | |",
        "      | |",
        "  _   | |",
        " | |__| |",
        "  \____/ ",
        "         ",
        "         "
    ],
    'K': [
        "  _  __ ",
        " | |/ / ",
        " | ' /  ",
        " |  <   ",
        " | . \  ",
        " |_|\_\ ",
        "        ",
        "        "
    ],
    'L': [
        "  _      ",
        " | |     ",
        " | |     ",
        " | |     ",
        " | |____ ",
        " |______|",
        "         ",
        "         "
    ],
    'M': [
        "  __  __ ",
        " |  \/  |",
        " | \  / |",
        " | |\/| |",
        " | |  | |",
        " |_|  |_|",
        "         ",
        "         "
    ],
    'N': [
        "  _   _ ",
        " | \ | |",
        " |  \| |",
        " | . ` |",
        " | |\  |",
        " |_| \_|",
        "        ",
        "        "
    ],
    'O': [
        "   ____  ",
        "  / __ \ ",
        " | |  | |",
        " | |  | |",
        " | |__| |",
        "  \____/ ",
        "         ",
        "         "
    ],
    'P': [
        "  _____  ",
        " |  __ \ ",
        " | |__) |",
        " |  ___/ ",
        " | |     ",
        " |_|     ",
        "         ",
        "         "
    ],
    'Q': [
        "   ____   ",
        "  / __ \  ",
        " | |  | | ",
        " | |  | | ",
        " | |__| | ",
        "  \___\_\ ",
        "          ",
        "          "
    ],
    'R': [
        "  _____   ",
        " |  __ \  ",
        " | |__) | ",
        " |  _  /  ",
        " | | \ \  ",
        " |_|  \_\ ",
        "          ",
        "          "
    ],
    'S': [
        "   _____ ",
        "  / ____|",
        " | (___  ",
        "  \___ \ ",
        "  ____) |",
        " |_____/ ",
        "         ",
        "         "
    ],
    'T': [
        "  _______ ",
        " |__   __|",
        "    | |   ",
        "    | |   ",
        "    | |   ",
        "    |_|   ",
        "          ",
        "          "
    ],
    'U': [
        "  _    _ ",
        " | |  | |",
        " | |  | |",
        " | |  | |",
        " | |__| |",
        "  \____/ ",
        "         ",
        "         "
    ],
    'V': [
        " __      __",
        " \ \    / /",
        "  \ \  / / ",
        "   \ \/ /  ",
        "    \  /   ",
        "     \/    ",
        "           ",
        "           "
    ],
    'W': [
        " __          __",
        " \ \        / /",
        "  \ \  /\  / / ",
        "   \ \/  \/ /  ",
        "    \  /\  /   ",
        "     \/  \/    ",
        "               ",
        "               "
    ],
    'X': [
        " __   __ ",
        " \ \ / / ",
        "  \ V /  ",
        "   > <   ",
        "  / . \  ",
        " /_/ \_\ ",
        "         ",
        "         "
    ],
    'Y': [
        " __     __",
        " \ \   / /",
        "  \ \_/ / ",
        "   \   /  ",
        "    | |   ",
        "    |_|   ",
        "          ",
        "          "
    ],
    'Z': [
        "  ______",
        " |___  /",
        "    / / ",
        "   / /  ",
        "  / /__ ",
        " /_____|",
        "        ",
        "        "
    ]
    
    
}

# Function to clear the console screen based on the operating system
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')  # Command to clear the console on Windows
    else:
        os.system('clear')  # Command to clear the console on Unix/Linux/Mac

# Function to print the ASCII art for a given text input
def print_ascii_art(text):
    rows = [""] * 8  # Initialize a list of 8 empty strings, one for each row of the ASCII art
    for char in text:
        art = ascii_art.get(char, ["[??]"] * 8)  # Get the ASCII art for the character, or placeholder if not found
        for i, line in enumerate(art):
            rows[i] += line + "  "  # Append the line of ASCII art to the corresponding row, with spacing
    for row in rows:
        print(row)  # Print each row of the ASCII art

# Main entry point of the script
if __name__ == "__main__":
    clear_console()  # Clear the console screen
    print("Welcome to the ASCII Art Generator!")  # Welcome message
    while True:
        user_input = input("Enter text to generate ASCII art (or type nothing to quit): ")  # Prompt user for input
        if user_input.lower() == "":  # Check if user wants to exit
            print("Goodbye!")  # Goodbye message
            break  # Exit the loop
        print_ascii_art(user_input)  # Generate and print the ASCII art for the input
