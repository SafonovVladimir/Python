class Person():
    # name = 'John'

    def __init__(self, name):
        self.name = name
        self.__age = 20

    def print_name(self):
        print(f'Hello. My name is {self.name}')

    def print_age(self):
        print(f"I'm {self.__age}")

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value in range (1, 101):
            self.__age = value
        else:
            print('Wrong age')