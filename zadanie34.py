
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
tablica.wyswietl()
tablica.zamien()
print(';')
tablica.wyswietl()

def znjadz(self):
    zmienna = self.head
    zmienna2 = self.head.next.next
    if self.head.val == None:
        return False
    while zmienna.next is not None and zmienna2.next.next is not None:
        if zmienna == zmienna2.next.next:
            zmienna3 = zmienna2.next.next
            break
        zmienna = zmienna.next
        zmienna2 = zmienna2.next.next
    tmp = zmienna3 
    tmp2 = zmienna.next
    tmp.next = None
    b = tmp2
    while True:
        kasia = True
        a = self.head
        while a != tmp2:
            prev = a
            a = a.next
            if a is None:
                kasia = False
                tmp2 = tmp2.next
                break
        if kasia:
            c = prev
            kasia = True
            break
    return c
    
        

