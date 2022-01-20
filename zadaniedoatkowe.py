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

def pousuwaj(a):
    if a is None:
        return 
    prev = Wezel()
    tmp = a
    prev.next = a
    w = prev
    while tmp.next is not None:
        if tmp.next.val%tmp.val == 0:
            prev.next = tmp.next
            tmp = tmp.next
        else:
            prev = tmp
            tmp = tmp.next
    return w.next

w = Lista()
w.dodaj(7)
w.dodaj(14)
w.dodaj(7)
w.dodaj(17)
w.dodaj(34)
w.dodaj(17)

a = w.head
c = pousuwaj(a)
while c is not None:
    print(c.val)
    c = c.next
