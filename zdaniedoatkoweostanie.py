from enum import Flag


def szukajwspolnego(a,b):
    zm1 = a
    zm2 = b
    flag = False
    while zm2 is not None:
        while zm1 is not None:
            if zm1.next is zm2:
                c = zm2
                d = zm1
                zm1.next = None
                flag = True
                break
            zm1 = zm1.next
        if flag:
            break
        zm1 = a
        zm2 = zm2.next
    if not Flag:
        return
    while c is not None:
        d.next = wezel(c.val)
        d = d.next
        c = c.next


        