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
def dwalancuchy(tablica1,tablica2):
    a = tablica1.head
    b = tablica2.head
    prev = None
    while b.next is not None:
        next = b.next
        b.next = prev
        prev = b
        b = next 
        next = b.next
    b.next = prev
    tablica2.head = b
    print(b.val , b.next.val)
    b = tablica2.head
    a = tablica1.head
    nowa_lista = Wezel()
    first = nowa_lista
    while b is not None or a is not None:
        if b is None:
            nowa_lista.next = a
            return first.next
        if a is None:
            nowa_lista.next = b
            return first.next
        if a.val > b.val:
            tmp = b.next
            b.next = None
            nowa_lista.next = b
            nowa_lista = nowa_lista.next
            b = tmp
        elif b.val > a.val:
            tmp = a.next
            a.next = None
            nowa_lista.next = a
            nowa_lista = nowa_lista.next
            a = tmp
        else:
            tmp = a.next
            tmp1 = b.next
            a.next = None
            b.next = None
            nowa_lista.next = a
            nowa_lista = nowa_lista.next
            a = tmp
            b = tmp1
    
    
    
tablica = Lista()
tablica.dodaj(9)
tablica.dodaj(8)
tablica.dodaj(7)
tablica.dodaj(6)
tablica.dodaj(5)
tablica.dodaj(4)
tablica1 = Lista()
tablica1.dodaj(1)
tablica1.dodaj(7)
tablica1.dodaj(9)
tablica1.dodaj(10)
tablica1.dodaj(11)
 
print(dwalancuchy(tablica1,tablica).val)


