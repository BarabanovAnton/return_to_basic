# class A:
#     property1 = 'Property 1'
#     property2 = 'Property 2'
#     name = 'guest'
#
#     def say_hi(self, name=''):
#         if name:
#             return f'Hi, {name}!'
#         else:
#             return f'Hello, {self.name}!'
#
# a = A()
# print(a.property1)
# print(a.say_hi())

from classes import Person
# import classes
person1 = Person('John')
# print(person1.get_age())
# person1.set_age(99)
print(person1.age)
person1.age = 35
person1.print_info()

