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
        if self.head == None:
            return False
        while zmienna.next is not None and zmienna2.next.next is not None:
            if zmienna == zmienna2:
                return True
            zmienna2 =zmienna2.next.next
            zmienna = zmienna.next
            
        return False
    
    
tablica = Lista()
tablica.dodaj(2)
tablica.dodaj(3)
tablica.dodaj(6)
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(9)
tablica.cykl()
print(tablica.znjadz())
