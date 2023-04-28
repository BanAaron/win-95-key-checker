import sys

from win95 import validate_win95_key

if __name__ == "__main__":
    while True:
        # Get input from user
        print("Enter your ✨Windows 95✨ key:")
        user_intput = input()

        # Check and pass the user input
        if user_intput.lower() in ("exit", "quit"):
            sys.exit()
        validate_win95_key(user_intput)
