from classes import Person, Employee

person1 = Person('John', 40)
person1.print_name()
# person1.print_age()

person2 = Person('Vova', 50)
# person2._age = 30
# print(person2.)
print(person1.get_age())
person1.set_age(5)
# print(person1.get_age())
person1.print_age()
# print('{}, {}'.format(person2.name, person2._Person__age))
# print(f"My name is {person2.name} and I'm {person2._Person__age} years old")

employee1 = Employee('Viktor', 25)


