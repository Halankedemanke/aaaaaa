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
    def długosc(self):
        if self.head.val == None:
            return 0
        else:
            zmien = self.head
            licznik = 1
            while zmien.next != None:
                zmien = zmien.next
                licznik += 1
            return licznik

    
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
    def zwroc(self,i):
        if self.head.val == None:
            return
        if i < 1 or i > Lista.długosc:
            return
        zmienna = self.head
        licznik = 1
        while licznik != i:
            zmienna = zmienna.next
            licznik += 1
        return zmienna.val
    def podstaw(self,i,value):
        if self.head.val == None:
            return
        if i < 1 or i > self.długosc():
            return
        zmienna = self.head
        licznik = 1
        while licznik != i:
            zmienna = zmienna.next
            licznik += 1
        zmienna.val = value


                


        


tablica = Lista()
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(7)
tablica.dodaj(6)
tablica.dodaj(5)
tablica.dodaj(4)
tablica.wyswietl()
tablica.zamien()
print(';')
tablica.wyswietl()
            
            