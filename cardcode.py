# -*- coding: utf-8 -*-
"""
Auther: yaccDL
program:cardcode.py
Description: a new DL code method to define card by number, simplify the operation
"""

class cardcode():
    def __init__(self, regentCode):
         self.regent = regentCode
#    def __init__(self):
#        return

    def code(self, card):
        cardFlower = {'D':0,'C':1,'H':2,'S':3,'J':4}
        a=card[0]
        b=int(card[1:])
        if b==1:
            b=b+13
        elif b==2:
            return 8000+cardFlower[a]
        
        if a=='J':
            return 9000+(b+10)*10
        else:
            return cardFlower[a]*1000+b*10
    
    def card(self, code):
        a=[]
        b=""
        t=code//1000
        n=code%1000//10
        if t==0:
            a.append('D')
            a.append(str(n))
            return b.join(a)
        elif t==1:
            a.append('C')
            a.append(str(n))
            return b.join(a)
        elif t==2:
            a.append('H')
            a.append(str(n))
            return b.join(a)
        elif t==3:
            a.append('S')
            a.append(str(n))
            return b.join(a)
        elif t==8:
            a.append('J')
            a.append(str(n))
            return b.join(a)
        else:
            return 'wrong'

    def imagePath(self, code):
        image_name = self.card(code)
        return 'img/' + image_name + '.png'

    def graphy(self, code):
        pokerlist =(' ',' ',' ','3','4','5','6','7','8','9','10','J','Q','K','A')
        flowerList={0:'♦ ',1:'♣ ',2:'♥ ',3:'♠ ',4:'♦ ',5:'♣ ',6:'♥ ',7:'♠ '}
        a=[]
        b=""
        t=code//1000
        n=code%1000//10
        tt=code%10

        if t==8:
            a.append(flowerList[tt])
            a.append('2')
            return b.join(a)
        elif t==9:
            #now the permanent master card are not considered
            if n==14:
                a.append('JK')
                return b.join(a)
            elif n==13:
                a.append('jk')
                return b.join(a)
        else:
            l=pokerlist[n]
            a.append(flowerList[t])
            a.append(l)
            return b.join(a)
"""
        if n<3 and n>0:
            n=n+13
        elif n==0:
            return None
        l=pokerlist[n]

        if t==0:
            a.append('♦')
            a.append(l)
            return b.join(a)
        elif t==1:
            a.append('♣')
            a.append(l)
            return b.join(a)
        elif t==2:
            a.append('♥')
            a.append(l)
            return b.join(a)
        elif t==3:
            a.append('♠')
            a.append(l)
            return b.join(a)
        elif t==8:
            a.append('♠')
            a.append(l)
            return b.join(a)
        elif t==9:
            if l=='2':
                #Senior Joker
                a.append('JK')
            else:
                a.append('jk')
            return b.join(a)
        else:
            return None                    
"""

