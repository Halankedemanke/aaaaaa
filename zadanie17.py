class Wezel:
    def __init__(self,val = None):
        self.prev = None
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
            zmienna = zmienna.next
        dostawiany.prev = zmienna.next
        zmienna.next = dostawiany
        
    
    def wyswietl(self):
        zmienna = self.head
        while zmienna != None:
            print(zmienna.val)
            zmienna.prev = zmienna
            zmienna = zmienna.next
    
  
    
    def alejaja(self):
        def jedynka(a):
            licznik = 0
            while a != 0:
                if a%2 == 1:
                    licznik += 1
                a//=2
            return licznik
        if self.head is None:
            return
        zmienna = self.head
        nastepnik = zmienna.next
        porzednik = zmienna.prev
        while zmienna.next != None:
            if jedynka(zmienna.val)%2 == 1:
                if zmienna is self.head:
                    self.head = zmienna.next
                if porzednik is not None:
                    porzednik.next = nastepnik
                if nastepnik is not None:
                    nastepnik.prev = porzednik
                zmienna = zmienna.next
                porzednik = porzednik
                nastepnik = zmienna.next
            else:
                porzednik = zmienna
                zmienna = zmienna.next
                nastepnik = zmienna.next
      

                


        

        
        
tablica = Lista()
tablica.dodaj(8)
tablica.dodaj(3)
tablica.dodaj(6)
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(9)
tablica.wyswietl()
print('[')
tablica.alejaja()
tablica.wyswietl()