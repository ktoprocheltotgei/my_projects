import random as rd
import pandas as pd
pd.options.display.expand_frame_repr = False
class gamepole():
    def int(self, n, m):
        self._n = n
        self._m = m
        self.is_alive = True
        self.hode = 0
        self.pole = [[0 for i in range(self._n)] for i in range(self._n)]
        self.olp = [['◽' for i in range(self._n)] for i in range(self._n)]
    def init(self):
        for i in range(self._m):
            a = rd.randint(0, self._n - 1)
            b = rd.randint(0, self._n - 1)
            while self.pole[a][b] == '*':
                a = rd.randint(0, self._n - 1)
                b = rd.randint(0, self._n - 1)
            self.pole[a][b] = '*'
            if 0 < b < self._n - 1:
                if self.pole[a][b - 1] != '*':
                    self.pole[a][b - 1] += 1
                if self.pole[a][b + 1] != '*':
                    self.pole[a][b + 1] += 1
                if 0 < a < self._n - 1:
                    if self.pole[a - 1][b - 1] != '*':
                        self.pole[a - 1][b - 1] += 1
                    if self.pole[a - 1][b + 1] != '*':
                        self.pole[a - 1][b + 1] += 1
                    if self.pole[a + 1][b - 1] != '*':
                        self.pole[a + 1][b - 1] += 1
                    if self.pole[a + 1][b + 1] != '*':
                        self.pole[a + 1][b + 1] += 1
                elif a > 0:
                    if self.pole[a - 1][b - 1] != '*':
                        self.pole[a - 1][b - 1] += 1
                    if self.pole[a - 1][b + 1] != '*':
                        self.pole[a - 1][b + 1] += 1
                elif a < self._n:
                    if self.pole[a + 1][b - 1] != '*':
                        self.pole[a + 1][b - 1] += 1
                    if self.pole[a + 1][b + 1] != '*':
                        self.pole[a + 1][b + 1] += 1
            elif b > 0:
                if self.pole[a][b - 1] != '*':
                    self.pole[a][b - 1] += 1
                if 0 < a < self._n - 1:
                    if self.pole[a - 1][b - 1] != '*':
                        self.pole[a - 1][b - 1] += 1
                    if self.pole[a + 1][b - 1] != '*':
                        self.pole[a + 1][b - 1] += 1
                elif a > 0:
                    if self.pole[a - 1][b - 1] != '*':
                        self.pole[a - 1][b - 1] += 1
                elif a < self._n:
                    if self.pole[a + 1][b - 1] != '*':
                        self.pole[a + 1][b - 1] += 1
            elif b < self._n - 1:
                if self.pole[a][b + 1] != '*':
                    self.pole[a][b + 1] += 1
                if 0 < a < self._n - 1:
                    if self.pole[a - 1][b + 1] != '*':
                        self.pole[a - 1][b + 1] += 1
                    if self.pole[a + 1][b + 1] != '*':
                        self.pole[a + 1][b + 1] += 1
                elif a > 0:
                    if self.pole[a - 1][b + 1] != '*':
                        self.pole[a - 1][b + 1] += 1
                elif a < self._n:
                    if self.pole[a + 1][b + 1] != '*':
                        self.pole[a + 1][b + 1] += 1

            if 0 < a < self._n - 1:
                if self.pole[a + 1][b] != '*':
                    self.pole[a + 1][b] += 1
                if self.pole[a - 1][b] != '*':
                    self.pole[a - 1][b] += 1
            elif a > 0:
                if self.pole[a - 1][b] != '*':
                    self.pole[a - 1][b] += 1
            elif a < self._n - 1:
                if self.pole[a + 1][b] != '*':
                    self.pole[a + 1][b] += 1
    def show(self):
        print(pd.DataFrame(self.pole, [f'|{i + 1}|' for i in range(self._n)], [f'| {i + 1}' for i in range(self._n)]))
    def nerazminirovannoe_pole(self):
        print(pd.DataFrame(self.olp, [f'|{i + 1}|' for i in range(self._n)], [f'| {i + 1}' for i in range(self._n)]))

    def hod(self, a, b):
        if self.olp[a][b]==self.pole[a][b]:
            print('клетка уже открыта')
            return 0
        self.olp[a][b] = self.pole[a][b]
        if self.olp[a][b]==0:
            d = list()
            d1 = list()
            c = 0
            e = 0
            for i in range(self._n):
                e +=self.olp[i].count(0)
            while e>c:

                try:
                    if self.olp[a + 1][b] != self.pole[a + 1][b]:
                        self.olp[a + 1][b] = self.pole[a + 1][b]
                        self.hode+=1
                        if self.olp[a + 1][b]==0:
                            d.append(a+1)
                            d1.append(b)
                            c-=1
                except IndexError:
                    ''
                try:
                    if self.olp[a + 1][b+1] != self.pole[a + 1][b+1]:
                        self.olp[a + 1][b + 1] = self.pole[a + 1][b + 1]
                        self.hode += 1
                        if self.olp[a + 1][b+1]==0:
                            d.append(a+1)
                            d1.append(b+1)
                            c-=1
                except IndexError:
                    ''
                try:
                    if b > 0 and self.olp[a + 1][b - 1] != self.pole[a + 1][b - 1]:
                        self.olp[a + 1][b - 1] = self.pole[a + 1][b - 1]
                        self.hode += 1
                        if self.olp[a + 1][b-1]==0:
                            d.append(a + 1)
                            d1.append(b - 1)
                            c-=1
                except IndexError:
                    ''

                try:
                    if a > 0 and self.olp[a - 1][b] != self.pole[a - 1][b]:
                        self.olp[a - 1][b] = self.pole[a - 1][b]
                        self.hode += 1
                        if self.olp[a - 1][b]==0:
                            d.append(a-1)
                            d1.append(b)
                            c-=1
                except IndexError:
                    ''
                try:
                    if a>0 and self.olp[a - 1][b + 1] != self.pole[a - 1][b + 1]:
                        self.olp[a - 1][b + 1] = self.pole[a - 1][b + 1]
                        self.hode += 1
                        if self.olp[a - 1][b+1]==0:
                            d.append(a - 1)
                            d1.append(b + 1)
                            c-=1

                except IndexError:
                    ''
                try:
                    if a > 0 and b>0 and self.olp[a - 1][b - 1] != self.pole[a - 1][b - 1]:
                        self.olp[a - 1][b - 1] = self.pole[a - 1][b - 1]
                        self.hode += 1
                        if self.olp[a - 1][b-1]==0:
                            d.append(a - 1)
                            d1.append(b - 1)
                            c-=1
                except IndexError:
                    ''
                try:
                    if self.olp[a][b + 1] != self.pole[a][b + 1]:
                        self.olp[a][b + 1] = self.pole[a][b + 1]
                        self.hode += 1
                        if self.olp[a][b+1]==0:
                            d.append(a)
                            d1.append(b + 1)
                            c-=1
                except IndexError:
                    ''
                try:
                    if b > 0 and self.olp[a][b - 1] != self.pole[a][b - 1]:
                        self.olp[a][b - 1] = self.pole[a][b - 1]
                        self.hode += 1
                        if self.olp[a][b-1]==0:
                            d.append(a)
                            d1.append(b - 1)
                            c-=1
                except IndexError:
                    ''
                if len(d)!=0 and len(d1)!=0:
                    a = d[0]
                    b = d1[0]
                    d.pop(0)
                    d1.pop(0)
                c +=1
                e = 0
                for i in range(self._n):
                    e += self.olp[i].count(0)
        print(pd.DataFrame(self.olp, [f'|{i + 1}|' for i in range(self._n)], [f'| {i + 1}' for i in range(self._n)]))
        print()
        if self.pole[a][b] == '*':
            print('вы взорвались')
            self.is_alive = False
        self.hode += 1
    def bezopasnoe_nachalo(self,a):
        e = 0
        c,c1 = 0,0
        for i in self.pole:
            for g in i:
                if g==0:
                    a.hod(c,c1)
                    e = 1
                    break
                c1+=1
            if e==1:
                break
            c+=1
            c1 = 0


