import json
from person_phone import Person


class Book:
    def __init__(self, filepath):
        with open(filepath) as file:
            self.json_data = json.load(file)
        self.person_list = []
        for data in self.json_data:
            self.person_list.append(Person(**data))

    def display(self):
        for data in self.person_list:
            print(f"{data.Name} \t {data.PhoneNumber}")

    def add_entry(self):
        while True:
            is_present, name = self.validate()
            if is_present:
                print(f"{name.Name} Already Exist!!")
                break
            phonenumber = int(input("Enter Phone Number:"))
            person = Person(name, phonenumber)
            self.person_list.append(person)
            return

    def delete_entry(self):
        while True:
            is_present, person = self.validate()
            if is_present:
                self.person_list.remove(person)
                self.display()
                return
            print(f"{person} is not present")

    def display_one(self, name):
        for data in self.person_list:
            if data.Name == name:
                print(f"{data.Name} \t {data.PhoneNumber}")
                return
        print(f"{name} is not present")

    def validate(self):
        is_present = False
        name = input("Enter Name:")
        for data in self.person_list:
            if data.Name == name:
                is_present = True
                person = data
                return is_present, person
        return is_present, name

    def update_entry(self):
        while True:
            is_present, person = self.validate()
            if is_present:
                option = int(input("What you want to update:\n1.Name\n2.Phone Number\n"))
                if option == 1:
                    new_name = input("Enter new Name:")
                    phonenumber = person.PhoneNumber
                    self.person_list.remove(person)
                    temp_person = Person(new_name, phonenumber)
                    self.person_list.append(temp_person)
                    self.display_one(new_name)
                    return
                if option == 2:
                    new_phone = int(input("Enter New Phone Number:"))
                    name = person.Name
                    self.person_list.remove(person)
                    temp_person = Person(name, new_phone)
                    self.person_list.append(temp_person)
                    self.display_one(name)
                    return
            print(f"{person} is not Present")
