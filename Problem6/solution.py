
def sumOfSquares(maxNum):
    sum = 0
    for i in range(1, maxNum+1):
        sum += i * i
    return sum

def sumUpToNumber(num):
    if(num % 2 == 0):
        #print("even")
        sum = (num + 1) * (num // 2)
        #print(sum)
    else:
        # print("odd")
        # print(((num + 1) * (num // 2)))
        # print(((num+1)//2))
        sum = ((num + 1) * (num // 2)) + ((num+1)//2)
        # print(sum)
    return sum


def squareOfSums(maxNum):
    sum = sumUpToNumber(maxNum)
    return sum * sum

def difference(maxNum):
    return squareOfSums(maxNum) - sumOfSquares(maxNum)

def main():
    #sumUpToNumber(6)
    print(difference(100))

main()