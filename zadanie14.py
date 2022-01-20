class Wezel:
    def __init__(self,val = None):
        self.val = val
        self.next = None

class Lista:
    def __init__(self):
        self.head = Wezel()
    
    def dodaj(self, dane):
        dostawiany = Wezel(dane)
        if self.head.val == None:
            self.head = Wezel(dane)
            return
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
    
    def zmien(self):
        if self.head == None or self.head.next == None:
            return
        while self.head.next.val%self.head.val == 0:
            self.head = self.head.next
        tmp = self.head
        nastepnik = tmp.next
        while nastepnik is not None and nastepnik.next is not None:
            if nastepnik.next.val % nastepnik.val == 0:
                tmp.next = nastepnik.next
                nastepnik = tmp.next
            else:
                tmp = nastepnik
                nastepnik = nastepnik.next
tablica = Lista()
tablica.dodaj(2)
tablica.dodaj(3)
tablica.dodaj(6)
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(9)
tablica.wyswietl()
print('[')
tablica.zmien()
tablica.wyswietl()

