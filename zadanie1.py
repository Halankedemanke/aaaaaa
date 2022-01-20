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
    
    def szukaj(self, dane):
        szukany = dane
        if self.head == None:
            return False
        zmienna = self.head
        while zmienna.next != None:
            if zmienna.val == szukany:
                return True
            if zmienna.next == None:
                return False
            zmienna = zmienna.next

    def usun(self, dane):
        indeks = dane
        if self.head == None:
            print('pusta lista')
            return
        licz = 1
        tmp = self.head
        while tmp.next != None:
            poprzednik = tmp
            tmp = tmp.next
            if indeks == licz:
                poprzednik.next = tmp.next
                return 
            licz += 1
    
    def wyswietl(self):
        print(self.head.val)
        zmienna = self.head
        while zmienna.next != None:
            zmienna = zmienna.next
            print(zmienna.val)


lista = Lista()
lista.dodaj(4)
lista.dodaj(6)
lista.dodaj(8)
lista.wyswietl()
lista.usun(3)
lista.wyswietl()