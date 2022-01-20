class wezel:
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
tablica = Lista()
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(7)
tablica.dodaj(6)
tablica.dodaj(5)
tablica.dodaj(4)
    
def jgkjgkgjgkjj(a1):
    p1 = wezel()
    p2 = wezel()
    z1 = p1
    z2 = p2
    guardian = None
    if a1 is None:
        return False
    while a1 is not None:
        if a1.val%3 == 1:
            tmp = a1.next
            a1.next = None
            z1.next = a1
            z1 = z1.next
            a1 = tmp
        elif a1.val%3 == 2:
            tmp = a1.next
            a1.next = None
            z2.next = a1
            z2 = z2.next
            a1 = tmp
        elif a1.val%3 == 0:
            tmp = a1.next
            a1.next = None
            a1 = None
            a1 = tmp
    return p1.next.val

print(jgkjgkgjgkjj(tablica.head))