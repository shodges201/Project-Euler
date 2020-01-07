import time

def sumOfSquares(maxNum):
    sum = 0
    for i in range(1, maxNum+1):
        sum += i * i
    return sum

def sumUpToNumber(num):
    if(num % 2 == 0):
        sum = (num + 1) * (num // 2)
    else:
        sum = ((num + 1) * (num // 2)) + ((num+1)//2)
    return sum


def squareOfSums(maxNum):
    sum = sumUpToNumber(maxNum)
    return sum * sum

def difference(maxNum):
    return squareOfSums(maxNum) - sumOfSquares(maxNum)

def main():
    start = time.time()
    print(difference(100))
    end = time.time()
    print("Calculating this took: " + str(end-start) + " seconds")

main()