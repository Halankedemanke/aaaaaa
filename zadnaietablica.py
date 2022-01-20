def czydotre(tab,w = 0,k = 0):
    if w == len(tab) - 1:
        return True
    tabruchy = [(1,2),(1,-2),(2,-1),(2,1)]
    if w == 0:
        if tab[w][k]:
           return czydotre(tab,w,k+ 1)
    if k > len(tab)-1:
        return False
    for w1,k1 in tabruchy:
        if 0 <= w + w1 <= len(tab) -1 and 0 <= k + k1 <= len(tab) -1:
            if not tab[w+w1][k+k1]:
                tab[w+w1][k+k1] = True
                if czydotre(tab,w + w1,k + k1):
                    print(w+w1,k+k1)
                    return True
                tab[w+w1][k+k1] = False
    return False
                
Tab = [[True,False,True,True,False],
[False,False,True,True,False],
[True,False,True,True,False],
[False,False,True,True,False],
[False,False,False,True,False]]

print(czydotre(Tab))