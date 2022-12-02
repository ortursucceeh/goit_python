from collections import UserDict
from datetime import datetime
import re


class AdressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator():
        pass


class Record:

    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        if birthday is not None:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = None
        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        return f"New phone '{phone}' was added to contact '{self.name.value.capitalize()}'."

    def remove_phone(self, removed_phone):
        for phone in self.phones:
            if phone.value == removed_phone:
                self.phones.remove(phone)
                return f"Phone '{removed_phone}' was removed"

    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.add_phone(new_phone)
                self.phones.remove(phone)
                return f"Phone '{old_phone}' was changed to '{new_phone}'"

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return f"Added birthday to '{self.name.value.capitalize()}'"

    @staticmethod
    def day_to_birthday(birthday):
        if birthday:
            try:
                birth = datetime.strptime(birthday, "%d.%m.%Y")
                today = datetime.today()

                if (today.month == birth.month and today.day >= birth.day or today.month > birth.month):
                    nextBirthdayYear = today.year + 1
                else:
                    nextBirthdayYear = today.year

                nextBirthday = datetime(
                    nextBirthdayYear, birth.month, birth.day)

                return (nextBirthday - today).days
            except:
                return "Wrong date"


class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if isinstance(self, Phone):
            if not new_value.isdigit():
                raise ValueError("Phone must be consists only of digits")
        elif isinstance(self, Name):
            if not new_value.isalpha():
                raise ValueError("Name must be consists only of letters")
        elif isinstance(self, Birthday):
            if not re.match(r"\d{2}\.\d{2}\.\d{4}", new_value):
                raise ValueError("Birthday must be in 'DD.MM.YYYY' format")
        self.__value = new_value


class Name(Field):
    pass


class Phone(Field):
    pass


class Birthday(Field):
    pass
