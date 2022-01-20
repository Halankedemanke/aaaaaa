class Wezel:
    def __init__(self,val = None):
        self.val = val
        self.next = None

class Lista:
    def __init__(self):
        self.head = Wezel()
    
    def dodaj(self, dane):
        dostawiany = Wezel(dane)
        if self.head is None:
            self.head = dostawiany
            return
        zmienna = self.head
        while zmienna.next != None:
            poprzednik = zmienna
            zmienna = zmienna.next
        zmienna.next = dostawiany

    def usun(self):
        if self.head == None:
            print('pusta lista')
            return
        licz = 1
        tmp = self.head
        while tmp.next != None:
            poprzednik = tmp
            tmp = tmp.next
            if licz%2 == 0:
                poprzednik.next = tmp.next
                licz = 0
            licz += 1
    
    def wyswietl(self):
        print(self.head.val)
        zmienna = self.head
        while zmienna.next != None:
            zmienna = zmienna.next
            print(zmienna.val)
tablica = Lista()
tablica.dodaj(5)
tablica.dodaj(2)
tablica.dodaj(5)
tablica.dodaj(4)
tablica.dodaj(5)
tablica.dodaj(6)
tablica.wyswietl()
tablica.usun()
tablica.wyswietl()