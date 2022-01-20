class wezel():
    def __init__(self, val=None):
        self.next = None
        self.val = val


class lista():
    def __init__(self):
        self.head = wezel()

    def dodaj(self, dane):
        if self.head.val is None:
            self.head = wezel(dane)
            return
        zmienna = self.head
        while zmienna.next != None:
            zmienna = zmienna.next
        zmienna.next = wezel(dane)

    def wyswietl(self):
        print(self.head.val)
        zmienna = self.head
        while zmienna.next != None:
            zmienna = zmienna.next
            print(zmienna.val)

    def szukaj(self):
        if self.head is None:
            return 0
        a = self.head
        b = self.head.next
        maxi = 0
        j = wezel()
        k = wezel()
        i = 1
        prev = 1
        while a is not None and b is not None:
            if a.val < b.val:
                c = a
                while b is not None and b.val > a.val:
                    a = b
                    b = b.next
                    i = i +1
                if i == maxi:
                    maxi = prev
                elif maxi < i:
                    prev = maxi
                    maxi = i
                    j = c
                    k = a
                i = 1
                a = a
                b = a.next
            else:
                a = b
                b = b.next
        if maxi != 1:
            prev = wezel()
            a = self.head
            tmp = self.head
            prev.next = tmp
            while tmp.next != None:
                if tmp == j:
                    prev.next = k.next
                    if j == self.head:
                        if k.next != None:
                            self.head = k.next
                        else:
                            return 0
                    return lista
                prev = tmp
                tmp = tmp.next


tablica = lista()
tablica.dodaj(7)
tablica.dodaj(3)
tablica.dodaj(6)
tablica.dodaj(2)
tablica.dodaj(8)
tablica.dodaj(9)
tablica.dodaj(2)
tablica.dodaj(8)
tablica.dodaj(9)
tablica.wyswietl()
print('[')
tablica.szukaj()
tablica.wyswietl()
            


            
            




