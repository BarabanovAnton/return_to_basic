class A:
    property1 = 'Property 1'
    property2 = 'Property 2'
    name = 'guest'

    def say_hi(self, name=''):
        if name:
            return f'Hi, {name}!'
        else:
            return f'Hello, {self.name}!'

a = A()
print(a.property1)
print(a.say_hi())