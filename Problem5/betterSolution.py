import time
import math

def isPrime(num):
    i = 2
    if num > 2:
        while num % i != 0 and i <= num:
            i = i + 1
        if(i == num):
            return True
        return False
    return True

def primeFactorization(num):
    product = 1
    for i in range(2, num+1):
        if(isPrime(i)):
            print(i)
            power = int(math.log(20, i))
            product *= int(math.pow(i, power))
    return product



def main():
    #print(isPrime(3))
    start = time.time()
    print(primeFactorization(20))
    end = time.time()
    print(end-start)
main()