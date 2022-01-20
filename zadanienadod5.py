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

def unikalne(tablica):
    z1 = tablica.head
    if z1 is None:
        return
    prev = Wezel()
    prev.next = z1
    a = prev
    while z1 is not None:
        c = z1.next
        flaga = False
        prevc = z1
        while c is not None:
            if c.val == z1.val:
                prevc.next = c.next
                c = c.next
                flaga = True
            else:
                prevc = c
                c = c.next
        if flaga:
            prev.next = z1.next
        else:
            prev = z1
        z1 = z1.next
    tablica.head = a.next
    return tablica

w = Lista()
w.dodaj(7)
w.dodaj(8)
w.dodaj(7)
w.dodaj(17)
w.dodaj(20)
w.dodaj(17)

unikalne(w).wyswietl()

        
