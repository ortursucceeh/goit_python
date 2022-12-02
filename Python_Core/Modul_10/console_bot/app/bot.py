import functools
from art import tprint
from entities import AdressBook, Record, Birthday
from constants import HELLO_WORDS, EXIT_WORDS


def input_error(func):
    @functools.wraps(func)
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
def add_contact(name, number=None, birthday=None):
    """Func which adds new contact in contacts"""
    if number is None:
        raise IndexError
    elif name.lower() in contacts:
        return f"Contact '{name.capitalize()}' is already in adressbook! (Enter add_phone)"

    record = Record(name.lower(), number, birthday)
    contacts.add_record(record)
    return f"Contact with name '{name.capitalize()}' and phone '{number}' was added."


@input_error
def find_contact(name, *args):
    """Func which shows name's number"""
    phones = [phone.value for phone in contacts[name.lower()].phones]
    return f"{name.capitalize()} : {', '.join(phones)}"


@input_error
def change_contact(name, new_number=None):
    """Func which changes some contact"""
    if name.lower() in contacts:
        del contacts[name.lower()]
        record = Record(name.lower(), new_number)
        contacts.add_record(record)
        return f"'{name.capitalize()}'s' number was changed to '{new_number}'."
    raise ValueError("Unknown name.")


@input_error
def show_all_contacts(*args):
    """Func which shows all contacts"""
    tprint("All contacts:", font="tarty2")
    result = []
    for key, value in contacts.items():
        if len(key) > 8:
            key = key[:8] + '...'
        phones = ', '.join([phone.value for phone in value.phones])
        result.append(f"[+] {key.capitalize(): <12}: {phones}")
    return '\n'.join(result)


@input_error
def remove_contact(name, *args):
    """Func which deletes contact"""
    del contacts[name.lower()]
    return f"Contact with name '{name.capitalize()}' was removed."


@input_error
def show_all_commands(*args):
    """Func which shows all commands"""
    return " # ".join(handler.keys())


@input_error
def remove_phone(name, phone=None):
    """Func which deletes phone in record"""
    return contacts[name.lower()].remove_phone(phone)


@input_error
def change_phone(name, old_phone, new_phone):
    """Func which changes phone in record"""
    return contacts[name.lower()].change_phone(old_phone, new_phone)


@input_error
def add_phone(name, number):
    """Func which adds phone in record"""
    if number is None:
        raise IndexError
    elif name.lower() in contacts:
        return contacts[name.lower()].add_phone(number)
    else:
        return f"Unknown name"


def show_days_to_birthday(name, *args):
    name = name.lower()
    if contacts[name].birthday is None:
        return f"Doesn't have '{name.capitalize()}' birthday info"
    data = contacts[name].birthday.value
    if name in contacts:
        if data:
            days = Record.day_to_birthday(data)
            return f"To {name.capitalize()}'s birthday left {days} days!"
        else:
            return f"Doesn't have '{name.capitalize()}' birthday info"
    else:
        return f"Contact with name '{name.capitalize()}' doensn't exist"


def add_bd(name, birthday, *args):
    return contacts[name.lower()].add_birthday(birthday)


handler = {
    "hello": lambda: "Hello! How can I help you?",
    "add": add_contact,
    "change": change_contact,
    "phone": find_contact,
    "show": show_all_contacts,
    "remove": remove_contact,
    "commands": show_all_commands,
    "add_phone": add_phone,
    "remove_phone": remove_phone,
    "change_phone": change_phone,
    "add_bd": add_bd,
    "days_to_bd": show_days_to_birthday
}


def main():
    tprint("AdressBook", font="tarty1")
    while True:

        command = input("Enter command: ").lower().strip().split()

        if command[0] in EXIT_WORDS:
            tprint("Bye!", font="tarty2")
            exit()

        elif command[0] in HELLO_WORDS:
            print(handler["hello"]())

        elif command[0] in handler:
            print(handler[command[0]](*command[1:]))
        else:
            print("Incorrect command.\n(To see all commands enter 'commands')")


if __name__ == "__main__":
    contacts = AdressBook()
    contacts.add_record(Record("liza", "123", "03.05.2005"))
    contacts.add_record(Record("artur", "7878", "29.02.2003"))
    contacts.add_record(Record("karina", "3711323", "15.05.2003"))
    contacts.add_record(Record("vlad", "987987", "15.06.2003"))
    contacts.add_record(Record("olya", "65446", "12.08.2003"))
    contacts.add_record(Record("egor", "16454", "22.04.2003"))
    contacts.add_record(Record("miha", "654987", "23.09.2003"))
    contacts.add_record(Record("nikita", "13213879", "06.06.2003"))

    main()
