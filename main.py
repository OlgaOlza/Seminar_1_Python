# # n = 5

# # print (n)
# """
# n = 'текст'

# print (n)


# n = "текст2"

# print (n)

# """

# # value = None
# # a = 123
# # b = 1.23
# # print(a)
# # print(b)
# # value = 1234
#print(value)


# n = "текст"

# print (type (n))

# n = 'текст"текст2"текс3'

# print (n)


# а = 5
# b = 5.89
# с = 'hello'

# print (а ,b,с )

# а = 5
# b = 5.89
# с = 'hello'

# print (f"{а} привет, {b}, {с}" )


# а = 5
# b = 5.89
# с = 'hello'

# print("{} привет, мир".format(а, b, с))

# print('Введите первое число ')

# a = input ()

# b = input('Введите второе число')

# print (a, '+', b, '=', a + b)

# c = 5.89
# print(c)
# print(type(c))
# n = int(c)
# print(n)
# print(type(n))


# bool

# с = 0
# print(с)
# print(type(с))
# n = bool(с)
# print(n)
# print(type(n))


# a = int(input('Введите первое число - '))
# b = int(input('Введите второе число - '))
# print (a, ' + ', b, ' = ', a + b)


# a = (input('Введите первое число - '))
# b = (input('Введите второе число - '))
# print (a, ' + ', b, ' = ', a + b)

# a = 5.5684654
# b = 2.5512677
# print (round(a + b, 2))


# a = 6 > 4
# print(a)

# a = 6 > 4 and 5 > 2
# print(a)

# a = 2 == 2
# print(a)

# a = 2 != 2
# print(a)

# a = 'текст'
# b = 'текст'
# print(a == b)

# a = 10 < 3 < 5 < 10
# print(a)


# username = input('Введите Ваше имя: ')
# if username == 'Маша' :
#     print('Ура, это же МАША!')
# elif username == 'Марина' :
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар' :
#     print('Ильнар - топ')
# else :
#     print('Привет, ', username)

# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa) # 9


# i = 0
# while i < 5:
#     if i == 6:
#         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

# необходимо найти минимальный делитель данного числа
# n = int(input('Введите число: '))
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное
# # на 2
#         print(n)
#         flag = False
#     i += 1

# a = 'qwerty'

# print(a[3])

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "+"
#         print(line)

# text = 'съешь ещё этих мягких французских булок'
# print(len(text))
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

#  Лекция 2 
 
#  Списки

# # list_1 = []
# # list_1 = list()
# # # print(list_1)
 
# list_1 = [1, 2, 3, 6] 
# # print(*list_1)

# # for i in list_1:
# #     print(i)
    
# # print(len(list_1))

# print(list_1[2])

# print(list_1[-1])


# list_1 = [1, 3, 5]
# print(list_1)

# list_1.append(8)
# print(list_1)

# list = []
# for i in range(5):
#     list.append(i)
#     print(list)
    
    # Удаление последнего значения 
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]
# print(list_1.pop()) # -1
# print(list_1)

# Удаление конкретного элемента 

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]
    
    
    # Добавление элемента на нужную позицию
    
# list1 = [12, 7, -1, 21, 0]
# print(list1.insert(2, 11))
# print(list1) # [12, 7, 11, -1, 21, 0]


# # ● Отрицательное число в индексе — счёт с конца списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]
    

# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))

# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))


# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# for e in t:
#     print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять
# # кортеж)

# d = {}
# в = dict()
# print(d)

# d['q'] = 'qwerrty'
# print(d)

# d['w'] = 'werrty'
# print(d['q'])

# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←

# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться

# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'

# # del dictionary['left'] # удаление элемента

# # for item in dictionary: # for (k,v) in dictionary.items():
# #     print('{}: {}'.format(item, dictionary[item]))
# # # up: ↑
# # # down: ↓
# # # right: →
    
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()
    
    
#     a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}


