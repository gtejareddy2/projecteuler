import lib

n = 1
i = 0

while(n <= 10001):
    i+=1
    if lib.is_prime(i):
        n+=1


print i
