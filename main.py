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

text = 'съешь ещё этих мягких французских булок'
print(len(text))
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

 