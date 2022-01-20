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
    
    def zmien(self):
        if self.head == None or self.head.next == None:
            return
        poprzednik = self.head
        zmienna = poprzednik.next
        while self.head.val < self.head.next.val:
            self.head = self.head.next
        while zmienna != None:
            if poprzednik.val > zmienna.val :
                poprzednik.next = zmienna.next
                zmienna = poprzednik.next
            else:
                poprzednik = zmienna
                zmienna = zmienna.next
            

               
                

        

tablica = Lista()
tablica.dodaj(2)
tablica.dodaj(3)
tablica.dodaj(6)
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(9)
tablica.wyswietl()
print('[')
tablica.zmien()
tablica.wyswietl()