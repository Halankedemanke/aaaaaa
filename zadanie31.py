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

def jakniema(tablica1):
    p = Wezel()
    a = p
    prev = Wezel(None)
    curr = tablica1.head
    prev.next = curr
    licznik = 0
    while curr is not None:
        if curr.val%2 == 0 and curr.val > 0:
            prev = curr
            curr = curr.next
        elif curr.val%2 == 1 and curr.val < 0:
            a = curr
            prev.next = curr.next
            curr = curr.next
            a.next = p.next
            p.next = a
        else:
            prev.next = curr.next
            b = curr
            curr = curr.next
            b = None
            licznik+=1
    print(licznik)
    return p.next

tablica2 = Lista()
tablica2.head = jakniema(tablica1)
tablica2.wyswietl()
tablica1.wyswietl()
        





            