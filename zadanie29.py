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
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(7)
tablica.dodaj(6)
tablica.dodaj(5)
tablica.dodaj(4)

tablica1.dodaj(2)
tablica1.dodaj(9)
tablica1.dodaj(5)
tablica1.dodaj(7)
tablica1.dodaj(11)

def jakniema(tablica1, tablica2):
    zmienna1 = tablica1.head
    zmienna2 = tablica2.head
    licznik = 0
    if zmienna2 is not None and zmienna1 is not None:
        while True:
            if zmienna2 is None or zmienna1 is None:
                return licznik
            while zmienna2.val >= zmienna1.val and zmienna1 != None:
                if zmienna2.val == zmienna1.val:
                    licznik += 1
                zmienna1 = zmienna1.next
                if zmienna1 is None:
                    break
            tablica2.head = tablica2.head.next
            zmienna2 = tablica2.head
            zmienna1 = tablica.head
        return licznik
            

print(jakniema(tablica,tablica1))
            
