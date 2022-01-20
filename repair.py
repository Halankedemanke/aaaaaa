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
    



def repair(tablica):
    z1 = tablica.head
    roznica = 100000000000000
    while z1.next is not None:
        if abs(z1.next.val - z1.val) < abs(roznica):
            roznica = z1.next.val - z1.val
        z1 = z1.next
    tmp = tablica.head
    while tmp.next is not None:
        while abs(tmp.next.val - tmp.val) != abs(roznica):
            a = wezel(tmp.val + roznica)
            a.next = tmp.next
            tmp.next = a
            tmp = tmp.next
        tmp = tmp.next

    return tablica

tablica = Lista()
tablica.dodaj(2)
tablica.dodaj(0)
tablica.dodaj(-2)
tablica.dodaj(-16)
repair(tablica)
tablica.wyswietl()