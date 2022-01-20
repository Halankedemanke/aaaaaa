class Wezel:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Lista:
    def __init__(self):
        self.head = None

    def dodaj(self, dane):
        dostawiany = Wezel(dane)
        if self.head is None:
            self.head = dostawiany
            return
        zmienna = self.head
        while zmienna.next is not None:
            zmienna = zmienna.next
        zmienna.next = dostawiany

    def usun(self):
        if self.head == None:
            print('pusta lista')
            return
        licz = 1
        tmp = self.head
        while tmp.next != None:
            poprzednik = tmp
            tmp = tmp.next
            if licz % 2 == 0:
                poprzednik.next = tmp.next
                licz = 0
            licz += 1

    def wyswietl(self):
        zmienna = self.head
        while zmienna is not None:
            print(zmienna.val)
            zmienna = zmienna.next


def sortuje(tablica):
    tab = [[] for _ in range(10)]
    if tablica.head.val == None:
        return
    zmienna = tablica.head
    while zmienna != None:
        tab[zmienna.val % 10].append(zmienna.val)
        zmienna = zmienna.next
    i = 0
    tmp = Lista()
    while i != 10:
        for el in tab[i]:
            tmp.dodaj(el)
        i += 1
    return tmp


def sortuj(tablica):
    if tablica.head is None:
        return 0
    prev = Wezel()
    tmp = tablica.head
    prev.next = tmp
    listka = Lista()
    i = 0
    while tablica.head is not None:
        while tmp is not None:
            if (tmp.val)%10 == i:
                listka.dodaj(tmp.val)
                prev.next = tmp.next
                a = tmp.next
                tmp.next = None
                if tmp is tablica.head:
                    if a is None:
                        return listka
                    tablica.head = a
                tmp = a
            else:
                prev = tmp
                tmp = tmp.next
        i += 1
        prev = Wezel()
        tmp = tablica.head
        prev.next = tmp
    return listka


tablica = Lista()
tablica.dodaj(55)
tablica.dodaj(23)
tablica.dodaj(5)
tablica.dodaj(44)
tablica.dodaj(45)
tablica.dodaj(16)
sortuj(tablica).wyswietl()