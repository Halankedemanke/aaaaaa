
def prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i < (n*0.5) + 1:
        if n % i == 0:
            return False
        i += 1
    return True

n = 2222
def divide(n, i = 10, podizal = 1):
    if prime(n) and prime(podizal):
        print(podizal)
        return True
    if n//i == 0:
        return False

    if prime(n%i):
        if divide(n//i,i*10,podizal+1):
            return True
    return divide(n, i*10,podizal)

        
divide(n)