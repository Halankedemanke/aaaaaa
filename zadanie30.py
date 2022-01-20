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

tablica1.dodaj(2)
tablica1.dodaj(3)
tablica1.dodaj(5)
tablica1.dodaj(7)
tablica1.dodaj(11)
def lacz():
    global tablica1, tablica
    zmienna1 = tablica.head
    zmienna2 = tablica1.head
    while True:
        if zmienna1 == None:
            break
        zmienna = zmienna1 
        zmienna2 = tablica1.head
        zosia = False
        while zmienna.val >= zmienna2.val:
            if zmienna2.next == None:
                zmienna2.next = zmienna
                zosia = True
                break
            if zmienna.val == zmienna2.val:
                zosia = True
                break
            poprzednik = zmienna2
            zmienna2 = zmienna2.next
        zmienna1 = zmienna1.next
        if not zosia:
            if zmienna.val < zmienna2.val:
                poprzednik.next = zmienna
                zmienna.next = zmienna2
        
        

lacz()
tablica1.wyswietl()




