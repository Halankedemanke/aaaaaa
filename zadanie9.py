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
    
    def zwieksz(self):
        zmienna = self.head
        indeks = 1
        flag = False
        if zmienna == None:
            self.head.val = 1
        else:
            i = 1
            while zmienna.next != None:
                poprzednik = zmienna
                zmienna = zmienna.next
                indeks += 1
            if zmienna.val < 9:
                zmienna.val += 1
                return
            zmienna.val = 0
            while True:
                new_indeks = 1
                poczatek = self.head
                while new_indeks != indeks - i:
                    poczatek = poczatek.next
                    new_indeks += 1
                if poczatek.val <9 and indeks-i > 1:
                    if poczatek.val <= 8:
                        poczatek.val += 1
                        return
                elif poczatek.val == 9 and indeks - i <= 1:
                    tablica.dodaj(0)
                    self.head.val = 1
                    return
                poczatek.val = 0
                if indeks - i - 1 > 0:
                    i += 1
tablica = Lista()
tablica.dodaj(9)
tablica.dodaj(9)
tablica.dodaj(9)
tablica.dodaj(9)
tablica.dodaj(9)
tablica.dodaj(9)
tablica.wyswietl()
tablica.zwieksz()
tablica.wyswietl()
            
            



                