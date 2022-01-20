best = 0
def rek(t, i= 1, steps = 0, , s2 = 0):
    global best
    if i == len(t)-1:
        if s1 == s2 and s1 != 0:
            best = max(steps,best)
            return True
        return False
    a = rek(t, i+1, steps + 2,s1, s2 + t[i])
    if not a:
        a = rek(t, i+1, steps, s1+ t[i], s2= 0)
    else:
        return s1


    if s1 == s2:
        return rek(t, i+1, steps + 2,s2, t[i])
    else:
        return rek(t, i+1, steps + 2,s1, s2 + t[i])

      






t = [1,2,3,1,3,2,6,6]
print(rek(t))
print(best)