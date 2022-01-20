class wezel:
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
tablica1 = Lista()
tablica.dodaj(1)
tablica.dodaj(2)
tablica.dodaj(7)
tablica.dodaj(8)
tablica.dodaj(11)

tablica1.dodaj(1)
tablica1.dodaj(7)
tablica1.dodaj(9)
tablica1.dodaj(10)
tablica1.dodaj(11)

def usuzlity(z1,z2):
    if z1 is None or z2 is None:
        return 0
    licznik = 0
    tmp1 = z1
    tmp2 = z2
    g1 = wezel()
    g2 = wezel()
    g1.next = z1
    g2.next = z2
    p1 = g1
    p2 = g2
    while tmp1 is not None and tmp2 is not None:
        if tmp1.val < tmp2.val:
            p1 = tmp1
            tmp1 = tmp1.next
        elif tmp2.val < tmp1.val:
            p2 = tmp2
            tmp2 = tmp2.next
        else:
            tmp1 = tmp1.next
            p1.next = tmp1
            tmp2 = tmp2.next
            p2.next = tmp2
            licznik += 2
    z1 = g1.next
    z2 = g2.next
    return licznik


print(usuzlity(tablica.head,tablica1.head))
tablica1.wyswietl()
tablica.wyswietl()