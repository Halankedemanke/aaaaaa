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
tablica1 = Lista()
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(7)
tablica.dodaj(6)
tablica.dodaj(5)
tablica.dodaj(4)

tablica1.dodaj(4)
tablica1.dodaj(7)
tablica1.dodaj(9)
tablica1.dodaj(5)
tablica1.dodaj(4)
def lacz(tablica1,tablica2):
    zm1 = tablica1.head
    zm2 = tablica2.head
    while True:
        if zm1 == None:
            return True
        if zm1 == None:
            return False
        while zm1.val != zm2.val:
            zm2 = zm2.next
            if zm2 == None:
                return False
        zm1 = zm1.next
        zm2 = tablica2.head


    
        

print(lacz(tablica1,tablica))
