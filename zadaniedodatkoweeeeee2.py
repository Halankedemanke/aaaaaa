from zadanie16 import wezel


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
        if self.head.val == None:
            return False
        napis = ''
        while zmienna.next is not None and zmienna2.next.next is not None:
            if zmienna == zmienna2.next.next:
                zmienna3 = zmienna2.next.next
                licznik = 0
                while zmienna.next != zmienna3:
                    zmienna = zmienna.next
                    napis+= str(zmienna) + str(zmienna2)
                while str(self.head) not in napis:
                    self.head = self.head.next
                    licznik += 1
                return licznik
            zmienna = zmienna.next
            zmienna2 = zmienna2.next.next
        return False


w = Lista()
w.dodaj(7)
w.dodaj(14)
w.dodaj(7)
w.dodaj(17)
w.dodaj(34)
w.dodaj(17)

def znajdznajdz(tablica):
    h = tablica.head
    c = Wezel()
    c.next = h
    k = tablica.head
    while k.next is not None:
        k = k.next
    k.next = wezel()
    k = k.next
    while h.next.val is not None:
        if h.val%2 == 0:
            a = h.next
            h.next = None
            k.next = h
            k = k.next
            c.next = a
            h = a
        else:
            c = h
            h = h.next
    h.next = h.next.next

    return tablica
        

znajdznajdz(w).wyswietl()