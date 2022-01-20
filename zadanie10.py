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
    
    def dlugosc(self):
        indeks = 1
        zmienna = self.head
        while zmienna.next != None:
            poprzednik = zmienna
            zmienna = zmienna.next
            indeks += 1
        return indeks
    
    def zwieksz(self):
        zmienna = self.head
        n = self.dlugosc()
        flag = False
        if zmienna == None:
            return zmienna
        else:
            while zmienna is not None:
                zmienna.val += 2*zmienna.val
                zmienna = zmienna.next
            i = 0
            while i != n:
                new_indeks = 1
                poczatek = self.head
                while new_indeks != n - i:
                    poprzednik =  poczatek
                    poczatek = poczatek.next
                    new_indeks += 1
                if n - i == 1:
                    if poczatek.val <= 9:
                        return
                    else:
                        a = Wezel(poczatek.val//10)
                        poczatek.val = poczatek.val%10
                        a.next = poczatek
                        self.head = a
                        return
                elif n-i > 1:
                    if poczatek.val >= 10:
                        poprzednik.val += poczatek.val//10
                        poczatek.val = poczatek.val%10
                i+=1


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