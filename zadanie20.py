class Node:
   def __init__(self, el1 = None,el2= None):
      self.next = None
      self.el1 = el1
      self.el2 = el2


class lista():
    def __init__(self):
        self.head = None
    def wyswietl(self): 
        licznik = self.head
        print(licznik.el1,licznik.el2, end=",")
        while licznik.next != None:
            print(licznik.next.el1,licznik.next.el2 , end=",")
            licznik = licznik.next
        print("")


    def append(self, el1,el2):
        dostawiany = Node(el1,el2)
        if self.head is None:
            self.head = dostawiany
            return
        zmienna = self.head
        while zmienna.next != None:
            poprzednik = zmienna
            zmienna = zmienna.next
        zmienna.next = dostawiany



    def redukuj(self):
        if self.head is None:
            return
        act = self.head
        while act != None:
            Flag = False
            prev = act
            p = act.next
            while p is not None:
                if act.el1 < p.el1 and act.el2 <= p.el2 and act.el2>= p.el1:
                    act.el2 = p.el2
                    Flag = True
                if p.el1 < act.el1 and p.el2 <= act.el2 and act.el1 < p.el2:
                    act.el1 = p.el1
                    Flag = True
                if Flag:
                    prev.next = p.next
                    p = p.next
                if not Flag: 
                    prev = p 
                    p = p.next
                Flag = False
                
            act = act.next


tablica = lista()
tablica.append(15,19)
tablica.append(2,5)
tablica.append(7,11)
tablica.append(8,12)
tablica.append(5,6)
tablica.append(13,17)
tablica.redukuj()
tablica.wyswietl()

