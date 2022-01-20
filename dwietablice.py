maxi = 0
def dwiesumy(t1,t2, i = 0,suma1 = 0,suma2 = 0,k1 = 0, k2= 0):
    global maxi
    if suma1 == suma2 and k1 == k2:
        maxi = max(k1,maxi)
    if k1 > k2 + len(t2) or k2 > k1 + len(t1):
        return False
    if i >= len(t1) and i >= len(t2):
        return False
    if i <= len(t1) - 1 and k1 < k2 and i >= len(t2):
        return dwiesumy(t1,t2, i+1 ,suma1 + t1[i],suma2,k1+1, k2) or dwiesumy(t1,t2, i+1 ,suma1,suma2,k1, k2)
    if i <= len(t2) - 1 and k2 < k1 and i >= len(t1):
        return dwiesumy(t1,t2, i+1 ,suma1,suma2 + t2[i], k1, k2+1) or dwiesumy(t1,t2, i+1 ,suma1,suma2,k1, k2)
    if i < len(t1) and i < len(t2):
        return dwiesumy(t1,t2, i+1 ,suma1 + t1[i],suma2 + t2[i],k1 +1, k2+1) or dwiesumy(t1,t2, i+1 ,suma1 + t1[i],suma2,k1 +1, k2) or dwiesumy(t1,t2, i+1 ,suma1 ,suma2 + t2[i],k1, k2+1) or  dwiesumy(t1,t2, i+1 ,suma1,suma2,k1, k2)

t = [2,4,5,6,9,21,31,54,6,7]
t1 = [2,3,4,5,6,7,6,5,4,3,3]
dwiesumy(t,t1)
print(maxi)