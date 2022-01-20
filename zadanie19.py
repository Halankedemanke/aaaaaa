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
tablica.dodaj(2)
tablica.dodaj(3)
tablica.dodaj(6)
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(9)
tablica.wyswietl()
print('[')
tablica.usunsupilkat()
tablica.wyswietl()