from typing import List


class wezel():
    def __init__(self, dane = None):
        self.val = dane
        self.next = None

def system_ósemkowy(a):
    piec = 0
    while a != 0:
        if a%8 == 5:
            piec += 1
        a//=8
    if piec%2 == 0:
        return True
    else:
        return False

class Lista():
    def __init__(self):
        self.head = wezel()

    def dodaj(self, dane):
        dostawiany = wezel(dane)
        if self.head.val == None:
            self.head = wezel(dane)
            return
        else:
            zmienna = self.head
            while zmienna.next != None:
                poprzednik = zmienna
                zmienna = zmienna.next
            zmienna.next = dostawiany
    
    def wyswietl(self):
        print(self.head.val)
        zmienna = self.head
        while zmienna.next != None:
            zmienna = zmienna.next
            print(zmienna.val)
    
    def zamien(self):
        poprzednik = None
        zmienna = self.head
        if self.head.val == None:
            return
        else:
            while zmienna != None:
                nastepnik = zmienna.next
                zmienna.next = poprzednik
                poprzednik = zmienna
                zmienna = nastepnik
            self.head = poprzednik
                


        


tablica = Lista()
tablica.dodaj(1)
tablica.dodaj(3)
tablica.dodaj(5)
tablica.dodaj(6)

tablica1 = Lista()
tablica1.dodaj(7)
tablica1.dodaj(8)
tablica1.dodaj(9)

def dzielto(a,b):
    if a == None:
        return b
    if b == None:
        return a
    if a.val < b.val:
        tmp = a
        a = a.next
        tmp.next = None
    else:
        tmp = b
        b = b.next
        tmp.next = None
    tmp.next = dzielto(a,b)

def dzieltoo(a,b):
    w = Lista()
    while a is not None and b is not None:
        if a.val < b.val:
            tmp = a
            a = a.next
            w.dodaj(tmp.val)
        else:
            tmp = b
            b = b.next
            w.dodaj(tmp.val)
    if a is None:
        while b is not None:
            w.dodaj(b.val)
            b = b.next
    if b is None:
        while a is not None:
            w.dodaj(a.val)
            a = a.next
    return w

dzieltoo(tablica.head, tablica1.head).wyswietl()