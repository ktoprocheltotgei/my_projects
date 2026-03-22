"""📝📝📝                                          делает шахматную доску с помощью ткинтер
💻💻💻
from tkinter import *
p = Tk()
l = Canvas(p, width = 320, height = 320, background = 'white')
l.pack()
a=b=0
c=d=40
for i in range(1,5):
    for i in range(1,4):
        l.create_rectangle(a,b,c,d, fill ='black')
        a +=80
        c +=80
        l.create_rectangle(a, b, c, d, fill='black')
    a -=200
    b +=40
    c -=200
    d +=40
    for i in range(1,4):
        l.create_rectangle(a, b, c, d, fill='black')
        a +=80
        c +=80
        l.create_rectangle(a, b, c, d, fill='black')
    a -=280
    b +=40
    c -=280
    d +=40
mainloop()
"""
'''  📝📝📝                неудачная попытка кода 5букв(позже заменил это двумя строчками):
from images import vse_slova
o = vse_slova
j = 0
v = o.replace(' ', '')
g = len(v)
r = g//5
a = str(input())
for i in range(0,50):
    for i in range(r):
        if a != o.split()[j]:
            j +=1
            if j==r:
                a = str(input('введите существительное из пяти букв'))
                j =0
        elif a != o.split()[j]:
            a = str(input('введите существительное из пяти букв'))
            j = 0
'''
'''   📝📝📝                        то, чем заменил верхнюю попытку
💻💻💻
a = str(input())
while a not in vse_slova:
    a = str(input('введите существующее слово: '))
'''
''' 📝📝📝                                                задачи ОГЭ(и не только):
💻💻💻
n = int(input('количество: '))
g = 0
men = 0
maks = 300
for i in range(0, n):
    a = int(input())
    if a >= 1 and a <= 300:
        if a <= 30:
            g += 1
        if maks >=a:
            maks =a
        if men<=a:
            men =a
d = maks - men
print(-d)
print(g)
'''
'''
a = int(input())
b = 0
c =0
while a != 0 and a>=10 and a <100 and c<=1000:
    c+=1
    if a %8 == 0:
        b +=a
    else:
        b +=0
    a = int(input())
print(b)
'''
'''
from math import ceil
 2^i>=M   M(кол-во символов) 
 2: i(кол-во бит на кодирование одного символа)
 3: надо i умножить на количество символов'''
