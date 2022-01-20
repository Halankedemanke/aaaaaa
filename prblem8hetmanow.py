tab1 = [0]*8
def hetmanow_8(T,t,i =0, hetmanow = 8):
    if hetmanow == 0 and i  == len(T) - 1:
        return True
    if i >= len(T):
        return False
    else:
        for k in range(i,8):
            for j in range(8):
                if t[j] == 0:
                    t[j] = 1
                    if hetmanow_8(T,t,i + 1, hetmanow - 1):
                        return True
                    t[j] = 0
                    
    return False

tab = [[1,2,3,4,5,6,7,8],
[1,2,3,4,5,6,7,8],
[1,2,3,4,5,6,7,8],
[1,2,3,4,5,6,7,8],
[1,2,3,4,5,6,7,8],
[1,2,3,4,5,6,7,8],
[1,2,3,4,5,6,7,8],
[1,2,3,4,5,6,7,8]]

print(hetmanow_8(tab,tab1))

