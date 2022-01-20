def rek(t, i = 0, steps = 0, s1 = 0, s2 = 0):
    if i == len(t):
        if s1 == s2 and steps >= 2:
            print(steps)
            return True
    if i >= len(t):
        return False
    
    if s1 == s2:
        a = rek(t, i+1, steps + 1,t[i], s2)
        else:
            return rek(t, i+1, steps ,s1,s2 + t[i])
    if rek(t, i+1, steps + 1, t[i], s2):
        return True
    return rek(t,i+1, 0 ,s1 + t[i],s2)
    


    
    

tab = [1,2,3,1,5,2,2,2,6]
print(rek(tab))