print('                                                                                        САПЕР')
v = input('''ввберите уровень сложности
1 - начинающий(7х7)
2 - любитель(16х16)
3 - эксперт(25х25)
''')
while v.isdigit()==False or not 0<int(v)<5:
    v = input('''ввберите уровень сложности
1 - начинающий(7х7)
2 - любитель(16х16)
3 - эксперт(25х25)
''')
a = gamepole()
if v=='1':
    a.int(7,6)
if v=='2':
    a.int(16,40)
if v=='3':
    a.int(25,125)
a.init()
v = input('''легкий старт отключен
1 - включить
2 - не включать
''')
while v.isdigit()==False or not 0<int(v)<3:
    v = input('''легкий старт отключен
1 - включить
2 - не включать
''')
if v=='1':
    a.bezopasnoe_nachalo(a)
if v=='2':
    a.nerazminirovannoe_pole()
print('''чтобы сделать ход нужно ввести 2 числа через пробел. 1-е число - номер строки, 2-е - номер столбика''')
e = a._n ** 2 - a._m
while a.is_alive == True and a.hode <= e - 1:
    v = input('ваш ход: ')
    a1, b = '1','2'
    while len(v.split())!=2 or a1.isdigit()==False or b.isdigit()==False:
        print('неправильный синтакс хода')
        v = input('ваш ход: ')
        if len(v.split())==2:
            a1, b = v.split()
    a1,b = v.split()
    a1, b = int(a1) - 1, int(b) - 1
    while not 0 <= a1 <= a._n - 1 or not 0 <= b <= a._n:
        print('такой клетки нет на поле')
        v = input('ваш ход: ')
        a1, b = v.split()
        a1, b = int(a1) - 1, int(b) - 1
    a.hod(a1, b)
if a.is_alive == False:
    for i in range(a._n):
        a.pole[i] = [g for g in ''.join(map(str,a.pole[i])).replace('*','❗')]
    a.show()
    print('игра окончена')
elif a.hode >= e:
    for i in range(a._n):
        a.pole[i] = [g for g in ''.join(map(str,a.pole[i])).replace('*','❗')]
    a.show()
    print('вы победили!')