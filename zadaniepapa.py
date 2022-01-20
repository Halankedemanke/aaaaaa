def znajdzpierw(tablica):
    a = tablica.head
    if a is None or a.next is None or a.next.next is None:
        return False
    z1 = a
    z2 = a.next.next
    while z1 is not None and z2.next is not None and z2.next.next is not None:
        if z1 == z2:
            break
        z1 = z1.next
        z2 = z2.next.next
    a = z1.next
    z1.next = None
    tmp = tablica.head
    while True:
        while tmp is not None:
            if tmp.next == a:
                return tmp.val
            tmp = tmp.next
        a = a.next
        tmp = tablica.head

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
        
    def cykl(self):
        if self.head.val == None:
            return
        zmienna = self.head
        while zmienna.next != None:
            if zmienna.val == 6:
                b = zmienna
            poprzednik = zmienna
            zmienna = zmienna.next
        zmienna.next = b

tablica = Lista()
tablica.dodaj(2)
tablica.dodaj(3)
tablica.dodaj(6)
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(9)
tablica.cykl()
print(znajdzpierw(tablica))

            
