class Person():
    # name = 'John'

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def print_name(self):
        print(f'Hello. My name is {self.name}')

    def print_info(self):
        print(f'My name is {self.name} and I\'m {self.age} years old')

    def print_age(self):
        print(f'I\'m {self.age}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('Wrong age')


class Employee(Person):

    def __init__(self, name, age, company):
        super().__init__(name,age)
        self.company = company

    def more_info(self):
        print(f'{self.name} works in {self.company}')
