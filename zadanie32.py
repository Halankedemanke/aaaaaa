class Wezel:
    def __init__(self, val=None):
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

    def usunsupilkat(self):
        duplikaty = {}
        poprzednik = None
        zmienna = self.head
        while zmienna != None:
            if zmienna.val in duplikaty:
                duplikaty[zmienna.val] = 'XDD'
            else:
                duplikaty[zmienna.val] = 'X'
            poprzednik = zmienna
            zmienna = zmienna.next
        zmienna = self.head
        poprzednik = None
        while zmienna != None:
            if duplikaty[zmienna.val] == 'XDD':
                poprzednik.next = zmienna.next
                poprzednik = poprzednik
            else:
                poprzednik = zmienna
            zmienna = zmienna.next


tablica = Lista()
tablica1 = Lista()
tablica.dodaj(-9)
tablica.dodaj(8)
tablica.dodaj(-7)
tablica.dodaj(6)
tablica.dodaj(-5)
tablica.dodaj(4)

tablica1.dodaj(2)
tablica1.dodaj(-3)
tablica1.dodaj(-5)
tablica1.dodaj(-7)
tablica1.dodaj(12)


def wielommian(tablica1, tablica):
    p = Wezel(None)
    p1 = None
    p2 = None
    z1 = tablica1.head
    z2 = tablica.head
    while z1 is not None:
        a = z1.next
        z1.next = p1
        p1 = z1
        z1 = a
    tablica1.head = p1
    while z2 is not None:
        b = z2.next
        z2.next = p2
        p2 = z2
        z2 = b
    tablica.head = p2
    z1 = p1
    z2 = p2
    while z1 is not None and z2 is not None:
        a = p
        p = Wezel(z1.val + z2.val)
        p.next = a
        z1 = z1.next
        z2 = z2.next
    if z1 is not None:
        while z1 is not None:
            a = p
            p = Wezel(z1.val)
            p.next = a
            z1 = z1.next
    if z2 is not None:
        while z2 is not None:
            a = p
            p = Wezel(z2.val)
            p.next = a
            z2 = z2.next
    return p


t = wielommian(tablica1, tablica)
while t != None:
    print(t.val)
    t = t.next




