import tkinter as tk
import random as rd
import time


class gamepole():
    def int(self,a, n, m=17):
        self.t = tk.Tk()
        self.t.geometry('700x500+700+200')
        self.t.title('сапер')
        self._n = n
        self._m = round(n ** 2 / 100 * m)
        self.is_alive = True
        self.is_flag=[[False for i in range(self._n)] for i in range(self._n)]
        self.kolvo_flagov=0
        self.beznal = True
        self.infoobigre = tk.Label(self.t, text=f'мины: {self._m}',font=('Calibri',15))
        self.infoobigre1=tk.Label(self.t, text=f'флаги: {self.kolvo_flagov}',font=('Calibri',15))
        self.infoobigre2=tk.Label(self.t, text='статус игры: продолжается',font=('Calibri',15))
        self.infoobigre3 = tk.Label(self.t, text='легкий старт:', font=('Calibri', 15))
        self.infoobigre4 = tk.Button(self.t, text='вкл', font=('Calibri', 15))
        self.infoobigre.place(x=self._n*35,y=0)
        self.infoobigre1.place(x=self._n * 35, y=25)
        self.infoobigre2.place(x=self._n * 35, y=50)
        self.infoobigre3.place(x=self._n * 35, y=75)
        self.infoobigre4.place(x=self._n * 35+125, y=80,width=50,heigh=25)
        self.infoobigre4.bind('<ButtonPress>',lambda event:a.bezopasnoe_nachalo())
        self.chity=tk.Button(self.t, text='читы',font=('Arial',15))
        self.chity.place(width=50,height=25,relx=1.0, rely=1.0, anchor="se")
        self.hode = 0
        self.cvet_otritoy='lightgray'
        self.cvet_zakritoy='white'
        self.obnova = tk.Button(self.t, text='начать заного', font=('Calibri', 15))
        self.obnova.place(relx=1.0, rely=0.0, anchor="ne", width=150, heigh=30)
        self.obnova.bind('<ButtonPress>', lambda event: a.igratb_snova(a))
        self.pole = [[0 for i in range(self._n)] for i in range(self._n)]
        self.olp = [[] for i in range(self._n)]
        c, c1 = 0, 0
        for i in range(self._n):
            for g in range(self._n):
                l = tk.Button(self.t, text='',font=('Arial',18),bg=self.cvet_zakritoy)
                l.place(x=c1, y=c, width=35, height=35)
                l.bind("<Button-1>", lambda event, i1=i, g1=g: a.init(i1, g1,a))
                l.bind("<Button-3>", lambda event, i1=i, g1=g: a.flag(i1, g1))
                self.olp[i].append(l)
                c1 += 35
            c += 35
            c1 = 0
        self.chity.bind("<Button-1>", lambda event: a.cheats())
    def init(self,a1,b1,a):
        for i in range(self._m):
            a2 = rd.randint(0, self._n - 1)
            b = rd.randint(0, self._n - 1)
            if self.beznal==True:
                ab=str(a2)+str(b)
                while self.pole[a2][b] == '💣' or str(a1) + str(b1) == ab or str(a1 + 1) + str(b1) == ab or str(a1 + 1) + str(b1 + 1) == ab or str(
                            a1 + 1) + str(b1 - 1) == ab or str(a1) + str(b1 + 1) == ab or str(a1) + str(
                            b1 - 1) == ab or str(a1 - 1) + str(b1 - 1) == ab or str(a1 - 1) + str(b1) == ab or str(
                            a1 - 1) + str(b1 + 1) == ab:
                    a2 = rd.randint(0, self._n - 1)
                    b = rd.randint(0, self._n - 1)
                    ab = str(a2) + str(b)
            else:
                while self.pole[a2][b] == '💣':
                    a2 = rd.randint(0, self._n - 1)
                    b = rd.randint(0, self._n - 1)
            self.pole[a2][b] = '💣'
            if 0 < b < self._n - 1:
                if self.pole[a2][b - 1] != '💣':
                    self.pole[a2][b - 1] += 1
                if self.pole[a2][b + 1] != '💣':
                    self.pole[a2][b + 1] += 1
                if 0 < a2 < self._n - 1:
                    if self.pole[a2 - 1][b - 1] != '💣':
                        self.pole[a2 - 1][b - 1] += 1
                    if self.pole[a2 - 1][b + 1] != '💣':
                        self.pole[a2 - 1][b + 1] += 1
                    if self.pole[a2 + 1][b - 1] != '💣':
                        self.pole[a2 + 1][b - 1] += 1
                    if self.pole[a2 + 1][b + 1] != '💣':
                        self.pole[a2 + 1][b + 1] += 1
                elif a2 > 0:
                    if self.pole[a2 - 1][b - 1] != '💣':
                        self.pole[a2 - 1][b - 1] += 1
                    if self.pole[a2 - 1][b + 1] != '💣':
                        self.pole[a2 - 1][b + 1] += 1
                elif a2 < self._n:
                    if self.pole[a2 + 1][b - 1] != '💣':
                        self.pole[a2 + 1][b - 1] += 1
                    if self.pole[a2 + 1][b + 1] != '💣':
                        self.pole[a2+ 1][b + 1] += 1
            elif b > 0:
                if self.pole[a2][b - 1] != '💣':
                    self.pole[a2][b - 1] += 1
                if 0 < a2 < self._n - 1:
                    if self.pole[a2 - 1][b - 1] != '💣':
                        self.pole[a2 - 1][b - 1] += 1
                    if self.pole[a2 + 1][b - 1] != '💣':
                        self.pole[a2 + 1][b - 1] += 1
                elif a2 > 0:
                    if self.pole[a2 - 1][b - 1] != '💣':
                        self.pole[a2 - 1][b - 1] += 1
                elif a2 < self._n:
                    if self.pole[a2 + 1][b - 1] != '💣':
                        self.pole[a2 + 1][b - 1] += 1
            elif b < self._n - 1:
                if self.pole[a2][b + 1] != '💣':
                    self.pole[a2][b + 1] += 1
                if 0 < a2 < self._n - 1:
                    if self.pole[a2 - 1][b + 1] != '💣':
                        self.pole[a2 - 1][b + 1] += 1
                    if self.pole[a2 + 1][b + 1] != '💣':
                        self.pole[a2 + 1][b + 1] += 1
                elif a2 > 0:
                    if self.pole[a2 - 1][b + 1] != '💣':
                        self.pole[a2 - 1][b + 1] += 1
                elif a2 < self._n:
                    if self.pole[a2 + 1][b + 1] != '💣':
                        self.pole[a2 + 1][b + 1] += 1

            if 0 < a2 < self._n - 1:
                if self.pole[a2 + 1][b] != '💣':
                    self.pole[a2 + 1][b] += 1
                if self.pole[a2 - 1][b] != '💣':
                    self.pole[a2 - 1][b] += 1
            elif a2 > 0:
                if self.pole[a2 - 1][b] != '💣':
                    self.pole[a2 - 1][b] += 1
            elif a2 < self._n - 1:
                if self.pole[a2 + 1][b] != '💣':
                    self.pole[a2 + 1][b] += 1
        for i in range(self._n):
            for g in range(self._n):
                if self.pole[i][g]==0:
                    self.pole[i][g]=' '
        for i in range(self._n):
            for g in range(self._n):
                self.olp[i][g].bind("<Button-1>", lambda event, i1=i, g1=g: a.hod(i1, g1,a))
        a.hod(a1,b1,a)
        self.vremya_igri = time.time()
    def cheats(self):
        for i in range(self._n):
            for g in range(self._n):
                if self.pole[i][g] == '💣':
                    self.olp[i][g]['text'] = '💣'
    def igratb_snova(self,aa):
        self.is_alive = True
        self.kolvo_flagov = 0
        self.hode = 0
        self.is_flag = [[False for i in range(self._n)] for i in range(self._n)]
        self.infoobigre1['text'] = f'флаги: {self.kolvo_flagov}'
        self.infoobigre2['text']='статус игры: продолжается'
        self.vremya_igri=time.time()
        for i in range(self._n):
            for g in range(self._n):
                self.olp[i][g]['text']=''
                self.olp[i][g]['bg']=self.cvet_zakritoy
                self.pole=[[0 for i in range(self._n)] for i in range(self._n)]
                self.olp[i][g].bind("<Button-1>", lambda event, i1=i, g1=g: aa.init(i1, g1,aa))
                self.olp[i][g].bind("<Button-3>", lambda event, i1=i, g1=g: aa.flag(i1, g1))

    def hod(self, a, b,aa):
        if self.is_flag[a][b] == False:
            if self.olp[a][b]['text'] == ' ':
                return 0
            if self.olp[a][b]['text']==self.pole[a][b] and self.olp[a][b]['text']!='':
                c = 0
                c1=list()
                try:
                    if self.olp[a][b+1]['text'] =='🏳':
                        c+=1
                    elif self.olp[a][b+1]['text'] =='':
                        c1.append((a,b+1))
                except IndexError:
                    pass
                try:
                    if self.olp[a+1][b+1]['text'] =='🏳':
                        c+=1
                    elif self.olp[a+1][b+1]['text'] =='':
                        c1.append((a+1,b+1))
                except IndexError:
                    pass
                try:
                    if self.olp[a+1][b]['text'] =='🏳':
                        c+=1
                    elif self.olp[a+1][b]['text'] =='':
                        c1.append((a+1,b))
                except IndexError:
                    pass
                try:
                    if a>0 and self.olp[a-1][b+1]['text'] =='🏳':
                        c+=1
                    elif a>0 and self.olp[a-1][b+1]['text'] =='':
                        c1.append((a-1,b+1))
                except IndexError:
                    pass
                if a>0 and self.olp[a-1][b]['text'] =='🏳':
                    c+=1
                elif a>0 and self.olp[a-1][b]['text'] =='':
                    c1.append((a-1,b))
                if a>0 and b>0 and self.olp[a-1][b-1]['text'] =='🏳':
                    c+=1
                elif a>0 and b>0 and self.olp[a-1][b-1]['text'] =='':
                    c1.append((a-1,b-1))
                if b>0 and self.olp[a][b-1]['text'] =='🏳':
                    c+=1
                elif b>0 and self.olp[a][b-1]['text'] =='':
                    c1.append((a,b-1))
                try:
                    if b>0 and self.olp[a+1][b-1]['text'] =='🏳':
                        c+=1
                    elif b>0 and self.olp[a+1][b - 1]['text'] == '':
                        c1.append((a+1, b - 1))
                except IndexError:
                    pass
                if c==self.olp[a][b]['text']:
                    for i in c1:
                        aa.hod(i[0],i[1],aa)
                return 0
            self.olp[a][b]['text'] = self.pole[a][b]
            if self.olp[a][b]['text']=='💣':
                for i in range(self._n):
                    for g in range(self._n):
                        if self.pole[i][g] == '💣':
                            self.olp[i][g]['text'] = '💣'
                        self.olp[i][g].unbind('<Button-1>')
                        self.olp[i][g].unbind('<Button-3>')
                self.olp[a][b]['bg'] = 'red'
                self.infoobigre2[
                    'text'] = f'статус игры: {rd.choice(('поражение', 'ты умер', 'попытка была', 'взорвано'))}({round(time.time() - self.vremya_igri, 2)})'
                return 0
            self.olp[a][b]['bg'] = self.cvet_otritoy
            self.hode += 1
            if self.olp[a][b]['text'] == ' ':
                self.olp[a][b].unbind('<Button-1')
                d = list()
                d1 = list()
                c = 0
                e = 0
                for i in range(self._n):
                    for g in range(self._n):
                        if self.olp[i][g]['text'] == ' ':
                            e += 1
                while e > c:
                    try:
                        if self.olp[a + 1][b]['text'] != self.pole[a + 1][b]:
                            self.olp[a + 1][b]['text'] = self.pole[a + 1][b]
                            self.olp[a+1][b]['bg'] = self.cvet_otritoy
                            self.olp[a+1][b].unbind('<Button-1')
                            self.hode += 1
                            if self.olp[a + 1][b]['text'] == ' ':
                                d.append(a + 1)
                                d1.append(b)
                                c-= 1
                            if self.is_flag[a+1][b]:
                                self.kolvo_flagov -= 1
                                self.is_flag[a+1][b] = False
                    except IndexError:
                        ''
                    try:
                        if self.olp[a + 1][b + 1]['text'] != self.pole[a + 1][b + 1]:
                            self.olp[a + 1][b + 1]['text'] = self.pole[a + 1][b + 1]
                            self.olp[a+1][b+1]['bg'] = self.cvet_otritoy
                            self.hode += 1
                            if self.olp[a + 1][b + 1]['text'] == ' ':
                                d.append(a + 1)
                                d1.append(b + 1)
                                c-= 1
                            if self.is_flag[a+1][b + 1]:
                                self.kolvo_flagov -= 1
                                self.is_flag[a+1][b+1] = False
                    except IndexError:
                        ''
                    try:
                        if b > 0 and self.olp[a + 1][b - 1]['text'] != self.pole[a + 1][b - 1]:
                            self.olp[a + 1][b - 1]['text'] = self.pole[a + 1][b - 1]
                            self.olp[a+1][b-1]['bg'] = self.cvet_otritoy
                            self.hode += 1
                            if self.olp[a + 1][b - 1]['text'] == ' ':
                                d.append(a + 1)
                                d1.append(b - 1)
                                c-= 1
                            if self.is_flag[a+1][b - 1]:
                                self.kolvo_flagov -= 1
                                self.is_flag[a+1][b-1] = False

                    except IndexError:
                        ''
                    try:
                        if a > 0 and self.olp[a - 1][b]['text'] != self.pole[a - 1][b]:
                            self.olp[a - 1][b]['text'] = self.pole[a - 1][b]
                            self.olp[a-1][b]['bg'] = self.cvet_otritoy
                            self.hode += 1
                            if self.olp[a - 1][b]['text'] == ' ':
                                d.append(a - 1)
                                d1.append(b)
                                c-= 1
                            if self.is_flag[a-1][b]:
                                self.kolvo_flagov -= 1
                                self.is_flag[a-1][b] = False
                    except IndexError:
                        ''
                    try:
                        if a > 0 and self.olp[a - 1][b + 1]['text'] != self.pole[a - 1][b + 1]:
                            self.olp[a - 1][b + 1]['text'] = self.pole[a - 1][b + 1]
                            self.olp[a-1][b+1]['bg'] =self.cvet_otritoy
                            self.hode += 1
                            if self.olp[a - 1][b + 1]['text'] == ' ':
                                d.append(a - 1)
                                d1.append(b + 1)
                                c-= 1
                            if self.is_flag[a-1][b + 1]:
                                self.kolvo_flagov -= 1
                                self.is_flag[a-1][b+1] = False
                    except IndexError:
                        ''
                    try:
                        if a > 0 and b > 0 and self.olp[a - 1][b - 1]['text'] != self.pole[a - 1][b - 1]:
                            self.olp[a - 1][b - 1]['text'] = self.pole[a - 1][b - 1]
                            self.olp[a-1][b-1]['bg'] = self.cvet_otritoy
                            self.hode += 1
                            if self.olp[a - 1][b - 1]['text'] == ' ':
                                d.append(a - 1)
                                d1.append(b - 1)
                                c-= 1
                            if self.is_flag[a-1][b - 1]:
                                self.kolvo_flagov -= 1
                                self.is_flag[a-1][b-1] = False
                    except IndexError:
                        ''
                    try:
                        if self.olp[a][b + 1]['text'] != self.pole[a][b + 1]:
                            self.olp[a][b + 1]['text'] = self.pole[a][b + 1]
                            self.olp[a][b+1]['bg'] = self.cvet_otritoy
                            self.hode += 1
                            if self.olp[a][b + 1]['text'] == ' ':
                                d.append(a)
                                d1.append(b + 1)
                                c-= 1
                            if self.is_flag[a][b+1]:
                                self.kolvo_flagov-=1
                                self.is_flag[a][b+1]=False
                    except IndexError:
                        ''
                    try:
                        if b > 0 and self.olp[a][b - 1]['text'] != self.pole[a][b - 1]:
                            self.olp[a][b - 1]['text'] = self.pole[a][b - 1]
                            self.olp[a][b-1]['bg'] =self.cvet_otritoy
                            self.hode += 1
                            if self.olp[a][b - 1]['text'] == ' ':
                                d.append(a)
                                d1.append(b - 1)
                                c-= 1
                            if self.is_flag[a][b - 1]:
                                self.kolvo_flagov -= 1
                                self.is_flag[a][b-1] = False
                    except IndexError:
                        ''
                    if len(d) != 0 and len(d1) != 0:
                        a = d[0]
                        b = d1[0]
                        d.pop(0)
                        d1.pop(0)
                    e = 0
                    c+=1
                    for i in range(self._n):
                        for g in range(self._n):
                            if self.olp[i][g]['text'] == ' ':
                                e += 1
            self.infoobigre1['text']=f'флаги: {self.kolvo_flagov}'
            if self.hode==self._n*self._n-self._m:
                self.infoobigre2['text']=f'статус игры: победа({round(time.time()-self.vremya_igri,2)})'
                for i in range(self._n):
                    for g in range(self._n):
                        self.olp[i][g].unbind('<Button-1>')
                        self.olp[i][g].unbind('<Button-3>')
    def bezopasnoe_nachalo(self):
        if self.beznal==True:
            self.beznal=False
            self.infoobigre4['text']='выкл'
        else:
            self.beznal=True
            self.infoobigre4['text']='вкл'
    def flag(self,a,b):
        if self.olp[a][b]['text']=='':
            self.olp[a][b]['text']='🏳'
            self.is_flag[a][b]=True
            self.kolvo_flagov+=1
            self.infoobigre1['text']=f'флаги: {self.kolvo_flagov}'
        elif self.olp[a][b]['text']=='🏳':
            self.olp[a][b]['text']=''
            self.is_flag[a][b]=False
            self.kolvo_flagov-=1
            self.infoobigre1['text']=f'флаги: {self.kolvo_flagov}'



b = gamepole()
b.int(b,10)


tk.mainloop()