import time

def isPrime(num):
    i = 2
    if num > 2:
        while num % i != 0 and i <= num//2:
            i = i + 1
        if(i == num):
            return True
        return False
    return False

def isPalindrome(num):
    numStr = str(num)
    numChecks = len(numStr) // 2
    #odd length
    if(not len(numStr) % 2 == 0):
        numChecks += 1
    for i in range(0, numChecks):
        if(numStr[i] != numStr[len(numStr)-i-1]):
            return False
    return True

def productOfLengthsThree(num):
    for i in range(100, num//100):
        if(num % i == 0 and len(str(int(i))) == 3 and len(str(num // i)) == 3):
            # print(num)
            # print(i)
            # print(num // i)
            # print("------------")
            return True
    return False

def findLargePalindrome(num):
    for i in range(num, 0, -1):
        if(isPalindrome(i)):
            #print(i)
            if(not isPrime(i)):
                if(productOfLengthsThree(i)):
                    return i
    return -1

def main():
    #totalTime = 0
    #not checking primes:
    #average over 100 trials -> 0.14785187005996703
    #checking for primes:
    #average over 100 trials -> 0.14781426668167114
    # for i in range(0, 100):
    #     start = time.time()
    #     print(findLargePalindrome(998001))
    #     end = time.time()
    #     totalTime += end-start
    # print(totalTime / 100)
    print(findLargePalindrome(998001))

main()