'''m = 13
i = 4
c = i*18 #в битах
d = c/8 + 55 #на одного человека в байтах
c = ceil((d*64)/1024)
print(c)
'''
'''
for a in range(1000, 10000):
    b1 = a%10
    b2 = (a//10)%10
    b3 = (a//100)%10
    b4 = (a//1000)%10
    c1 = b1+b2
    c2 = b3+b2
    c3 = b3 +b4
    d = [c1, c2, c3]
    d.remove(min(d))
    v = max(d)
    v1 = min(d)
    s = str(v1) + str(v)
    if s =='1215':
        print(a)
'''
'''
c = 0
for i in range(105105, 1000000):
    b = str(i)
    b1 = b[0]
    b2 = b[1]
    a = b1+b2
    a1 = (i//10)%10
    a2 = i%10
    a3 = str(a1) + str(a2)
    if i%117==0 and a=='99' and a3 =='88':
        c +=1
print(c)'''
'''for i in range(990054, 9900089):
    i1 = str(i)
    if i1[:2] =='99' and i1[-2:]=='88' and i%117==0:
        print(i, i//117)
'''
'''
count = 0
n = 3*3125**8+2*625**7-4*625**6+3*125**5-2*25**4-2024
b = 0
c = 0
h = ''
while n > 0:
    if n%25==0:
        count += 1
    c = n%25
    b =c
    n = n // 25
    c = n
    h +=str(b)
print(h[::-1])
print(count)
'''
'''
count = 0
n = 3*3125**8+2*625**7-4*625**6+3*125**5-2*25**4-2024
b = 0
c = 0
h = ''
while n > 0:
    if n%25==0:
        count += 1
    c = n%25
    b =c
    n = n // 25
    c = n
    h +=str(b)
print(h[::-1])
print(count)
'''
'''
a = 0
o = 0
for i in range(174457, 174506):
    c = 0
    for b in range(2, 174505):
        if i%b==0:
            c +=1
            if c==1:
                a = b
            elif c==2:
                o = b
    if c==3:
        a1 = max(o, a)
        a2 = min(o, a)
        print(i, a2, a1)
'''
'''
for i in range(33333, 55556):
    c1 = 0
    d = str(i)
    for b in range(len(d)):
        c = int(d[b])
        c1 +=c
    if c1>35:
        print(i)
'''
'''def pp(n):
    d1 = []
    for d in range(1, n+1):
        if n%d==0:
            d1.append(d)
    return sorted(d1)
for n in range(174457, 174506):
    if len(pp(n))==4:
        print(n, pp(n)[1], pp(n)[2])
'''
'''   📝📝📝                                       проверяет нетривиальные делители:
💻💻💻
from math import ceil
def pp(n):
    d1 = []
    for d in range(1,n+1):
        if n%d==0:
            d1.append(d)
    return sorted(d1)
st = ceil(300000000**0.25)
en = int(500000000**0.25)
for n in range(st, en+1):
    if len(pp(n))==2 :
        print(n**4, n, n**2,n**4//n)
'''
'''                                         делал я и чуть чуть учебник(ответ 8):
a = '192.168.32.160'
m = '255.255.255.240'
c1 = 0
c = ''
for i in a.split('.'):
    a1 = bin(int(i))
    c+=str(a1)+'.'
c = c.rstrip('.')
c = c.replace('0b', '')
c2 = ''
for i in m.split('.'):
    a1 = bin(int(i))
    c2+=str(a1)+'.'
c2 = c2.rstrip('.')
c2 = c2.replace('0b', '')
print('IP:  ',c, len(c))
print('Mask:',c2, len(c2))
def pg(s):
    ip = 0
    for c in s.split('.'):
        ip = ip*256 + int(c)
    return ip
print('')
a1 = int(pg(a))
m1 = int(pg(m))
for i in range(16):
    if bin(a1).count('1')%2==0:
        print( a1)
        c1+=1
    a1 += 1
print(c1)
'''
'''                                     делали вместе(ответ 7)
a = '192.168.32.160'
c = ''
for i in a.split('.'):
    a1 = bin(int(i))
    c+=str(a1)+'.'
c = c.rstrip('.')
c = c.replace('0b', '')
a2 = '255.255.255.240'
c2 = ''
for i in a2.split('.'):
    a1 = bin(int(i))
    c2+=str(a1)+'.'
c2 = c2.rstrip('.')
c2 = c2.replace('0b', '')
print('IP:  ',c, len(c))
print('Mask:',c2, len(c2))
ip = (192<<24) + (168<<16) + (32<<8) + 160
print(ip)
q = 0
temp_ip = ip
for i in range(16):
    temp_ip = temp_ip + 1
    if bin(temp_ip)[2:].count('1') %2 ==0:
        print('podhodit:', temp_ip)
        q = q+1
print(q)
'''
'''                                                      задание №5 на 46 странице
from math import ceil
def pp(n):
    d1 = []
    for d in range(1,n+1):
        if n%d==0:
            d1.append(d)
    return sorted(d1)
st = ceil(100000000**0.5)
en = int(900000000**0.5)
for n in range(st, en+1):
    if len(pp(n))==4 and pp(n)[1]**2==pp(n)[2]:
        print(n**2, n**2//pp(n)[1])
'''
'''                                            задание №6 тоже 46 стр
a = '193.124.85.64'
m = '255.255.255.192'
c1 = 0
c = ''
for i in a.split('.'):
    a1 = bin(int(i))
    c+=str(a1)+'.'
c = c.rstrip('.')
c = c.replace('0b', '')
c2 = ''
for i in m.split('.'):
    a1 = bin(int(i))
    c2+=str(a1)+'.'
c2 = c2.rstrip('.')
c2 = c2.replace('0b', '')
print('IP:  ',c, len(c))
print('Mask:',c2, len(c2))
def pg(s):
    ip = 0
    for c in s.split('.'):
        ip = ip*256 + int(c)
    return ip
def jj(n):
    return bin(n).lstrip('0b')
print('')
a1 = bin(int(pg(a))).lstrip('0b')
for i in range(64):
    b = str(a1)
    if b.count('1')>b.count('0'):
        c1+=1
    print(a1, a1.count('1'), a1.count('0'))
    a1 = jj(int(a1, 2)+1)
print(c1)
'''
''' 📝📝📝                                        функция, которая переводит в любую систему счисления:
💻💻💻
def pe(n, n1):
    c = ''
    c1 = ''
    if n1 ==8:
        c = oct(n).lstrip('o0')
    elif n1==16:
        c = hex(n).lstrip('x0')
    elif n1 ==2:
        c = bin(n).lstrip('b0')
    elif n1==1:
        print('какая единичная система?')
    else:
        if n1<=n:
            while n!=0:
                c +=str(n%n1)
                n //=n1
        else:
            while n!=0:
                if n%n1 in [10, 11, 12, 13, 14, 15, 16]:
                    if n%n1==10:
                        c +='A'
                    if n%n1==11:
                        c +='B'
                    if n%n1==12:
                        c +='C'
                    if n%n1==13:
                        c +='D'
                    if n%n1==14:
                        c +='E'
                    if n%n1==15:
                        c +='F'
                    if n%n1==16:
                        c +='G'
                    n //=n1
                else:
                    c +=str(n%n1)
                    n //=n1
    return c1.join(reversed(c))
'''
'''
from math import ceil
def pp(n):
    d1 = []
    n = int(n)
    for d in range(1,n+1):
        if n%d==0:
            d1.append(d)
    return sorted(d1)
st = ceil(10000/11)
en = int(99999/11)
n = round(1234)
print(pp(n), len(pp(n)), n)
for n in range(st, en+1):
    if len(pp(n))==66:
        print(n**2, n)
print(pp(66), len(pp(66)))
print(pp(6), len(pp(6)))
'''
''' 📝📝📝                             определяет, сколько раз числа меняли свой знак(+ или -)
💻💻💻
a = 1
c, c1 = 0,0
while a!=0:
    a = int(input())
    while a>0:
        a = int(input())
        if a==0:
            break
        if a<0:
            c +=1
    while a<0:
        a = int(input())
        if a==0:
            break
        if a>0:
            c +=1
print(c)
'''
'''📝📝📝                              пишет, какой последовательностью является последовательность
💻💻💻
f = int(input('кол-во чисел '))
c, c1 = 0, -1
b = 0
a = 0
for i in range(f):
    b = a
    a = int(input())
    if a>b:
        c += 1
    elif b>a:
        c1 -= 1
if c==f:
    print('возрастающая')
elif c1==-f:
    print('убывающая')
else:
    print('это не последовательность')
'''
'''  📝📝📝                             находит второе максимальное число в последовательности
💻💻💻
f = int(input('кол-во чисел '))
c = list()
for i in range(f):
    a = int(input())
    c.append(str(a))
c.remove(max(c))
print(max(c))
'''
''' 📝📝📝                               находит максимальную сумму чисел в последовательности
💻💻💻
f = int(input('кол-во чисел '))
c = list()
for i in range(f):
    a = int(input())
    c.append(str(a))
c1 = max(c)
c.remove(max(c))
print(int(c1)+int(max(c)))
'''
'''
c = 0
i =0
from math import ceil
def pp(n):
    d1 = []
    for d in range(2,n):
        if n%d==0:
            d1.append(d)
    return sorted(d1)
while c<64:
    i +=1
    c +=i
    print(c, len(pp(c)))
'''
'''  📝📝📝                                                   заменяет А на Б и Б на А
💻💻💻
a = 'A0ABBABA41BA'
print(''.join([i.replace('A', 'B') if i=='A' else 'A' for i in a]))
def pe(b):
    c = ''
    for i in b:
        if i=='B':
            c+='A'
        elif i=='A':
            c+='B'
        else:
            c+=i
    return c
print(pe(a))
'''
''' 📝📝📝                                        проверяет верность номера телефона
💻💻💻
a = input('введите номер: ')
if (a[0]=='8' and len(a)==11 and a.isdigit()==True) or (a[:2]=='+7' and len(a)==12 and a[1:].isdigit()==True):
    print('номер верен')
else:
    print('номер неверен')
'''
''' 📝📝📝                                     заменяет максимальное число на минимальное и наоборот
💻💻💻
a = int(input('кол-во: '))
d = list()
for i in range(a):
    b = int(input())
    d.append(b)
c = d.index(max(d))
c1 = d.index(min(d))
d[c], d[c1] = d[c1], d[c]
print(d)
'''
'''📝📝📝                                 вводится день, месяц и год и проверяется, кто старше
💻💻💻
a = int(input())
a1 = int(input())
a2 = int(input())
b = int(input())
b1 = int(input())
b2 = int(input())
if a2<b2:
    print('первый старше')
elif b2==a2:
    if a1<b1:
        print('первый старше')
    elif a1==b1:
        if a<b:
            print('первый старше')
        else:
            print('второй старше')
    else:
        print('второй старше')
else:
    print('второй старше')
'''
''' 📝📝📝                                                   находит в строке максимальную сумму цифр в одну строчку
💻💻💻
a = '123 abc 65 abc 1000 hello 91'
print(max(filter(str.isdigit, a.split()), key=lambda x: sum(int(i) for i in x)))
'''
''' 📝📝📝                                                 изменяет функцию, которая суммирует все аргументы на функцию, которая находит среднее арифмитическое
💻💻💻
def ya(test):
    def gay(*args):
        return test(sum(args))/test(len(args))
    return gay
@ya
def get_sum(*args):
    return sum(args)
print(get_sum(1, 2, 3, 4, 5, 6, 7))
'''
''' 📝📝📝                                               Напишите функцию trip_list(*args), которая получает произвольное число аргументов
строк — города посещенные во время путешествия в порядке их посещения. Города
могут повторяться. Функция должна возвращать список городов отсортированный по
алфавиту без повторений.
💻💻💻
def ger(*args):
    return list(sorted(set(args)))
print(ger('Чебоксары', 'Москва', 'Чебоксары', 'Анапа'))
'''
''' 📝📝📝                                                 Напишите программу, которая сортирует список чисел по уменьшению количества
цифр, если количество цифр совпадает, по значению по возрастанию.
Отсортированные числа следует вывести на одной строке через пробел. Используй
функцию sorted() или метод sort() и анонимную функцию в качестве ключа сортировки.
💻💻💻
def nepridum(args):
    return ' '.join(sorted(args, key=lambda x: (-len(x), int(x))))
a = '65 56 1 3 2 242 323 252'.split()
print(nepridum(a))
'''
'''📝📝📝                                                Напишите функции для регистрации и авторизации пользователя: registration(user,
password) и authorization(user, password).
Функция registration() добавляет пользователя и ничего не выводит. Если при
регистрации пользователя логин уже был зарегистрирован ранее, то это значит, что
для данного пользователя необходимо обновить пароль.
Функция authorization() выводит:
Python
Unset
● «Доступ разрешен», если пара пользователь пароль верная
● «Неверный пароль», если пароль не верный
● «Пользователь не найден», если нет такого пользователя.
💻💻💻
def log(l, p):
    global d
    d = {l: p}
    pass
def avto(n, k):
    if d == {n: k}:
        print('вход разрешен')
    else:
        if d.keys() != {n: k}.keys():
            print('пользователь не найден')
        elif d.values() != {n: k}.values():
            print('неверный пароль')
log('vanya', '12345678')
avto('vanya', '12345678')
avto('vanya', '1234')
avto('vasya', '12345678')
log('dmitri', '368')
avto('dmitri', '368')
'''
'''   📝📝📝                                                                  Напишите программу, которая по номеру билета определяет, является ли билет
счастливым. Билет называется счастливым, если сумма цифр в его левой половине
равна сумме цифр в правой. Номер билета состоит из шести цифр.
Входные данные:
Вводится одно целое шестизначное число.
Выходные данные:
Выводится одна строка «Счастливый» или «Обычный».
Пример ввода:
123006
Пример вывода:
Счастливый
💻💻💻
a = 123456
b = 234432
c = [i for i in str(a)]
def nomer(a):
    c = list(map(int, [i for i in str(a)]))
    if sum(c[:3])==sum(c[3:]):
        return True
    else:
        return False
print(nomer(b))
'''
'''  📝📝📝                                                                     Напишите программу, которая будет сокращать дробь.
💻💻💻
a = 10
b = 15
def nod(a, b):
    while a!=0 and b!=0:
        if a>b:
            a = a%b
        else:
            b = b%a
    return a+b
print(a//nod(a, b), b//nod(a,b), nod(a,b))
'''
'''  📝📝📝                                                                         Напишите программу для вывода чисел от 1, 2, 3 и так далее лесенкой. На первой
ступени должно быть одно число, на второй – два числа, на третьей три числа и так
далее.
Входные данные:
Вводится одно целое число n.
Выходные данные:
Выводится n строк - на каждой строке числа без разделителей.
💻💻💻
a = 5
d = list()
c = 1
for i in range(a):
    i+=1
    d.clear()
    while len(d)!=i:
        d.append(c)
        c+=1
    print(int(''.join(map(str, d))))
'''
'''  📝📝📝                                                                  Напишите программу, которая будет проверять валидность адреса электронной почты
и будет продолжать запрашивать адрес до тех пор, пока не будет введён валидный
адрес. Программа должна выводить:
● «Адрес электронной почты введен верно», если в строке есть символы «@» и
«.».
● «Отсутствует @», если нет соответствующего символа.
● «Отсутствует .», если нет соответствующего символа.
● «Отсутствует @ и .», если нет соответствующих символов.
💻💻💻
def prov(a):
    if '@' not in a and '.' not in a:
        return 2
    elif '@' not in a:
        return 0
    elif '.' not in a:
        return 1
    else:
        return 3
b = str(input())
while prov(b)!=3:
    if prov(b)==0:
        print('нету @')
        b = str(input())
    if prov(b)==1:
        print('нету .')
        b = str(input())
    if prov(b)==2:
        print('нету @ и .')
        b = str(input())
print('адрес введен верно')
'''
'''  📝📝📝                                                      Напишите функцию filter_numbers(*args, type), получающую произвольное
число позиционных аргументов: целые числа и один именованный аргумент type,
который может быть равен значению 'odd' или 'even'. Если значение аргумента
type равно 'odd', то функция возвращает список нечетных чисел, если 'even' —
четных.
💻💻💻
def filters(*args, **type):
    if type.get('type')=='even':
        return list(filter(lambda a: a%2==0, args))
    elif type.get('type')=='odd':
        return list(filter(lambda a: a%2!=0, args))
print(filters(1, 2, 3, 4, type='odd'))
'''
'''  📝📝📝                                                        Напишите программу, которая сортирует список чисел по уменьшению количества
цифр, если количество цифр совпадает, по значению по возрастанию.
Отсортированные числа следует вывести на одной строке через пробел
💻💻💻
a = '65 56 1 3 2 242 323 252'
print(' '.join(sorted(a.split(), key=lambda x: (-len(x), x))))
'''
'''  📝📝📝                                                  Напишите программу для вычисления степени числа с помощью рекурсии без
использования циклов.
Входные данные:
Вводится два целых числа через пробел — основание и степень.
Выходные данные:
Выводится одно целое число.
Пример ввода:
2 5
Пример вывода:
32
💻💻💻
def stepa(ch, st):
    if st==0:
        return 1
    return ch * stepa(ch, st-1)
print(stepa(2, 5))
'''
''' 📝📝📝                                                           Напишите программу, в которой будет создан класс Time. Реализуйте в нем
следующие методы:
● __init__(h, m) — добавляет объекту атрибуты h и m (часы и минуты);
● __str__() — возвращает текстовое представление объекта в формате: h:m.
Определите методы арифметических операций:
● сложение self + other — возвращает новый объект класса Time;
Python
● вычитание self - other — возвращает новый объект класса Time. Если разность
будет отрицательной, то считать ее равной 0 (h и m равны 0);
● умножение на число self * n — возвращает новый объект класса Time
💻💻💻
class time:
    def __init__(self, h, m):
        self.h = h
        self.m = m
    def __str__(self):
        return f'{self.h}:{self.m}'
    def __sub__(self, other):
        return divmod(self.h * 60 + self.m - other.h *60 - other.m, 60)
    def __add__(self, other):
        return divmod(self.h * 60 + self.m + other.h *60 + other.m, 60)
    def __mul__(self, other):
        return divmod((self.h * 60 + self.m) * other, 60)
a = time(2, 30)
b = time(3, 45)
print(a * 4)
'''
'''  📝📝📝                                                                         Напишите программу, в которой создайте класс Date. Реализуйте в классе следующие
методы:
● __init__(d, m, y) — добавляет объекту атрибуты d, m, y (день, месяц и год);
● __str__() — возвращает текстовое представление объекта в формате: d.m.y;
● методы сравнения.
Входные данные:
Вводится три строки — на первой и второй строке вводятся даты в формате d.m.y, на
третьей строке вводится одна из операций сравнения ==, !=, >, >=, <, <=.
Выходные данные:
Выводится True или False — результат сравнения объектов
💻💻💻
from functools import total_ordering
@total_ordering
class date:
    def __init__(self, d, m, y):
        self.d = int(d)
        self.m = int(m)
        self.y = int(y)
    def __eq__(self, other):
        return (self.d, self.m, self.y)==(other.d, other.m, other.y)
    def __gt__(self, object):
        if self.y>object.y:
            return True
        elif self.y==object.y and self.m> object.m:
            return True
        elif self.m == object.m and self.d > object.d:
            return True
        else:
            return False

a = input().split('.')
b = input().split('.')
a = date(a[0], a[1], a[2])
b = date(b[0], b[1], b[2])
print(a < b)
'''
''' 📝📝📝                                                                                 Напишите программу, в которой создайте класс Student. Реализуйте в классе
следующие методы:
● __init__(name, course) — добавляет объекту атрибуты name (строка) и course
(целое число от 5 до 11), status со значением 'student'.
● next_course() — увеличивает course на единицу, пока студент не закончит
обучение (11 класс — последний год обучения). Если после вызова метода
next_course, класс становится больше 11, то значение атрибута course
устанавливается на None, a status на строку 'graduate'.
● deduction() — изменяет значение атрибута course на None, a status на строку
'expelled'.
● get_info() — возвращает строку вида Student: {name} ({course}), status: {status},
например, Student: Иванов Иван Иванович (None), status: expelled.
💻💻💻
class Student:
    def __init__(self, n, c):
        self.__c = c
        self.__n = n
        self.__status = 'student'

    def get_info(self):
        return f'{self.__n} ({self.__c}), статус: {self.__status}'

    def deduction(self):
        self.__c = None
        self.__status = 'expelled'
    def next_course(self):
        if self.__c<11:
            self.__c +=1
        else:
            self.__status = 'graduate'
            self.__c = None
student1 = Student('Михайлов Петр', 10)
print(student1.get_info())
student1.next_course()
student1.next_course()
print(student1.get_info())
student2 = Student('Васильев Сергей', 5)
print(student2.get_info())
student2.deduction()
print(student2.get_info())
'''
'''📝📝📝                                                  Напишите программу, в которой создайте класс Person (человек). Реализуйте в классе
следующие методы:
● __init__(name, age) — добавляет объекту атрибуты name (строка), age (целое
число);
● get_name() — возвращает строковое представление объекта в формате:
Человек: {name}, например Человек: Иванов Иван;
● get_age() — возвращает строку в формате Возраст: {age}, например Возраст:
15.
Создайте класс Student (ученик), выполнив наследование от Person. Переопределите
следующие методы:
● __init__(name, age, course) — добавляет объекту атрибуты, как у экземпляра
класса Person, и атрибут course (целое число);
● get_name() — возвращает строковое представление объекта в формате:
Ученик: {name} ({course} класс), например Ученик: Иванов Иван (7 класс).
💻💻💻
class person:
    def __init__(self, n, a):
        self.n  = n
        self.a = a
    def get_name(self):
        return f'ученик: {self.n}'
    def get_age(self):
        return f'Возраст: {self.a}'
class student(person):
    def __init__(self, n, a, c):
        super().__init__(n, a)
        self.c = c
    def get_name(self):
        return f'ученик: {self.n} ({self.c} класс)'
b = student('Иван', 15, 7)
print(b.get_name())
print(b.get_age())
print(person('абвгд', 4).get_name())
'''
''' 📝📝📝                                                     Напишите программу, в которой создай класс Time. Реализуйте в классе следующие
методы:
● __init__(h, m) — добавляет объекту атрибуты h и m — часы и минуты;
● __str__() — возвращает текстовое представление объекта в формате: «h:m».
● методы сравнения.
💻💻💻
from functools import total_ordering
@total_ordering
class dio:
    def __init__(self, h, m):
        self.h = h
        self.m = m
    def __str__(self):
        return f'{self.h}:{self.m}'
    def __eq__(self, other):
        return (self.h,self.m) == (other.h, other.m)
    def __lt__(self, other):
        return (self.h, self.m) < (other.h, other.m)
a = dio(1,0)
b = dio(0, 59)
print(a>b)
'''
'''📝📝📝                                                    Создайте класс Sequence (последовательность). Реализуйте в классе следующие
методы:
● __init__(lst) — принимает один аргумент lst — список элементов
последовательности;
● __str__() — который будет возвращать текстовое представление объекта в
формате: «Последовательность {элементы через запятую и пробел}».
● сложение self + other — возвращает новый объект Sequence, в которой сначала
находятся элементы первой последовательности, затем элементы второй
последовательности, если их не было в первой последовательности в том же
порядке. Например, операция Sequence([1, 1, 2, 4]) + Sequence([3, 4, 5, 1, 6])
должна возвращать Sequence([1, 1, 2, 4, 3, 5, 6]).
💻💻💻
class posl:
    def __init__(self, lst):
        self.lst = lst
    def __str__(self):
        return f'последовательность'
    def __add__(self, other):
        return posl(self.lst + list(filter(lambda x: x not in self.lst, other)))
a = [1,1,2,4]
b = [3,4,5,1,6]
print(posl(a).__add__(b))
'''
'''  📝📝📝                                                                          Напишите программу, в которой создайте класс Product (товар). Реализуй в классе
следующие методы:
● __init__(name, price, amount) — добавляет объекту атрибуты name, price,
amount;
● sale() — продажа, уменьшает количество товара (amount), при этом количество
товара не может быть меньше 0. При продаже товара, у которого значение
количества равно 0, необходимо выводить сообщение «Нет в наличии».
● refund() — возврат товара, увеличивает количество товара (amount);
● get_info() — возвращает строку вида «Товар: {name}, цена: {price}, количество:
{amount}», например, «Товар: футболка, цена: 200, количество: 130».
💻💻💻
class product:
    def __init__(self, n, p, a):
        self.n = n
        self.p = p
        self.a = a
    def sale(self):
        if self.a==0:
            print(f'нет в наличии')
        else:
            self.a -= 1
    def refund(self):
        self.a +=1
    def get_info(self):
        return f'Товар: {self.n}, цена: {self.p}, количество: {self.a}'
product = product('Телефон', 20000, 2)
product.sale()
product.sale()
product.sale()
product.refund()
print(product.get_info())
'''
'''  📝📝📝                                                               Создайте класс Password для хранения и проверки пароля. Инициализатор класса
принимает один параметр — строку с паролем — и выполняет проверку его
корректности. Правильный пароль должен иметь длину не менее восьми символов и
включать хотя бы один знак из набора ?,.!@#$%^&*()<>. Если пароль корректен, то он
сохраняется в атрибут password. В противном случае вызывается одно из собственных
исключений MinLengthPasswordError (не выполнено условие минимальной длины) или
NoSpecialCharactersError (нет символа из набора).
Python
Считайте с клавиатуры одну строку — пароль. Создайте с ним экземпляр класса, если
он корректный, и выведите на экран текст «Пароль: {password}», например, «Пароль:
12345678@. Если пароль некорректный, с помощью вызова исключений
MinLengthPasswordError или NoSpecialCharactersError выведите на экран текст
«Короткий пароль» или «Нет специального символа». Сначала проверяется условие
необходимой длины: если оба условия ложны, то выводится одно сообщение —
«Короткий пароль».
При написании кода программы используйте обработку исключений. Создайте
собственные исключения MinLengthPasswordError и NoSpecialCharactersError.
💻💻💻
class lenerror(Exception):
    pass
class nospecerror(Exception):
    pass
class parol:
    def __init__(self, p):
        if len(p) < 8:
            raise lenerror('не менее 8 символов')
        if set(' ?,.!@#$%^&*()<>') & set(p)==set():
            raise nospecerror('должны быть спец символы')
        else:
            self.p = p
try:
    p = parol(input('пароль: '))
except lenerror as e:
    print(e)
except nospecerror as e:
    print(e)
else:
    print('parolb is ok')
'''
''' 📝📝📝                                                             Скачайте файл numbers.txt, который содержит произвольное количество строк. В
каждой из них есть целые числа, разделенные пробелом. Напишите программу, с
помощью которой найдите сумму всех введенных чисел.
Пример файла numbers.txt:
1 2 3
4 5
6
7 8
9
Python
Python
Python
Ответ:
45
💻💻💻
c = 0
with open('abaldetb.txt', 'r') as f:
    for i in f:
        c += sum(map(int, i.split()))
print(c)
'''
'''   📝📝📝                                                    Дано некоторое число. Проверьте, что цифры этого числа расположены по возрастанию
💻💻💻
a = '12345'
if sorted(a)==list(a) or sorted(a, key=lambda x: -int(x))==list(a):
    print('да')
else:
    print('нет')
'''
'''📝📝📝                                                         Дан список:
[1, '', 2, 3, '', 5]
Удалите из списка все пустые строки.
💻💻💻
a = [1, '', 2, 3, '', 5]
print(list(filter(lambda x: x!='', a)))
'''
'''📝📝📝
[
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]
Выведите в консоль все элементы этого списка
💻💻💻
a = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]
for i in a:
    for g in i:
        print(g)
'''
'''📝📝📝                                                 Дано число. Получите список делителей этого числа.
💻💻💻
a = 1234
b = list()
for i in range(1, a+1):
    if a%i==0:
        b.append(i)
print(b)
'''
'''📝📝📝                                        Найдите сумму элементов этого словаря
💻💻💻
a = dct = {
	1: {
		1: 11,
		2: 12,
		3: 13,
	},
	2: {
		1: 21,
		2: 22,
		3: 23,
	},
	3: {
		1: 24,
		2: 25,
		3: 26,
	},
}
c = 0
for i in a.values():
    for g in i.values():
        c +=g
print(g)
'''
''' 📝📝📝                                       Создайте простейший в мире класс SimplePass. Затем создайте экземпляр класса и выведите на экран его тип.
💻💻💻
class SimpleClass:
    pass
a = SimpleClass
print(type(a))
'''
''' 📝📝📝                                               Определите класс A, включающий:
- строку документирования класса ''Класс A'';
- метод set_a() для установки значения атрибута a;
- метод get_a() для получения значения этого атрибута.
Выведите на экран документацию класса. Затем создайте первый экземпляр класса и при помощи определенных методов установите и 
выведите значение его атрибута a. Далее создайте второй экземпляр класса, после чего также установите и выведите на экран значение атрибута 
a, но уже при помощи прямого доступа к атрибуту по точке.
💻💻💻
class a:
    def __str__(self):
        return 'класс a'
    def set_a(self, a):
        self.a = a
    def get_a(self):
        return self.a
print(a.__dict__)
c = a()
c.set_a(5)
print(c.get_a())
b = a()
b.set_a(10)
print(a.get_a(b))
'''
'''  📝📝📝                                                    Определите класс B, включающий:
- строку документирования класса ''Класс B'';
- конструктор, инициализирующий атрибут данных b создаваемых экземпляров;
- метод get_b() для получения значения этого атрибута.
💻💻💻
class b:
    def __init__(self, b):
        self.b =b
    def get_b(self):
        return self.b
b = b(2)
print(b.get_b())
'''
''' 📝📝📝                                                      Определите класс C, наследующий классы A (задача 13.2) и B (задача 13.3) и включающий:
- строку документирования класса 'Класс C = A + B';
- конструктор, инициализирующий дополнительно атрибуты данных a и c создаваемых экземпляров;
- собственные методы set_b() и set_c() для установки значений соответствующих атрибутов;
- собственный метод get_c() для получения значения атрибута c.
Выведите на экран документацию класса. Затем создайте экземпляр класса obj, после чего при помощи соответствующих методов экземпляра выведите значения его атрибутов a, b и c.
💻💻💻
class a:
    def __str__(self):
        return f'класс a{self.a})'
    def __init__(self, a):
        self.a = a
    def get_a(self):
        return f'A = {self.a}'

class b():
    def __init__(self, b, a):
        super().__init__(a)
        self.b =b
    def str(self):
        return f'класс b({self.b})'
    def get_b(self):
        return f'B = {self.b}'

class c(b, a):
    def __init__(self, a, b, c):
        super().__init__(a,b)
        self.c = c
    def __str__(self):
        return f'класс с({self.c}) = а({self.a}) + b({self.b})'
    def set_b(self, b):
        self.b = b
    def set_c(self,c):
        self.c = c
    def get_c(self):
        return f'C = {self.c}'
c1 = c(10, 15, 20)
print(c1.get_c())
print(c1.get_b())
print(c1.get_a())
c1.set_c(30)
print(c1.get_c())
c1.set_b(25)
print(c1.get_b())
print(c.__mro__)
'''
''' 📝📝📝                                                                 Определите класс D, включающий:
- статический метод stat_print_dict, выводящий на экран словарь атрибутов переданного ему объекта класса;
- метод класса cls_print_dict, выводящий на экран словарь атрибутов своего класса.
💻💻💻
class d:
    c = 0
    e = 1
    @staticmethod
    def stat_dict(**kwargs):
        return kwargs
    @classmethod
    def class_dict(cls):
        return {cls.c: cls.e}
print(d.class_dict(), d.stat_dict(a=23))
'''
''' 📝📝📝                                                            Определите класс E, наследующий класс D (задача 13.5) и включающий единственный 
атрибут данных класса e = 'Класс E'. Создайте экземпляр obj_1 класса D 
и, вызвав оба метода из этого экземпляра, выведите на экран словарь атрибутов класса. 
Затем создайте экземпляр obj_2 класса E и также, вызвав оба метода из этого экземпляра,
 выведите на экран словарь атрибутов этого класса. Объясните результаты.
💻💻💻
class d:
    c = 0
    j = 'le le le'
    @staticmethod
    def stat_dict(**kwargs):
        return kwargs
    @classmethod
    def class_dict(cls):
        return {cls.c: cls.j}
class e(d):
    c = 100
    j = 'попа'
d1 = d()
e1 = e()
print(d1.class_dict(), d1.stat_dict(a=5))
print(e1.class_dict(), e1.stat_dict(a=5))
'''
'''  📝📝📝                                                                                       Определите класс F, наследующий класс A (задача 13.2), включающий:
- конструктор, обновляющий строку документации создаваемых экземпляров на 'Объект класса F';
- расширенный метод set_a() для установки значения атрибута a, который должен дополнительно выводить сообщение 'Атрибут a установлен!'.
💻💻💻
class a:
    def __str__(self):
        return 'класс a'
    def set_a(self, a):
        self.a = a
    def get_a(self):
        return self.a
class f(a):
    def set_a(self, a):
        self.a = a
        print('атрибут а установлен')
    def __str__(self):
        return 'класс f'
f1 = f()
a1 = a()
a1.set_a(5)
f1.set_a(5)
'''
''' 📝📝📝                                                                               Определите класс PiNum, хранящий значение числа Пи и включающий:
- конструктор, инициализирующий текущую точность представления числа Пи создаваемым экземпляром (по умолчанию два знака после запятой);
- переопределяемый магический метод __str__, возвращающий строку с текущим значением числа Пи;
- управляемый атрибут max_pi, хранящий значение числа Пи с максимальной точностью в 13 знаков после запятой и недоступный для изменения или удаления;
- метод set_pi_prec, устанавливающий значение атрибута cur_pi экземпляра для хранения значения числа Пи с текущей точностью (по умолчанию два знака после запятой).
Используя созданный класс, создайте экземпляр числа Пи с точностью в три знака после запятой и выведите его 
строковое представление на экран. Измените точность представления числа до пяти знаков после запятой и выведите 
новое значение на экран. Также выведите значение числа Пи с максимальной точностью.
💻💻💻
class PiNum:
    pi = 3.1415926535897
    cur = 2
    @classmethod
    def __str__(cls):
        return str(cls.pi)[:cls.cur]
    @classmethod
    def set_pi(cls, c):
        cls.cur = c+2
        print(f'установленно знаков после запятой: {c}')
    @classmethod
    def max_pi(cls):
        return cls.pi
p = PiNum()
p.set_pi(3)
print(p)
p.set_pi(5)
print(p)
print(PiNum.max_pi())
'''
'''  📝📝📝                                                                  Определите класс Circle, представляющий окружность и включающий:
- статический метод, переводящий метры в сантиметры или наоборот;
- конструктор, инициализирующий радиус r экземпляра и атрибут pi для хранения числа Пи с точностью в три знака после запятой 
(для получения требуемого значения используйте класс PiNum из предыдущей задачи);
- методы экземпляров для получения длины и площади окружности с точностью в три знака после запятой.
Используя созданный класс, рассчитайте и выведите на экран длину и площадь окружности в сантиметрах, зная что ее радиус равен 2.57 метра.
💻💻💻
class circle:
    def __init__(self, r):
        self.r = r
    def perevod(self):
        self.r *=100
    def get_long(self):
        a = 2* 3.141 *self.r
        if a!=int:
            return '%.3f' % a
        else:
            return a
    def get_square(self):
        a = 3.141*self.r**2
        if a!=int:
            return '%.3f' % a
        else:
            return a
r = circle(2.57)
r.perevod()
print(r.get_long(), r.get_square())
'''
'''  📝📝📝                                                           Определите суперкласс Сотрудник, включающий:
- конструктор, инициализирующий имя работника, его должность (по умолчанию None) и оклад (по умолчанию 0);
- метод экземпляра для повышения оклада на какую-то часть (например, на 0.3, то есть на 30%) с округлением результата до копеек;
- магический метод __str__ для перегрузки строкового представления объекта, который должен выводить данные о работнике в формате 'Атрибут: объект.атрибут' 
по одной записи на каждой строке.
Также определите подкласс Менеджер, наследующий суперкласс Сотрудник и переопределяющий метод повышения оклада таким образом, чтобы он еще больше повышал оклад
💻💻💻
class sotr:
    def __init__(self, n, i, d):
        self.d = d
        self.n, self.i = n, i
    def __str__(self):
        return f'имя: {self.n}, должность: {self.i}, зарплата: {self.d}'
    def povys(self):
        a = self.d* 1.335
        if a!=int:
            self.d ='%.2f' % (self.d* 1.335)
        else:
            self.d = a
        print('запрлата повышена на 30%')
class mened(sotr):
    def povys(self):
        a = self.d * 1.335 * 1.25
        if a!=int:
            self.d = '%.2f' % a
        else:
            self.d = a
        print('зарплата повышена на 30% + надбавка за должность менеджера 25%')
ivan = sotr('Иван', 'Сотрудник', 1700)
print(ivan)
ivan.povys()
print(ivan)
print()
igor = mened('Игорь', 'Менеджер', 3000)
print(igor)
igor.povys()
print(igor)
'''
'''   📝📝📝                                                              Создайте абстрактный класс геометрической фигуры Shape с конструктором, 
принимающим длину стороны и высоту, проведенную к этой стороне. Определите в классе абстрактный метод area(), 
который будет использоваться подклассами для расчета площади соответствующих им геометрических фигур. Далее 
создайте классы Triangle и Rectangle, наследующие суперкласс Shape и реализующие его абстрактный метод под 
свои нужды. Продемонстрируйте использование созданных классов для нахождения площади треугольника и прямоугольника
 по известным значениям длины стороны и высоты, проведенной к этой стороне.
 💻💻💻
 class shape:
    def __init__(self, c, v):
        self.c = c
        self.v = v
    def area(self):
        return self.c*self.v
class rectangle(shape):
    def area(self):
        return self.v*2 * self.c
class triangle(shape):
    def area(self):
        return self.c * self.v /2
    
pryamoygolnik = rectangle(6, 1.5)
print(pryamoygolnik.area())
treygolnik = triangle(6, 3)
print(treygolnik.area())
'''
'''   📝📝📝                                                         Определите класс Counter, реализующий десятичный счетчик, который может увеличивать или уменьшать свое 
значение на единицу в заданном диапазоне, включая границы диапазона. В классе должны быть предусмотрены следующие возможности:
- конструктор для инициализации счетчика значениями по умолчанию (стартовое значение, нижняя и верхняя границы диапазона),
- метод для его инициализации произвольными значениями,
- а также методы для увеличения и уменьшения текущего значения счетчика.
Все методы класса должны принимать только именованные параметры и проверять выход текущего значения счетчика за 
допустимый диапазон. Создайте экземпляр счетчика со значениями по умолчанию и выведите его начальные параметры. 
Далее проверьте его работу циклом в пределах диапазона, увеличивая и выводя на экран его текущее значение от 
минимально возможного до максимального. Затем переустановите счетчик, задав отрицательную нижнюю и положительную
 верхнюю границы, а также установив положительное стартовое значение для отсчета. Опять же, проверьте его работу 
 циклом, уменьшая и выводя на экран его текущее значение от стартового до минимально возможного. Задайте заведомо 
 большее количество итераций циклов в обоих случаях, обеспечив прерывание их работы при попытке выхода счетчика за 
 пределы диапазона.
 💻💻💻
 class deapathonError(Exception):
    pass
class counter:
    def __init__(self, ch, m, m1):
        self.ch = ch
        self.m = m
        self.m1 = m1
    def __str__(self):
        return str(self.ch)
    def plus(self):
        if self.ch<self.m1:
            self.ch += 1
        else:
            raise deapathonError('число достигло максимума')
    def minus(self):
        if self.ch>self.m:
            self.ch -=1
        else:
            raise deapathonError('число достигло минимума')

a = counter(10, 5, 20)
print(a)
while True:
    try:
        a.plus()
        print(a)
    except deapathonError as e:
        print(e)
        break

b = counter(3, -10, 4)
print(b)
while True:
    try:
        b.minus()
        print(b)
    except deapathonError as e:
        print(e)
        break
'''
'''   📝📝📝                                                   сделал простую таблицу с помощью пандаса
import pandas as pd
💻💻💻
df = pd.DataFrame({'цвет': ['оранжевый', 'красный', 'синий'], 'номер': map(lambda x:x*x, [2,3,4])})
print(df)
'''
'''  📝📝📝                                                        делает таблицу с именами и изменяет ее если кому-то меньше 18

import pandas as pd
💻💻💻
file = {'имя': ['Иван','Игорь','Мария'], 'возраст': [16, 30, 25], 'город': ['Москва', 'Омск', 'Казань']}
file['возраст'] = list(i if i>18 else 'несовершенолетний' for i in file['возраст'])
a = pd.DataFrame(file)
print(a)
'''
'''   📝📝📝                                                           Дан двумерный массив размером m x n. Сформируйте новый массив, заменив
положительные элементы единицами, а отрицательные нулями. Выведите оба массива.
💻💻💻
import numpy as np
a = np.array([[-4,-3,2],[1,-23,5]])
print(a)
b = np.array([[0 if i<0 else 1 for i in a[0]], [0 if i<0 else 1 for i in a[1]]])
print(b)
'''
'''  📝📝📝                                                             Дана целая квадратная матрица n-го порядка. Определите, является ли она
магическим квадратом, т.е. такой матрицей, в которой суммы элементов во всех строках и
столбцах одинаковы
💻💻💻
import numpy as np
m,n = '01','34'
while len(m)!=1 or len(n)!=1:
    a = np.random.randint(1,5,(4,4))
    m = set(a.sum(axis=1))
    n = set(a.sum(axis=0))
print('магический кубик: ', a, sep='\n')
'''
'''  📝📝📝                                                     Требуется упорядочить по возрастанию элементы каждой строки матрицы
размером n х m.
💻💻💻
import numpy as np

a = np.random.randint(1,10,(4,10))
c = 0
for i in a:
    if c==0:
        b = np.array(sorted(i, key=lambda x: x))
        c = 1
    else:
        b = np.vstack((b,sorted(i, key=lambda x: x)))
print('было:', a, 'стало:', b, sep='\n')
'''
'''   📝📝📝                                                       Создайте класс «Мебель» с полями «Марка», «Название», «Цена» и методом для
вывода подробной информации о предмете. От класса «Мебель» необходимо
унаследовать класс «Стол» с унаследованными полями класса «Мебель» и новыми полями
«Спинка» (True/False), «Кол-во ножек» и методом для вывода подробной информации.
💻💻💻
class mebelb:
    def __init__(self, m,n,t):
        self.m,self.n,self.t = m,n,t
    def __str__(self):
        return f'марка {self.m}, название {self.n}, цена {self.t}'
class table(mebelb):
    def __init__(self, m,n,t,c,k):
        super().__init__(m,n,t)
        self.c,self.k = c,k
    def __str__(self):
        return f'марка {self.m}, название {self.n}, цена {self.t}, спинка {self.c}, кол-во ножек {self.k}'
a = mebelb('ксяоми', 'диван', 9999999)
print(a)
b = table('я гей', 'стул', 69, True, 52)
print(b)
'''
''' 📝📝📝                                                чтобы если что понять как работает аксис в нампай
💻💻💻
import numpy as np
b = np.array([[[1,2,1],[0,5,1]],[[3,4,5],[10,20,8]]])
print(b, end='\n\n\n')
print(b.max(axis=1))
'''
'''  📝📝📝                                                    читает файл table1, превращает его в таблицу через пандас и еще добавляет новый столбик
💻💻💻
import pandas as pd
file = pd.read_csv('table1.csv')
file['образование'] = ['самое крутое', 'среднее', 'вышее', 'проффесиональное', 'какое-то', 'плохое']
print(file)
'''
''' 📝📝📝                                                         добавляет столбец в таблицу
💻💻💻
df = pd.read_csv('internet Speed 2022.csv')
new_country = pd.DataFrame([{'country': 'Сервера суперселл, когда я не играю', 'broadband': 999.999, 'mobile': 999.999}])
new_list1 = pd.concat([new_country,df])
print(new_list1)
'''
''' 📝📝📝                                                                олимпиадная задача(пишу по памяти)
мишка хотел устроить пикник, из еды у него есть только хлеб, варенье и чай. Он очень принципиальный и хочет, чтобы все продукты лежали по порядку сначала хлеб,
потом варенье и в конце чай. За одну секунду мишка может передвинуть местами только два продукта, каждого из продуктов может быть сколько угодно.
Найдите максимальное число секунд, за которые мишка может поставить по порядку 3, 9, 11 и 13 продуктов. В ответе напишите комбинацию букв (х-хлеб,
в-варенье, ч-чай) и кол-во секунд, за которые можно поставить продукты по порядку. Пример для 3 продуктов: чвх 3
это был ужас как я вообще это решил
💻💻💻
from random import choice
a = ''
b = 'х ч в'
q = dict()
for i in range(100000):
    c = 0
    c1 = 0
    while len(a)<13:
        a += choice(b.split())
        if len(a) == 13 and set(i for i in a) != {'х', 'в', 'ч'}:
            a = ''
    d = [i for i in a]
    for j in range(a.count('х')):
        m = d.index('х')+c1
        c += m - c1
        c1 += 1
        d.remove('х')
    с1 = 0
    for j in range(a.count('в')):
        m = d.index('в')+c1
        c += m - c1
        c1 += 1
        d.remove('в')
    q.update({c:a})
    a = ''

print(max(q.items()))
#9 - чччвххвхх (27)
#11 - чччччввххвх (40)
#13 - ччччччвввхххх (56)
'''
'''📝📝📝                                                                  Из входного потока читаются строки данных с помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))
В формате: id, name, old, salary (записанные через пробел). Например:
1 Сергей 35 120000
2 Федор 23 120000
3 Иван 13 1200
То есть, каждая строка — это элемент списка lst_in.
Необходимо в класс:
class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
добавить два метода:
-select(self, a, b) — возвращает список из элементов списка lst_data в диапазоне [a; b] (включительно) по их индексам (не id, а индексам списка);
 также учтите, что граница b может превышать длину списка.
- **insert(self, data)** — для добавления в список lst_data новых данных из переданного списка строк data.
Каждая запись в списке lst_data должна быть представлена словарем в формате:
{'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}
Например:
{'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}
Примечание:  
В этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с числом полей в коллекции FIELDS.
P. S. Ваша задача только добавить два метода в класс DataBase.
**Sample Input:**
1 Сергей 35 120000
2 Федор 23 120000
3 Иван 13 1200
💻💻💻
 a = int(input('кол-во строк: '))
lst_in = list()
for i in range(a):
    lst_in.append(input())
class DataBase:
    lst_data = []
    fd = ('id', 'name', 'old', 'salary')
    def insert(self, data):
        for i in data:
            self.lst_data.append(dict((zip(self.fd, i.split()))))
        return self.lst_data
    def select(self, a, b):
        return self.lst_data[a:b+1]

print(DataBase().insert(lst_in))
'''
'''📝📝📝                                                         Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:
add(self, eng, rus) для добавления новой связки английского и русского слова (если английское слово уже существует, то новое русское слово добавляется как синоним для 
перевода, например, до идти, ходить, ехать); если связка eng-rus уже существует, то второй раз ее добавлять не нужно, например: add('go', 'идти'), add('go', 'идти");
remove(self, eng) для удаления связки по указанному английскому слову,
translate(self, eng) для перевода с английского на русский (метод должен возвращать список из русских слов, соответствующих переводу английского слова, даже если в 
списке всего одно слово).
Все добавления и удаления связок должны выполняться внутри каждого конкретного объекта классa Translator, т.е. связки хранить локально внутри экземпляров классов класса 
Translator.
Создайте экземпляр tr класса Translator и вызовите метод add для следующих связок:
tree дерево
car-машина
car - автомобиль
leaf-лист
river-peka
gо-идти
go- ехать
gо - ходить
milk - Молоко
Затем методом remove() удалите связку для английского слова саг. С помощью метода translate() переведите слово gо. Результат выведите на экран в виде строки из всех 
русских слов, связанных со словом до
Вывод в формате: идти ехать ходит
💻💻💻
class translator:
    d = dict()
    def add(self,eng,rus):
        if bool(self.d.get(eng))==True:
            self.d.update({eng: f'{self.d.get(eng)} {rus}'})
        else:
            self.d.update({eng:rus})
    def remove(self,eng):
        self.d.pop(eng)
    def translate(self,eng):
        return self.d.get(eng)
tr = translator()
tr.add('tree','дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

print(tr.translate('go'))
print(tr.translate('leaf'))
print(tr.translate('car'))

tr.remove('car')
print(tr.translate('car'))
'''
''' 📝📝📝                                                     Объявите класс CardCheck для проверки корректности информации на пластиковых картах. Этот класс должен иметь
следующие методы:
check_card_number(number) проверяет строку с номером карты и возвращает булево значение True, если номер в верном формате и False - в противном случае. Формат номера следующий:
XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
check_name(name) проверяет строку name с именем пользователя карты. Возвращает булево значение True, если имя записано верно и False - в противном случае.
Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами. Например, SERGEI BALAKIREV.
Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):
is_number = Cardcheck.check_card_number("1234-5678-9012-0980")
is_name = Cardcheck. check_name("SERGEI BALAKIREV")
Для проверки допустимых символов в классе должен быть прописан атрибут:
CHARS_FOR_NAME = ascii_lowercase.upper() + digits
Подумайте, как правильнее объявить методы check_card_number и check_name (декораторами @classmethod и @staticmethod).
💻💻💻
class cardcheck:
    @staticmethod
    def chek_card(a):
        c = ''
        for i in a.split('-'):
            c+=i
            if len(i)!=4:
                return False
        if c.isdigit()==True:
            return True
        else:
            return False
    @staticmethod
    def name_chek(name):
        c = name.split()
        if len(c)==2 and c[0].isupper()==True and c[1].isupper()==True and c[0].isalpha()==True and c[1].isalpha() ==True:
            return True
        else:
            return False
tests = [
        ("1234-5678-9012-3456", "JOHN DOE"),
        ("1234-5678-9012-345",  "ALICE SMITH"),
        ("1234-5678-9012-345G", "BOB 123"),
        ("0000-1111-2222-3333", "SERGEI BALAKIREV"),
    ]
for i in tests:
    print(f'статус карты: {cardcheck.chek_card(i[0])}')
    print(f'статус имени: {cardcheck.name_chek(i[1])}')
'''
'''  📝📝📝                                        Объявите в программе класс Video с двумя методами:
create(self, name) для задания имени пате текущего видео (метод сохраняет имя name в локальном атрибуте пате объекта класса Video);
play(self) - для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>"). Объявите еще один класс с 
именем YouTube, в котором объявите два метода (с декоратором @classmethod): add_video(cls, video) - для добавления нового видео 
(метод помещает объект video класса Video в список); play(cls, video_indx) - для проигрывания видео из списка по указанному индексу 
(индексация с нуля).
(здесь cls - ссылка на класс YouTube). И список (тоже внутри класса YouTube):
videos - для хранения добавленных объектов класса Video (изначально список пуст).
Метод play() класса YouTube должен обращаться к объекту класса Video по индексу списка videos и, затем, вызывать метод play() класса Video.
Методы add_video и play вызывайте напрямую из класса YouTube. Создавать экземпляр этого класса не нужно.
Создайте два объекта 1 и 2 класса Video, затем, через метод create() передайте им имена "Python" и "Python ООП". После этого с 
помощью метода add_video класса YouTube, добавьте в него эти два видео и воспроизведите (с помощью метода play класса YouTube) 
сначала первое, а затем, второе видео.
💻💻💻
class video:
    def create(self, v):
        self.name = v
    def play(self):
        return f'воспроизводится видео {self.name}'

class youtube:
    vid = list()
    @classmethod
    def add_video(cls, v):
        cls.vid.append(v)
    @classmethod
    def pla(cls,ind):
        try:
            return f'воспроизводится видео {cls.vid[ind]}'
        except IndexError:
            return 'Ошибка: видео с таким индексом не существует'
v1 = video()
v2 = video()
v1.create('Python')
v2.create('Python OOП')
print(v1.play())
print(v2.play())
print()
youtube.add_video(v1.name)
youtube.add_video(v2.name)
print(youtube.pla(0))
print(youtube.pla(1))
print(youtube.pla(2))
'''
'''   📝📝📝                                                    Объявите класс AppStore интернет-магазин приложений для устройств под iOS. 
В этом классе должнь быть реализованы следующие методы:
add_application(self, app) - добавление нового приложения арр в магазин; remove_application(self, app)- удаление приложения арр из магазина;
block_application(self, app) - блокировка приложения арр (устанавливает локальное свойство blocked объекта аpp в значение True); 
total apps(self) - возвращает общее число приложений в магазине.
Класс AppStore предполагается использовать следующим образом (эти строчки в программе не писать):
store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube) store.remove_application(app_youtube)
Здесь Application- класс, описывающий добавляемое приложение с указанным именем. Каждый объект класса Application должен содержать локальные свойства:
name-наименование приложения (строка);
blocked - булево значение (True приложение заблокировано; False не заблокировано, изначально False).
Как хранить список приложений в объектах класса AppStore решите сами.
💻💻💻
class appstore:
    b = dict()
    def add_application(self, a):
        self.b.update({a:True})
        print(f"приложение '{a}' добавлено")
    def remove_app(self,a):
        try:
            self.b.pop(a)
            print(f"приложение '{a}' успешно удалено")
        except KeyError:
            print(f"приложения '{a}' нету")
    def block(self,a):
        try:
            if self.b[a]!='Block':
                self.b[a]='Block'
                print(f"приложение {a} успешно заблокировано")
            else:
                print(f"приложение '{a}' уже заблокировано")
        except KeyError:
            print(f"приложения '{a}' нету")
    def total_app(self):
        return f'кол-во приложений: {len(self.b)}'
s = appstore()
s.add_application('Youtube')
s.add_application('Roblox')
s.add_application('Minecraft')
s.remove_app('Youtube')
s.remove_app('Youtube')
s.block('Youtube')
s.block('Minecraft')
s.block('Minecraft')
print(s.total_app())
'''
'''  📝📝📝                                           Объявите класс для мессенджера с именем Viber. В этом классе должны быть следующие методы:
add_message(msg) - добавление нового сообщения в список сообщений;
remove_message(msg) - удаление сообщения из списка;
set_like(msg) - поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg: если лайка нет то он ставится, если уже есть, то убирается);
show_last_message(число) отображение последних сообщений;
total_messages() возвращает общее число сообщений.
Эти методы предполагается использовать следующим образом:
msg = Message("Всем привет!")
Viber.add_message(msg)
Viber. add_message(Message("Это курс по Python 00П."))
Viber. add_message(Message("Что вы о нем думаете?")) Viber.set_like (msg)
Viber.remove_message(msg)
Класс меѕѕаgе (необходимо также объявить) позволяет создавать объекты-сообщения со следующим набором локальных свойств: text - текст сообщения (строка);
f_like-поставлен или не поставлен лайк у сообщения (булево значение True если лайк есть и False в противном случае, изначально
False).
💻💻💻
class viber:
    m =list()
    z = dict()
    def add_messege(self, ms):
        self.m.append(ms)
        self.z.update({ms:False})
        print(f"сообщение '{ms}' добавлено")
    def remove_messege(self,ms):
        try:
            self.m.remove(ms)
            self.z.pop(ms)
            print(f"сообщение '{ms}' удалено")
        except Exception:
            print(f"сообщения '{ms}' нет")
    def set_like(self, ms):
        try:
            if self.z[ms]==False:
                self.z[ms] = True
                print(f"лайк на сообщение '{ms}' поставлен")
            else:
                self.z[ms] = False
                print(f"лайк убран с сообщения '{ms}'")
        except KeyError:
            print(f"сообщения '{ms}' нет")
    def show_last_messeges(self, a):
        print(f'последние сообщения({a}): {' | '.join(self.m[-a:])}')
    def total_messeges(self):
        print(f'кол-во сообщений: {len(self.m)}')
class messege(viber):
    def text(self,ms):
        print(ms)
    def fl_like(self, ms):
        try:
            print(self.z[ms])
        except KeyError:
            print(f"сообщения '{ms}' нет")
m = messege()
m.add_messege('привет')
m.add_messege('здорова, как дела?')
m.add_messege('норм, вот ооп тут изучаю')
m.add_messege('и че, получается?')
m.add_messege('как видишь')
m.text('привет')
m.text('здорова, как дела?')
m.text('норм, вот ооп тут изучаю')
m.text('и че, получается?')
m.text('как видишь')
m.set_like('здорова, как дела?')
m.fl_like('здорова, как дела?')
m.set_like('здорова, как дела?')
m.fl_like('здорова, как дела?')
m.set_like('dfss')
m.remove_messege('привет')
m.set_like('привет')
m.show_last_messeges(3)
m.total_messeges()
'''
''' 📝📝📝                                      Создайте абстрактный класс Shape для рисования плоских фигур. Необходимо
построить производные классы Square (квадрат, который характеризуется координатами
левого верхнего угла и длиной стороны), Circle (окружность с заданными координатами
центра и радиусом), Ellipse (эллипс с заданными координатами вершин описанного вокруг
него прямоугольника), позволяющие рисовать указанные фигуры, а также передвигать их
на плоскости.
💻💻💻
from tkinter import *
class shape():
    def __init__(self, s):
        self.x = 250 - (s // 2)
        self.y = 250 + (s // 2)
        self.s = s
    def __str__(self):
        return f'{self.x}, {self.y}'
class square(shape):
    def sq(self):
        b = Canvas(bg='black', width=500, heigh=500)
        b.pack(anchor=CENTER, expand=1)
        b.create_rectangle(self.x, self.y, self.y, self.x, fill='white')
        mainloop()
class oval(shape):
    def oval(self):
        b = Canvas(bg='black', width=500, heigh=500)
        b.pack(anchor=CENTER, expand=1)
        b.create_oval(self.x, self.y, self.y, self.x, fill='white')
        mainloop()
a = 5
while not(0<a<3):
    a = int(input("""1 - квадрат
2 - круг
"""))
s = 0
if a==1:
    while not (0 < s < 501):
        s = int(input('введите размер рисунка(не более 500)\n'))
    square(s).sq()
elif a==2:
    while not (0 < s < 251):
        s = int(input('введите радиус круга(не более 250)\n'))*2
    oval(s).oval()
'''
'''📝📝📝                                                Разработайте класс Равнобочная трапеция, члены класса – координаты 4-х точек.
Предусмотрите в классе конструктор и методы: проверка, является ли фигура
равнобочной трапецией; вычисление и вывод сведений о фигуре: длины сторон, периметр,
площадь.
💻💻💻
from math import ceil
from tkinter import *
class trap:
    def __init__(self, a, b, c, d):
        x1, y1 = a.split()
        x2, y2 = b.split()
        x3, y3 = c.split()
        x4, y4 = d.split()
        x1, x2, x3, x4, y1, y2, y3, y4 = int(x1), int(x2), int(x3), int(x4), int(y1), int(y2), int(y3), int(y4)
        self.ab = ceil(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
        self.bc = ceil(((x3 - x2)**2 + (y3 - y2)**2)**0.5)
        self.cd = ceil(((x4 - x3)**2 + (y3 - y4)**2)**0.5)
        self.ad = ceil(((x4 - x1)**2 + (y4 - y1)**2)**0.5)
        self.f = self.ab==self.cd
        self.ah = abs(y2-y1)
    def istr(self):
        if self.f==True:
            return True
        else:
            return False
    def perim(self):
        return f'периметр: {self.ab+self.bc+self.cd+self.ad}'
    def plosh(self):
        return f'площадь: {(self.bc+self.ad)//2*self.ah}'
a = '2 3'
b = '6 6'
c = '8 6'
d = '12 3'
h=trap(a, b, c, d)
print('равнобедренная:',h.istr())
if h.istr()==True:
    print(h.perim())
    print(h.plosh())
    x1, y1 = a.split()
    x2, y2 = b.split()
    x3, y3 = c.split()
    x4, y4 = d.split()
    x1, x2, x3, x4, y1, y2, y3, y4 = int(x1), int(x2), int(x3), int(x4), int(y1), int(y2), int(y3), int(y4)
    a = Canvas( width=250,heigh=250)
    a.create_polygon((x1 * 10, y1 * 10), (x2 * 10, y2 * 10), (x3 * 10, y3 * 10), (x4 * 10, y4 * 10), fill='black')
    a.pack(anchor=CENTER)
    mainloop()
'''
''' 📝📝📝                                   Объявите в программе следующие несколько классов:
СРЦ-класс для описания процессоров;
Memory-класс для описания памяти;
MotherBoard-класс для описания материнских плат.
Обеспечить возможность создания объектов каждого класса командами:
cpu = CPU(наименование, тактовая частота)
= Nemory(наименование, размер памяти)
b = MotherBoard(наименование, процессор, память1, память2,..., памятьN)
Обратите внимание при создании объекта класса MotherBoard можно передавать несколько объектов класса Меmоrу, максимум N по числу слотов памяти на материнской плате (N = 4).
Объекты классов должны иметь следующие локальные свойства:
для класса CPU: name наименование; fr тактовая частота;
для класса Memory name наименование; volume - объем памяти;
для класса MotherBoard: name наименование; сри ссылка на объект класса CPU: total_mem_slots = 4- общее число слотов памяти (атрибут прописывается с этим значением и не меняется);
mem_slots список из объектов класса Memory (максимум total_mem_slots = 4 штук по максимальному числу слотов памяти).
Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов на материнской плате в виде следующего списка из четырех строк:
[Материнская плата: <наименование>",
Центральный процессор: «наименование>, <тактовая частота>,
Слотов памяти: «общее число слотов памяти>",
Память: <<наименование 1> <объем_1>; <наименование_2> <объем_2>;...; наименование_N> <объем_N>]
Создайте объект mь класса Mother Board с одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory).
💻💻💻
class comp:
    j = list()
    pass
class gpu(comp):
    def __init__(self,a,b):
        self.j.append(f'имя процессора: {a}')
        self.j.append(f'тактовая частота: {b}')
class mem(comp):
    def __init__(self,c,d):
        self.j.append(f'название памяти: {c}')
        self.j.append(f'объем памяти: {d} Гб')
class mb(comp):
    def __init__(self,e,p1=None,p2=None,p3=None,p4=None):
        self.j.append(f'имя материнской платы: {e}')
        o = [p1,p2,p3,p4]
        self.j.append(f'памяти({len(list(filter(lambda x: x!=None,o)))}): {list(filter(lambda x:x!=None,o))}')
    @classmethod
    def get_config(cls):
        return cls.j
gpu('крутой',124)
print(mb.get_config())
mem('оперативная',256)
print(mb.get_config())
mb('мама','память1','память2')
print(mb.get_config())
'''
'''  📝📝📝                                           Объявите в программе класс Cart (корзина), объекты которого создаются командой:
cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство дoods список объектов для покупки (объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.
В классе Cart объявить методы:
add(self, gd) - добавление в корзину товара, представленного объектом да; remove(self, indx) удаление из корзины товара по индексу indx;
get list(self) - получение из корзины товаров в виде списка из строк:
<наименовние_1>: <цена_1>', <наименовние_2>: <цена_2>',
<наименовние_N>: <<цена_N>]
Объявите в программе следующие классы для описания товаров:
Table - столы,
ТѴ-телевизоры;
Notebook- Ноутбуки;
Cup - кружки.
Объекты этих классов должны создаваться командой:
gd = Имя класса (name, price)
Каждый объект классов товаров должен содержать локальные свойства:
name-наименование;
price- цена.
Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.
💻💻💻
class cart:
    def __init__(self):
        self.gd = list()
    def add(self,g):
        self.gd.append(g)
    def remove(self,indx):
        self.gd.pop(indx)
    def get_list(self):
        return self.gd
def table(tabletka,ponos):
    return {tabletka: ponos}
def tv(n,p):
    return {n:p}
def notebook(n,p):
    return {n:p}
def cup(n,p):
    return {n:p}
gg = table('каменный', 500)
kk = tv('плоский', 10000)
ee = cup('стеклянная', 200)
a = cart()
a.add(gg)
a.add(kk)
a.add(ee)
print(a.get_list())
a.remove(0)
print(a.get_list())
b = cart()
b.add(gg)
print(b.get_list())
'''
'''   📝📝📝                                            Вам необходимо реализовать односвязный список (не список языка Python, объекты в списке не хранить, 
а формировать связанную структуру) из объектов класса ListObject:
Для этого объявите в программе класс ListObject, объекты которого создаются командой:
obj = Listobject(data)
Каждый объект класса ListObject должен содержать локальные свойства:
next obj - ссылка на следующий присоединенный объект (если следующего объекта нет, то next_obj = None);
data -данные объекта в виде строки.
самом классе ListObject должен быть объявлен метод:
link(self, obj) - для присоединения объекта obj такого же класса к текущему объекту self (то есть, атрибут next_obj объекта self должен ссылаться на obj).
Прочитайте список строк из входного потока командой:
lst_in = list(map(str, strip, sys.stdin.readlines()))
self.
Затем сформируйте односвязный список, в объектах которых (в атрибуте data) хранятся строки из списка Ist_in (первая строка в первом объекте, вторая во втором и т.д.). 
На первый добавленный объект класса ListObject должна ссылаться переменная head_obj.PC
💻💻💻
class listobject:
    def __init__(self,data):
        self.data = data
        self.lst_obj = None
        self.head_obj = None
    def link(self,obj):
        self.data.append(obj)
        if self.head_obj ==None:
            self.head_obj = obj
        self.lst_obj = obj
a = listobject([1,2,3,4])
a.link(123)
a.link('pp')
print(a.data,a.lst_obj)
b = listobject(['a','b','c','d'])
b.link('alfavit')
print(b.lst_obj)
print(a.head_obj)
'''
'''    📝📝📝                                                    Разработайте класс Book: Автор, Название, Издательство, Год, Количество 
страниц. Создайте массив объектов. Выведите: 
а) список книг заданного автора; 
б) список книг, выпущенных заданным издательством;
в) список книг, выпущенных после заданного года.
💻💻💻
class book:
    av = ['пушкин','толстой','даль']
    kn = [[('книга1','издательство4',1537,200),('книга2','издательство4',1999,300),('книга3','издательство1',1850,122)],[('война и мир','издательство5',1765,10000),('книга4','издательство1',1900,98)],[('книга5','издательство1',2027,443),('книга6','издательство4',988,889)]]
    n = dict(zip(av,kn))
    def avtor(self,a):
        a1 = self.av.index(a)
        for i in self.kn[a1]:
            print(i[0])
    def nazvanie(self,a):
        c = 0
        for i in self.kn:
            for g in i:
                if g[0]==a:
                    print(self.av[c])
                    break
            c +=1
    def isdatel(self,a):
         for i in self.kn:
            for g in i:
                if g[1]==a:
                    print(g[0])
    def posle(self,a):
        for i in self.kn:
            for g in i:
                if g[2]>=a:
                    print(g[0])
a = book()
print('книги Пушкина:')
a.avtor('пушкин')
print('\nавтор книги 6')
a.nazvanie('книга6')
print('\nкниги, выпущенные издательством 4:')
a.isdatel('издательство4')
print('\nкниги, выпущенные после 1800')
a.posle(1800)
'''
'''📝📝📝                                                               Создайте базовый класс «Транспортное средство» и производные классы 
«Автомобиль», «Велосипед», «Повозка». Подсчитайте время и стоимость перевозки 
пассажиров и грузов каждым транспортным средством.
💻💻💻
class transport:
    v = 100
    p = 100
    def vrema(self):
        return f'vremya perevosky: {self.v}'
    def plata(self):
        return f'stoimostb perevozky: {self.p}'
class povozka(transport):
    v = 1000
class velosiped(transport):
    v = 500
    p = 0
class avto(transport):
    p = 2500
print(povozka().vrema())
print(povozka().plata())
print(avto().vrema())
print(avto().plata())
print(velosiped().vrema())
print(velosiped().plata())
'''
''' 📝📝📝                                                                    запускает калькулятор и считает 5х4
💻💻💻
from pywinauto import Application
import time
app = Application(backend='uia').start('Calc')
time.sleep(1)
app.connect(title='Калькулятор')
dlg = app.window(title='Калькулятор')
dlg.child_window(title='Четыре', control_type='Button').click()
dlg.child_window(title='Умножить на', control_type='Button').click()
dlg.child_window(title='Пять', control_type='Button').click()
dlg.child_window(title='Равно', control_type='Button').click()
'''
'''                                                                                 открывает ватсап и нажимает на контакт Планшет

import time
from pywinauto import mouse,Application
mouse.click(button='left',coords=(322, 1057))
time.sleep(0.5)
app = Application(backend='uia').connect(title='WhatsApp')
e = app.window(title='WhatsApp')
e.child_window(title='Планшет', control_type='Text').click_input()
'''
'''📝📝📝                                                            телеграм бот с некоторыми функциями
💻💻💻
import telebot as tg
import requests
from bs4 import BeautifulSoup
from datetime import datetime
bot = tg.TeleBot("8441626044:AAEKFDSUOPzHsV8XU8YayiFvQhHKvHrfH1M")
vop = ['1. Сколько существует видов алгоритмов в пайтон?',"2. Как создать список?","3. Какая самая маленькая единица измерения памяти?",
       "4. что выведет данная программа?\na = 15\nif a!=15:\n   a **=2\nelse:\n    a /=3\nprint(a)","5. Возможно ли одновременно запустить несколько программ?",
       "6. Что возвращает функция len()?","7. Какой из этих типов данных логический?","8. Что значит // ?",'9. Кто придумал основные принципы кодированя информации?',
       '10. Выберете неправильное название переменной']
ot = dict()
pr = {1: 3, 2: 'a = list()', 3: 'бит', 4: '5.0', 5: 'да', 6: 'длину строки', 7: '1', 8: 'деление нацело', 9: 'Кравцов Иван', 10: '1bes'}
@bot.message_handler(commands=["start"])
def repeat_all_messages(message):
    keyboard = tg.types.InlineKeyboardMarkup()
    button1 = tg.types.InlineKeyboardButton(text="начать", callback_data="старт")
    keyboard.add(button1)
    global msg
    msg = bot.send_message(message.chat.id, 'тест на знание пайтон\nколичество вопросов: 10',reply_markup=keyboard)
@bot.message_handler(commands=['search'])
def search(ms):
    mark = tg.types.InlineKeyboardMarkup()
    b = tg.types.InlineKeyboardButton(text='погода', callback_data='pogoda')
    b1 = tg.types.InlineKeyboardButton(text='время', callback_data='vremya')
    b3 = tg.types.InlineKeyboardButton(text='звонок через', callback_data='zvon')
    b2 = tg.types.InlineKeyboardButton(text='фото', callback_data='negr')
    mark.add(b, b1)
    mark.add(b3, b2)
    global msg
    msg = bot.send_message(ms.chat.id, 'нажми на кнопку', reply_markup=mark)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'pogoda':
        response = requests.get(
            'https://yandex.ru/pogoda/ru/moscow?lat=55.755863&lon=37.617699&utm_source=serp&utm_medium=touch&utm_content=helper_today&utm_campaign=helper&utm_term=title&ysclid=mgktpsq01836237733')
        page = BeautifulSoup(response.text, 'html5lib')
        a = page.find_all('p', class_="A11Y_visuallyHidden__y0sw0 visuallyHidden")
        for i in a:
            if 'погода сейчас' in i.text:
                bot.send_message(call.message.chat.id,i.text.lstrip('Тверской район, '))
                break
    if call.data == 'vremya':
        a = datetime.now()
        bot.send_message(call.message.chat.id, f'{a.hour}:{a.minute}')

    if call.data == 'zvon':
        f = [30600, 33300, 34500, 37200, 38400, 41100, 42300, 45000, 45600, 48300, 49500, 52200, 53400, 56100]
        a = datetime.now()
        a1 = a.hour * 3600 + a.minute * 60 + a.second
        for i in f:
            if i > a1:
                b1 = i
                break
            else:
                b1 = f[0]
        e = b1 - a1
        if e < 0:
            e = (86400 - a1) + b1
        if e // 3600 >= 1:
            bot.send_message(call.message.chat.id, f'{e // 3600} часов {e // 60 % 60} минут {e % 60} секунд')
        else:
            bot.send_message(call.message.chat.id, f'{e // 60 % 60} минут {e % 60} секунд')
    if call.data == 'negr':
        bot.send_photo(call.message.chat.id,
                       'https://avatars.mds.yandex.net/i?id=54ee191148b1211fc052de3ae21c5548_l-5869942-images-thumbs&n=13')
    if call.data == "старт":
        keyboard = tg.types.InlineKeyboardMarkup()
        b1 = tg.types.InlineKeyboardButton(text="1", callback_data="1:1")
        b2 = tg.types.InlineKeyboardButton(text="2", callback_data="1:2")
        b3 = tg.types.InlineKeyboardButton(text="3", callback_data="1:3")
        keyboard.add(b1,b2,b3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id, text='1. Сколько существует видов алгоритмов в пайтон?', reply_markup=keyboard)
    elif call.data in '1:1 1:2 1:3':
        if call.data == "1:1":
            ot.update({1: 1})
        elif call.data == "1:2":
            ot.update({1:2})
        elif call.data == '1:3':
            ot.update({1:3})
        keyboard = tg.types.InlineKeyboardMarkup()
        b1 = tg.types.InlineKeyboardButton(text="а = list", callback_data="2:1")
        b2 = tg.types.InlineKeyboardButton(text="a = list()", callback_data="2:2")
        b3 = tg.types.InlineKeyboardButton(text="a = str()", callback_data="2:3")
        keyboard.add(b1, b2, b3)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=msg.message_id,text= "2. Как создать список?", reply_markup=keyboard)
    elif call.data in '2:1 2:2 2:3':
        if call.data == "2:1":
            ot.update({2: "а = list"})
        elif call.data == "2:2":
            ot.update({2:"a = list()"})
        elif call.data == '2:3':
            ot.update({2:"a = str()"})
        keyboard = tg.types.InlineKeyboardMarkup()
        b1 = tg.types.InlineKeyboardButton(text="бит", callback_data="3:1")
        b2 = tg.types.InlineKeyboardButton(text="гбайт", callback_data="3:2")
        b3 = tg.types.InlineKeyboardButton(text="километр", callback_data="3:3")
        keyboard.add(b1, b2, b3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id, text="3. Какая самая маленькая единица измерения памяти?", reply_markup=keyboard)
    elif call.data in '3:1 3:2 3:3':
        if call.data == "3:1":
            ot.update({3: "бит"})
        elif call.data == "3:2":
            ot.update({3:"гбайт"})
        elif call.data == '3:3':
            ot.update({3:"километр"})
        keyboard = tg.types.InlineKeyboardMarkup()
        b1 = tg.types.InlineKeyboardButton(text="225", callback_data="4:1")
        b2 = tg.types.InlineKeyboardButton(text="5", callback_data="4:2")
        b3 = tg.types.InlineKeyboardButton(text="5.0", callback_data="4:3")
        b4 = tg.types.InlineKeyboardButton(text="0.5", callback_data="4:4")
        keyboard.add(b1, b2)
        keyboard.add(b3,b4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id,
                              text="4. что выведет данная программа?\na = 15\nif a!=15:\n   a **=2\nelse:\n    a /=3\nprint(a)", reply_markup=keyboard)
    elif call.data in '4:1 4:2 4:3 4:4':
        if call.data == "4:1":
            ot.update({4: "225"})
        elif call.data == "4:2":
            ot.update({4:'5'})
        elif call.data == '4:3':
            ot.update({4:'5.0'})
        elif call.data == '4:4':
            ot.update({4:'0.5'})
        keyboard = tg.types.InlineKeyboardMarkup()
        b1 = tg.types.InlineKeyboardButton(text="нет", callback_data="5:1")
        b2 = tg.types.InlineKeyboardButton(text='да', callback_data="5:2")
        keyboard.add(b1, b2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id,text="5. Возможно ли одновременно запустить несколько программ?",reply_markup=keyboard)
    elif call.data in '5:1 5:2':
        if call.data == "5:1":
            ot.update({5: "нет"})
        elif call.data == "5:2":
            ot.update({5:'да'})
        keyboard = tg.types.InlineKeyboardMarkup()
        b1 = tg.types.InlineKeyboardButton(text="длину строки", callback_data="6:1")
        b2 = tg.types.InlineKeyboardButton(text='сумму чисел', callback_data="6:2")
        b3 = tg.types.InlineKeyboardButton(text='сумму цифр', callback_data="6:2")
        keyboard.add(b1, b2, b3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id,text="6. Что возвращает функция len()?", reply_markup=keyboard)
    elif call.data in '6:1 6:2 6:3':
        if call.data == "6:1":
            ot.update({6: "длину строки"})
        elif call.data == "6:2":
            ot.update({6:'сумму чисел'})
        elif call.data == '6:3':
            ot.update({6:'сумму цифр числа'})
        keyboard = tg.types.InlineKeyboardMarkup()
        b1 = tg.types.InlineKeyboardButton(text="1", callback_data="7:1")
        b2 = tg.types.InlineKeyboardButton(text='15.3', callback_data="7:2")
        b3 = tg.types.InlineKeyboardButton(text='попа', callback_data="7:3")
        b4 = tg.types.InlineKeyboardButton(text='4', callback_data="7:4")
        keyboard.add(b1, b2)
        keyboard.add(b3, b4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id,text="7. Какой из этих типов данных логический?", reply_markup=keyboard)
    elif call.data in '7:1 7:2 7:3 7:4':
        if call.data == "7:1":
            ot.update({7: '1'})
        elif call.data == "7:2":
            ot.update({7:'15.3'})
        elif call.data == '7:3':
            ot.update({7:'попа'})
        elif call.data == '7:4':
            ot.update({7:'4'})
        keyboard = tg.types.InlineKeyboardMarkup()
        b1 = tg.types.InlineKeyboardButton(text="умножение", callback_data="8:1")
        b2 = tg.types.InlineKeyboardButton(text='дробь', callback_data="8:2")
        b3 = tg.types.InlineKeyboardButton(text='остаток от деления', callback_data="8:3")
        b4 = tg.types.InlineKeyboardButton(text='деление нацело', callback_data="8:4")
        keyboard.add(b1, b2)
        keyboard.add(b3, b4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id,text="8. Что значит // ?", reply_markup=keyboard)
    elif call.data in '8:1 8:2 8:3 8:4':
        if call.data == "8:1":
            ot.update({8: "умножение"})
        elif call.data == "8:2":
            ot.update({8:'дробь'})
        elif call.data == '8:3':
            ot.update({8:'остаток от деления'})
        elif call.data == '8:4':
            ot.update({8:'деление нацело'})
        keyboard = tg.types.InlineKeyboardMarkup()
        b1 = tg.types.InlineKeyboardButton(text="Кравцов Иван", callback_data="9:1")
        b2 = tg.types.InlineKeyboardButton(text='Фон Нейман', callback_data="9:2")
        b3 = tg.types.InlineKeyboardButton(text='Пушкин', callback_data="9:3")
        b4 = tg.types.InlineKeyboardButton(text='Цуркерберг', callback_data="9:4")
        keyboard.add(b1, b2)
        keyboard.add(b3, b4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id,text='9. Кто придумал основные принципы кодированя информации?', reply_markup=keyboard)
    elif call.data in '9:1 9:2 9:3 9:4':
        if call.data == "9:1":
            ot.update({9: "Кравцов Иван"})
        elif call.data == "9:2":
            ot.update({9:'Фон Нейман'})
        elif call.data == '9:3':
            ot.update({9:'Пушкин'})
        elif call.data == '9:4':
            ot.update({9:'Цуркерберг'})
        keyboard = tg.types.InlineKeyboardMarkup()
        b1 = tg.types.InlineKeyboardButton(text="1bes", callback_data="10:1")
        b2 = tg.types.InlineKeyboardButton(text='ad_ili_ray', callback_data="10:2")
        b3 = tg.types.InlineKeyboardButton(text='bs234jseeiso45924jkl2h32o', callback_data="10:3")
        b4 = tg.types.InlineKeyboardButton(text='w', callback_data="10:4")
        keyboard.add(b1, b2)
        keyboard.add(b3, b4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id,text='10. Выберете неправильное название переменной', reply_markup=keyboard)
    elif call.data in '10:1 10:2 10:3 10:4':
        if call.data == "10:1":
            ot.update({10: "1bes"})
        elif call.data == "10:2":
            ot.update({10:'ad_ili_ray'})
        elif call.data == '10:3':
            ot.update({10:'bs234jseeiso45924jkl2h32o'})
        elif call.data == '10:4':
            ot.update({10:'w'})
        c = 1
        og = 0
        for i in ot.values():
            if i == pr[c]:
                og += 1
            c += 1
        if og!=10:
            keyboard = tg.types.InlineKeyboardMarkup()
            b1 = tg.types.InlineKeyboardButton(text="показать ответы", callback_data="конец")
            keyboard.add(b1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id,text=f'оценка {og}/10\n\n', reply_markup=keyboard)
    elif call.data == 'конец':
        c = 1
        a = ''
        for i in ot.values():
            if i != pr[c]:
                a += f"""{vop[c-1]}
твой ответ: {i}
правильный ответ: {pr[c]}

"""
            c += 1
        bot.send_message(call.message.chat.id, a)


bot.polling(none_stop=True, interval=0)
'''
'''📝📝📝                                                учусть использовать ткинтер
💻💻💻
import tkinter as tk
c = 0
def ot(l,b):
    global c
    c += 1
    e = tk.Label()
    if c==1:
        e.configure(text='эй не надо нажимать')
    elif c==2:
        e.configure(text='последнее предупреждение')
    elif c==3:
        e.configure(text='кто прочел тот лох')
    elif c==69:
        b['state'] = ['disabled']
        b['text']='о нет ты сломал ее'
    l.config(text=c)
    e.pack()
a = tk.Tk()
a.title('okno')
a.geometry('500x500+700+200')
l = tk.Label(a,text='вопрос1',width=100,height=50,font=(15))
l.place(x=200,y=0)
b=tk.Button(text='не нажиай',command=lambda:ot(l,b))
b.configure(background='#FF7276')
b.pack(expand=True,anchor='w',padx=40)
tk.mainloop()
'''
''' 📝📝📝                                                                 олимпиадное задание
Ваня очень дружелюбный мальчик, поэтому у него очень много друзей.
Ваня рад этому, но вот делиться, если он что-то купил, приходится со всеми.
Потому Ваня придумал очень гениальный план. Когда его спрашивают, что он
купил, при выходе с магазина, он хочет называть только те продукты, которыми
ему не жалко поделиться.
Продукты, которыми не жалко поделиться, это продукты, которых Ваня
купил минимум K//2 (целочисленное деление K на 2), где K – количество друзей,
которые встретили Ваню у магазина.
Определите, какими продуктами Ваня поделится в этот раз с ребятами.
Входные данные:
На вход в программу на первой строке подаётся K – количество друзей,
которые встречают Ваню у магазина (1 <= K <= 10000).
На второй строке подаётся N (1 <= N <= 1000000) – количество продуктов,
которые купил Ваня.
Далее, на N строках указаны названия продуктов (одно слово английскими
буквами), купленных Ваней, притом продукты, которые были куплены более чем
в количестве 1 штуки, идут подряд. Если Ваня купил Apple 3 штуки,
то Apple будут идти подряд. Но продукты не отсортированы по алфавиту!
Выходные данные:
На выходе необходимо вывести в отсортированном по алфавиту порядке
названия всех продуктов (каждое название на новой строке), которыми
поделится Ваня. Если Ваня не поделится с ребятами продуктами, то вывести
«NO» заглавными буквами.
💻💻💻
import copy
k = int(input())//2
l = list()
for i in range(int(input())):
    l.append(input())
kol = dict()
c = 0
for i in l:
    for g in l:
        if g==i:
            c+=1
            kol.update({g:c})
    c=0
kol1=copy.copy(kol)
for i,g in kol.items():
    if g==1 or g<k:
        kol1.pop(i)
l.clear()
for i,i1 in kol1.items():
    for i3 in range(i1//2):
        l.append(i)
l.sort()
if l!=[]:
    for i in l:
        print(i)
"""
4
6
Apple
Apple
Milk
Cola
Cola
Cola
"""
'''
'''  📝📝📝                                                  Маша работает в очень крупной IT-компании, притом полностью
удалённо. Маша поняла, что сидячая работа – это очень тяжело, поэтому
прикупила себе недорогой гребной тренажёр. Но так как тренажёр недорогой, то
Маша прочитав инструкцию поняла, что он имеет ограничения по времени
работы и простоя. Таким образом, на тренажёре можно заниматься только 20
минут максимум, а потом нужно чтобы тренажёр «отдыхал» минимум 10 минут.
Маша решила посчитать, сколько минут она сможет прозаниматься на
тренажёре за день, если будет знать все свои промежутки времени, когда она не
может заниматься на тренажёре 100%.
Работает Маша с 10:00 по 19:00, потому в подсчёт идёт только время
проведённое на тренажёре именно в этот промежуток времени.
Входные данные:
На вход на первой строке подаётся число N (1<=N<=1000) – количество
занятых промежуток Маши.
Далее на N строках указываются промежутки в виде времени начала и
времени конца занятого времени в формате h:mm-h:mm (например, 9:12-9:20) в
хронологическом порядке.
Выходные данные:
Выведите на одной строке количество минут, которые Маша проведёт на
тренажёре в этот день, если она будет заниматься сразу же, как тренажёр
«отдохнул».
Примечание: если тренажёр включили меньше чем на 20 минут, то на
отдых ему требуется также 10 минут.
💻💻💻
a = int(input())
l =list()
for i in range(a):
    a,b=input().split('-')
    a,b=int(a[3:])+int(a[:2])*60,int(b[3:])+int(b[:2])*60
    l.append([a,b])
ot=[]
pr1=600
pr2=1140
l.append([pr2,pr2])
for i in l:
    e = i[0]-pr1
    if e//20==0:
        e2=0
    else:
        e2=(e//30)*10
    e-=e2
    ot.append(e)
    pr1=i[1]
print(sum(ot))
"""
2
10:15-12:00
14:14-15:10
"""
'''
'''📝📝📝                                               Игра «Космическое домино».
Правила.
1. В игре участвуют только ТРЕХЗНАЧНЫЕ числа.
2. Перед началом игры для каждого игрока случайным образом генерируется
некоторый диапазон трехзначных чисел, из которого и ТОЛЬКО из него он
может выбирать числа для продолжения игры.
3. Первые два стартовых числа генерируются тоже компьютером.
4. Игроки ходят по очереди, доставляя сопряженное число из своего диапазона
(если такое есть) к левому или правому концу цепочки.
5. Если у игрока нет в диапазоне числа, сопрягаемого ни с одним из концов
цепочки, то игра завершается его проигрышем.
Определение: число M называется сопрягаемым с числом N, если оно построено
по следующим правилам:
1. Если N нечетное, то число M начинается с нечетной цифры, если N – четное,
то с четной (но не с 0!)
2. Последние две цифры числа M есть сумма цифр числа N.
Заметим, что оба числа являются трехзначными!
Например, если N = 213, тогда M может быть 106, 306, 506, 706 или 906. Для
числа N = 914, число M может быть только 214, 414, 614 или 814.
Примечание: числа в цепочке могут повторяться.
Входные данные:
L и R два натуральных трехзначных числа через пробел в одной строке. Левое и
правое число в цепочке соответственно.
A и B два натуральных трехзначных числа через пробел в одной строке. Диапазон,
который выпал игроку в начале игры. A < B. Число A или B также может быть выбрано
игроком для хода, если является сопрягаемым с концом цепочки.
Выходные данные:
На первой строчке количество чисел, сопрягаемых с концами цепочки из
диапазона игрока.
На второй строке минимальное из этих чисел с указанием перед ним без пробела
литеры “ L”, если его надо поставить к левому концу, и литеры “R”, если к правому.
Если число можно добавить в любой конец, то ставим его в левый конец.
💻💻💻
f,f1=map(int,input().split())
d,d1=map(int,input().split())
c=0
c1=list()
c2=list()
for i in range(d,d1+1):
    if ((f%2==0 and int(str(i)[0])%2==0) or (f%2!=0 and int(str(i)[0])%2!=0)) and sum(int(i) for i in str(f))==int(str(i)[-2:]):
        c+=1
        c1.append(i)
    elif ((f1%2==0 and int(str(i)[0])%2==0) or (f1%2!=0 and int(str(i)[0])%2!=0)) and sum(int(i) for i in str(f1))==int(str(i)[-2:]):
        c+=1
        c2.append(i)
print(c)
if c1+c2:
    if c1 and c2 and min(c1)>min(c2):
        print('R',end='')
    else:
        print('L', end='')
    print(min(c1+c2))
'''
'''  📝📝📝                                          бинарный поиск
💻💻💻
a=[9,8,7,6,4,3,2,1,0]
a.sort()
l,r=0,len(a)
n=3
c=0
while l!=r-1:
    u=(l+r)//2
    if a[u]>n:
        r=u
    else:
        l=u
    c+=1
    if a[u]==n:
        break
print(a,c)
'''
'''  📝📝📝                                          сортировка
💻💻💻
a=[9,8,7,6,4,3,2,1]
e=len(a)
for i in range(e-1):
    for g in range(e-i-1):
        if a[g]>a[g+1]:
            a[g],a[g+1]=a[g+1],a[g]
print(a)
'''
'''  📝📝📝                                           Требуется определить в заданном массиве количество элементов, равных искомому числу.
💻💻💻
a=[0,1,1,1,1,2,3,4,6]
l,r=0,len(a)
n=1
c=0
while l!=r-1:
    u=(l+r)//2
    if a[u]>n:
        r=u
    else:
        l=u
    if a[u]==n:
        a.remove(n)
        c+=1
        l, r = 0, len(a)
print(c)
'''
'''    📝📝📝                                      Проверяет простоту числа(делится только на себя и 1)
💻💻💻
def pr(n):
    k=2
    while k*k<=n and n%k!=0:
        k+=1
    return k*k>n
'''
'''📝📝📝                                              17. *Напишите программу перебора слов заданной длины,
не использующую рекурсию. Попробуйте составить функцию, которая на основе некоторой комбинации
вычисляет следующую за ней.
💻💻💻
n=4
alf='абвг'
b=''
def perev(s,v):
    s1=''
    while s!=0:
        s1=str(s%v)+s1
        s//=v
    return s1
t='вгвг'
for g in range(len(alf)):
        t=t.replace(alf[g],str(g))
t=int(t,len(alf))
t+=1
t=perev(t,len(alf))
for g in range(len(alf)):
    t=t.replace(str(g),alf[g])
while len(t)!=n:
    t=alf[0]+t
print(t)
"""c=0
n1=len(alf)**n
for i in range(n1):
    t=perev(i,len(alf))
    for g in range(len(alf)):
        t=t.replace(str(g),alf[g])
    while len(t)!=n:
        t=alf[0]+t
    print(t)
print(n1)"""
#гбгв гбгг: ггаг ггба; вгвг вгга
'''
'''  📝📝📝                                                      Напишите программу, которая заполняет матрицу 7×7 
случайными числами, а затем записывает в элементы, отмеченные на рисунках, число 99:
💻💻💻
import random as rd
a1=7
b=7
a=[[rd.randint(0,9) for i in range(a1)] for g in range(b)]
for i in a:
    print(i)
for i in range(len(a)):
    for g in range(len(a)):
        if g==(a1-1)//2:
            if i<=(b-1)//2:
                for e in range(g-i,g+i+1):
                    a[i][e]=99
            else:
                for e in range(g-(b-i)+1,g+(b-i)):
                    a[i][e]=99
print()
for i in a:
    for g in i:
        print(' '+str(g) if g<10 else g,end=' ')
    print()
'''
''' 📝📝📝                                           Заполните матрицу, содержащую N строк и M столбцов, натуральными числами по спирали и
змейкой, как на рисунках:
💻💻💻
a)
from math import ceil
n=5
m=9
a=[[0 for i in range(n)] for g in range(m)]
for i in a:
    for g in i:
        print(' '+str(g) if g<10 else g,end=' ')
    print()
e=iter(i for i in range(1,n*m+1))
gr=0
gr1=m-1
gg=n-1
gg1=0
for i1 in range(ceil(min(m,n)/2)):
    for i in range(m):
        for g in range(n):
            if i==gr and g>=gg1 and g<=gg:
                a[i][g]=next(e)
    for i in range(m):
        for g in range(n):
            if g==gg and i>gr and i<=gr1:
                a[i][g]=next(e)
    for i in range(m):
        for g in range(n-2,-1,-1):
            if i==gr1 and g<gg and g>=gg1 and a[i][g]==0:
                a[i][g]=next(e)

    for i in range(m-2,-1,-1):
        for g in range(n):
            if i>gr and g==gg1 and i<gr1 and a[i][g]==0:
                a[i][g]=next(e)
    gr+=1
    gg1+=1
    gr1-=1
    gg-=1
print()
for i in a:
    for g in i:
        print(' '+str(g) if g<10 else g,end=' ')
    print()
'''
