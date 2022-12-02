import functools
from art import tprint
from entities import AddressBook, Record
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
    result = [f"{'NAME': ^17} {'BIRTHDAY': ^14} {'PHONES': ^13}"]
    for key, rec in contacts.items():
        key = key[:8] + '...' if len(key) > 8 else key
        phones = ', '.join([phone.value for phone in rec.phones])
        bd = rec.birthday.value if rec.birthday else '-'
        result.append(f"[+] {key.capitalize(): <12} | {bd: ^12} | {phones}")
    return '\n'.join(result)


@input_error
def show_n_contacts(N, *args):
    """Func which shows N contacts"""
    result = [f"{'NAME': ^17} {'BIRTHDAY': ^14} {'PHONES': ^13}"]
    for item in contacts.iterator(int(N)):
        key, rec = item[0], item[1]
        key = key[:8] + '...' if len(key) > 8 else key
        phones = ', '.join([phone.value for phone in rec.phones])
        bd = rec.birthday.value if rec.birthday else '-'
        result.append(f"[+] {key.capitalize(): <12} | {bd: ^12} | {phones}")
    if len(result) == 1:
        return f"No more contacts left!"
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


@input_error
def show_days_to_birthday(name, *args):
    name = name.lower()
    if contacts[name].birthday is None:
        return f"Doesn't have '{name.capitalize()}' birthday info"
    data = contacts[name].birthday.value
    if name in contacts:
        if data:
            days = Record.day_to_birthday(data)
            return f"To {name.capitalize()}'s birthday left {days} days!"
        return f"Doesn't have '{name.capitalize()}' birthday info"
    return f"Contact with name '{name.capitalize()}' doesn't exist"


@input_error
def add_birthday(name, birthday, *args):
    return contacts[name.lower()].add_birthday(birthday)


handler = {
    "hello": lambda: "Hello! How can I help you?",
    "add": add_contact,
    "change": change_contact,
    "phone": find_contact,
    "show_all": show_all_contacts,
    "show": show_n_contacts,
    "remove": remove_contact,
    "commands": show_all_commands,
    "add_phone": add_phone,
    "remove_phone": remove_phone,
    "change_phone": change_phone,
    "add_birthday": add_birthday,
    "days_to_birthday": show_days_to_birthday
}


def main():
    tprint("Contact book", font="tarty1")
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
    contacts = AddressBook()
    contacts.add_record(Record("liza", "097123123", "03.05.2005"))
    contacts.add_record(Record("artur", "098712354", "29.02.2003"))
    contacts.add_record(Record("olya", "0681231233", "12.08.2003"))
    contacts.add_record(Record("karina", "0681231833"))
    contacts.add_record(Record("vlad", "076145683", "15.06.2003"))
    contacts.add_record(Record("egor", "0681231233", "22.04.2003"))
    contacts.add_record(Record("miha", "06811813"))
    contacts.add_record(Record("nikita", "0684456233", "06.06.2003"))
    contacts.add_record(Record("ekaterinaPetrovna", "09868733", "06.06.2003"))
    contacts.add_record(Record("magazinIgrashok", "09868156843"))

    main()
