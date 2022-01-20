class wezel:
    def __init__(self, dane = None):
        self.val = dane
        self.next = None


class Lista:
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
        if self.head.val == None:
            return
        else:
            poprzednik = None
            zmienna = self.head
            tmp = self.head
            while zmienna != None:
                poprzednik = zmienna
                zmienna = zmienna.next
                nastepnik = zmienna.next
                if system_ósemkowy(zmienna.val):
                    if zmienna.next == None:
                        return
                    poprzednik.next = nastepnik
                    zmienna.next = self.head
                    self.head = zmienna
                    zmienna = nastepnik
            self.head = tmp
                


        


tablica = Lista()
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(7)
tablica.dodaj(6)
tablica.dodaj(5)
tablica.dodaj(4)

tablica1 = Lista()
tablica1.dodaj(1)
tablica1.dodaj(7)
tablica1.dodaj(9)
tablica1.dodaj(10)
tablica1.dodaj(11)


def listki(t1,t2):
    z1 = t1.head
    z2 = t2.head
    g1 = wezel()
    g1.next = t1.head
    g2 = wezel()
    g2.next = t2.head
    p1 = None
    p2 = None
    licznik = 0
    if z1 is None or z2 is None:
        return 0
    while z2 is not None:
        if z2.val < z1.val:
            p2 = z2
            z2 = z2.next
        while z1 is not None and z2 is not None and z2.val>z1.val:
            p1 = z1
            z1 = z1.next
        if z1 is None:
            p2 = z2
            z2 = z2.next
            p1 = g1
            z1 = g1.next
        if z1.val == z2.val:
            licznik += 2
            if p1 is None:
                g1.next = t1.head.next
                t1.head = t1.head.next
            else:
                p1.next = z1.next
            if p2 is None:
                g2.next = t2.head.next
                t2.head = t2.head.next
            else:
                p2.next = z2.next
            z2 = z2.next
            z1 = g1.next
    return licznik

print(listki(tablica1,tablica))
            
        