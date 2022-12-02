from art import tprint
from entities import AddressBook, Record
from constants import HELLO_WORDS, EXIT_WORDS
from functions import handler, exit_from


def main():
    tprint("Contact book", font="tarty1")
    while True:

        command = input("Enter command: ").lower().strip().split()

        if command[0] in EXIT_WORDS:
            tprint("Bye!", font="tarty2")
            exit_from()

        elif command[0] in HELLO_WORDS:
            print(handler["hello"]())

        elif command[0] in handler:
            print(handler[command[0]](*command[1:]))
        else:
            print("Incorrect command.\n(To see all commands enter 'commands')")


if __name__ == "__main__":
    main()
