# test_commit
# test = 21
# print(test)
#
# my_true = True
# my_false = False

# str() int() float() bool()
# x = 5.2
# print(x, type(x))
# x = bool(x)
# print(x, type(x))

# words = 'Hello \nworld!'
# print(words)
# verse = '''\
# asas
# asasad
# fsafsafsfa\
# '''
# print(verse)

# s = r'C:\d\new.txt' #сырая строка
# print(s)

# s = 'Hello world!'
# print(s[0])
# print(s[-1])

# print(s[6:])
# print(s[::-1])

# s = 'Hello world'
# print(len(s))
# print(s.capitalize())
# print(s.center(20))
# print(s.count('l', 0, 3))
# print(s.find('l'))
# print(s.replace('l', 't'))
# print(s.split())

# name = 'John'
# age = 30

# print('My name is' + name + '. I\'m ' + str(age))
# print('My name is %(name)s. I\'m %(age)d' %{'name': name, 'age': age})
# print('My name is %s. I\'m %d' %(name, age))

# format
# print('My name is {0}. I\'m {1}'.format(name, age))

# f-strings
# print(f'My name is {name}. I\'m {age}.')

# x = 1
# if x == 0:
#     print('Coci zhopy')
# else:
#     print('Sam sosi')

# age = int(input('Сколько Вам лет? '))
#
# if age >= 18:
#     print('Добро пожаловать!')
# else:
#     print(f'Вам ещё рано! Вы ввели, что вам {age} лет. Вам ещё нужно подождать {18 - age} года.')

# while stmt:
#     do...

# i = 1
# while i <= 10:
#     print(i, end=' ')
#     i += 1

# s = 'Hello world'
# for l in s:
#     if l == ' ':
#         continue                      #Переход на следующую итерацию
#     print(f'"{l}"', end='  ')

# for i in 'Hello world':
#     if i == ' ':
#         break
#     print(i, end=' ')
# else:
#     print('\nNo spaces')

# age = 1900
# while age <= 2019:
#     print(age, end=' ')
#     age += 1
# else:
#     print('Done')

# l = [1, 2, 3, 4, 'lol', [123, 321]]
# print(l)
# l1 = ['hello']
# l2 = list('hello')
# l3 = list((1, 2, 3))
# l4 = [i for i in 'hello']
# l5 = [i for i in 'hello world' if i != ' ']
# l5 = [i for i in 'hello world' if i not in ['a', 'e', 'i', 'o', ' ']]
# print(l1, l2, l3, l4, l5, sep='\n')

# for i in range(1, 10):
#     for j in range(2, 11):
#         print(f'{i} * {j} = {i*j}\t', end=' ')
#     print('')
# else:
#     print('Well done')

# l = [1, 2, 3, 4, 'lol', [123, 321]]
# names = ['Ivanov', 'Petrov', 'Sidorov']
# l[2] = 'lol'


# l.append('new')
# # l.extend(names)
# l += names
# # l.remove('lol')
# # el = l.pop(2)
# l3 = ['hello', 'hi', 'privet', 'aaaaaaaaa']
# # l3.sort()
# print(l, l3, sep='\n')

# x = 10
# print(x, id(x))
# x = 20
# print(x, id(x))

# s = 'qwerty'
# print(s, id(s))
# s += 'qaz'
# print(s, id(s))

# l = [1, 2, 'lol']
# print(l, id(l))
# l.append(5)
# print(l, id(l))

# x = 10
# y = x
# print(x, id(x))
# print(y, id(y))


# l1 = [2, 3, 4]
# l2 = l1.copy()
# print(l1, id(l1))
# print(l2, id(l2))

# x = 10
# print(x)
# del x
# print(x)

# lis = [1, 2, 3]
# sum = 0
# for i in lis:
#     sum = sum + i**2
# print(sum)

# time = 11.8
# litres = (time * 0.5) // 1
# print(int(litres))

# s = 'Hello world'
# if ' ' in s:
#     print(s.upper())
# else:
#     print(s.lower())