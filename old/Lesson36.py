class A:
    property1 = 'Property1'
    property2 = 'Property2'
    name = 'guest'

    def say_hello(self, name=''):
        if name:
            return 'Hello, ' + name
        else:
            return 'Hi, ' + self.name


a = A()
b = A()

a.property1 = 'Property3'
a.property2 = 'Property4'

print(a.say_hello('John'))
print(b.say_hello())
# print(a.property1)
# print(a.property2)
