def pociecia(tab):
    suma = 0
    for val in tab:
        suma += val

    maxi = 0 

    for ciecie in range(2,len(tab)+1):
        if suma%ciecie == 0:
            ocaek = suma//ciecie
            cur = 0
            ciach = 1
            for i in range(len(tab)-1):
                cur += tab[i]
                if cur > ocaek:
                    break
                if cur == ocaek:
                    ciach += 1
                    cur = 0
                if cur == 0 and ciach == ciecie:
                    maxi = max(maxi,ciach)
        
    return maxi

print(pociecia([1,2,3,1,5,2,2,2,6]))