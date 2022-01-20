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
            poprzednik = zmienna
            zmienna = zmienna.next
        zmienna.next = self.head
    def znjadz(self):
        zmienna = self.head
        zmienna2 = self.head.next.next
        if self.head.val == None:
            return False
        napis = ''
        while zmienna.next is not None and zmienna2.next.next is not None:
            if zmienna == zmienna2.next.next:
                zmienna3 = zmienna2.next.next
                licznik = 0
                while zmienna.next != zmienna3:
                    zmienna = zmienna.next
                    napis+= str(zmienna) + str(zmienna2)
                while str(self.head) not in napis:
                    self.head = self.head.next
                    licznik += 1
                return licznik
            zmienna = zmienna.next
            zmienna2 = zmienna2.next.next
        return False

def elementprzed(tablica):
    if tablica.head == None:
        return False
    else:
        zm1 = tablica.head
        zm2 = tablica.head.next.next
        while zm1 != zm2 or zm2 == None or zm1 == None:
            zm1 = zm1.next
            zm2 = zm2.next.next
        if zm1 == zm2 and zm1 != None:
            b = zm1.next
            zm1.next = None
        prev = Wezel()
        prev.next = tablica.head
        w = tablica.head
        a = b
        while True:
            while a is not None:
                if a == w:
                    return prev.val
                a = a.next
            w = w.next
            prev = prev.next
            a = b
w = Lista()
w.dodaj(9)
w.dodaj(8)
w.dodaj(7)
w.dodaj(10)
w.dodaj(20)
w.dodaj(17)
c = w.head
while c.next is not None:
    if c.val == 7:
        a = c
    c = c.next
c.next = a

print(elementprzed(w))



