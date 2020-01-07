import time

def evenlyDivisible(num):
    for i in range(2, 21):
        if(not num % i == 0):
            return False
    return True

def driver():
    maxNum = 1
    for i in range(2, 21):
        maxNum *= i
    for j in range(20*19, maxNum, 20):
        if(evenlyDivisible(j)):
            return j
    return -1

def main():
    start = time.time()
    print(driver())
    end = time.time()
    print(end-start)
main()