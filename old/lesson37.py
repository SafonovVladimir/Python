from classes import Person

person1 = Person('John', 23)
person1.print_name()
person1.print_age()
person2 = Person('Vova', 20)
print('{}, {}'.format(person2.name, person2.age))
print(f"My name is {person2.name} and I'm {person2.age} years old")

