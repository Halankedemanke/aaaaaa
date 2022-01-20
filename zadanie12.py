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
            while zmienna.next is not None:
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
        poprzednik = None
        zmienna = self.head
        if self.head.val == None:
            return
        else:
            while zmienna != None:
                nastepnik = zmienna.next
                zmienna.next = poprzednik
                poprzednik = zmienna
                zmienna = nastepnik
            self.head = poprzednik
                


        


tablica = Lista()
tablica.dodaj('c')
tablica.dodaj('b')
tablica.dodaj('c')
tablica.dodaj('d')
tablica.dodaj('w')

def dzielto(tablica, b):
    a = tablica.head
    licznik = 1
    while a.next is not None:
        if a.val == b[0]:
            c = a
            i = 0
            while c.val == b[i] and i <= len(b) - 1 and c is not None:
                c = c.next
                i += 1
                if str(c.val) == b[i] and i == len(b) - 1 and c is not None:
                    return True
        a = a.next
        licznik += 1
    i = 0
    while i <= len(b) - 1:
        a.next = wezel(b[i])
        i += 1
        a = a.next
        licznik += 1

    return licznik
t = 'wujek'
print(dzielto(tablica, t ))
    