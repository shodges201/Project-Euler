def evenFibonacciNums():
    lower = 0
    higher = 1
    sum = 0
    evenFibs = []
    while(sum < 4000000):
        sum = lower + higher
        lower = higher
        higher = sum
        if(sum % 2 == 0):
            evenFibs.append(sum)
    return evenFibs

def sumOfEvenFibs(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
    return sum

def main():
    print(sumOfEvenFibs(evenFibonacciNums()))

main()
        