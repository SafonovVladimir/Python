class Person():
    # name = 'John'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(f'Hello. My name is {self.name}')

    def print_age(self):
        print(f"I'm {self.age}")