class wezel():
    def __init__(self,val = None):
        self.val = val
        self.next = None
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
    
    def szukaj(self, i):
        dane = wezel()
        dane.val = i
        if self.head.val == None:
            return
        if self.head.val != i:
            zmienna = self.head
            while zmienna.next != None:
                poprzednik = zmienna
                zmienna = zmienna.next
                if zmienna.val == i:
                    poprzednik.next = zmienna.next
                    return
            zmienna.next = dane
        elif self.head.val == i and self.head != None:
            self.head = self.head.next
        elif self.head == i and self.head.next == None:
            self.head = None
tablica = Lista()
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(7)
tablica.dodaj(6)
tablica.dodaj(5)
tablica.dodaj(4)
tablica.wyswietl()
tablica.szukaj(2)
print(';')
tablica.wyswietl()
            
dd