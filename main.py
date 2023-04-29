import sys
import os

from win95 import validate_win95_key

if __name__ == "__main__":
    while True:
        # Get input from user
        print("Enter your ✨Windows 95✨ key:")
        user_input = input()

        # Check and pass the user input
        if user_input.lower() in ("exit", "quit"):
            sys.exit()
        elif user_input.lower() in ("clear", "cls"):
            os.system("cls" if os.name == "nt" else "printf '\033c'")
        else:
            validate_win95_key(user_input)
