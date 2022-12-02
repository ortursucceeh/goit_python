contacts = {}

EXIT_WORDS = ["exit", "close", "good bye", "end"]


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Wrong name."
        except TypeError:
            return "Wrong command format."
        except IndexError:
            return "Wrong input data. Enter name and phone."
        except ValueError as e:
            return e.args[0]
        except Exception as e:
            return e.args
    return wrapper


@input_error
def add_contact(name, number=None):
    """Func which adds new contact in contacts"""
    if number is None:
        raise IndexError
    elif name in contacts:
        raise ValueError(f"{name} is already in contacts")
    contacts[name] = number
    return f"Contact with name {name} and phone {number} was added."


@input_error
def find_contact(name, number=None):
    """Func which shows name's number"""
    return contacts[name]


@input_error
def change_contact(name, new_number=None):
    """Func which changes some contact"""
    if name in contacts:
        contacts[name] = new_number
        return f"Contact's number with name {name} was changed to {new_number}."
    else:
        raise ValueError("Unknown name.")


@input_error
def show_all_contacts(*args):
    """Func which shows all contacts"""
    if contacts:
        return '\n'.join([f"{key} ---:  {value}" for key, value in contacts.items()])
    else:
        return "You don't have any contacts."


@input_error
def remove_contact(name, number=None):
    """Func which deletes contact"""
    del contacts[name]
    return f"Contact with name {name} was removed."


@input_error
def show_all_commands(name=None, number=None):
    """Func which shows all commands"""
    return " # ".join(handler.keys())


handler = {
    "hello": lambda: "Hello! How can I help you?",
    "add": add_contact,
    "change": change_contact,
    "phone": find_contact,
    "show": show_all_contacts,
    "remove": remove_contact,
    "commands": show_all_commands
}


def main():
    while True:

        command = input("Enter command: ").lower().strip().split()

        if command[0] in EXIT_WORDS:
            print("See ya!")
            exit()

        elif command[0] in handler:
            print(handler[command[0]](*command[1:]))
        else:
            print("Incorrect command. (To see all commands enter 'commands')")


if __name__ == "__main__":
    main()
