import math

def isPrime(num):
    i = 2
    if num > 1:
        while num % i != 0 and i <= num:
            i = i + 1
        if(i == num):
            return True
        return False
    return False


def largestPrimeFactor(largeNum):
    for i in range(largeNum//2, 2, -2):
        if(largeNum % i == 0):
            print(i)
            if(isPrime(i)):
                print("prime")
                return i
    return largeNum


def main():
    print(largestPrimeFactor(600851475143))


main()
