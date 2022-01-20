class wezel():
    def __init__(self, dane = None):
        self.val = dane
        self.next = None

def system_trójkowy(a):
    dwa = 0
    jeden = 0
    while a != 0:
        if a%3 == 1:
            jeden += 1
        if a%3 == 2:
            dwa += 1
        a//=3
    if jeden > dwa:
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
    
    def usun(self):
        if self.head == None:
            return
        if  system_trójkowy(self.head.val):
            self.head = self.head.next
        zmienna = self.head
        while zmienna.next != None:
            poprzednik = zmienna
            zmienna = zmienna.next
            if system_trójkowy(zmienna.val):
                poprzednik.next = zmienna.next
tablica = Lista()
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(7)
tablica.dodaj(6)
tablica.dodaj(5)
tablica.dodaj(4)
tablica.wyswietl()
tablica.usun()
print(';')
tablica.wyswietl()
            