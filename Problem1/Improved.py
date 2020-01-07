def sumUpTo(divisor, maxVal):
    print(divisor*(maxVal//divisor)*((maxVal//divisor)+1)//2)
    return divisor*(maxVal//divisor)*((maxVal//divisor)+1)//2

def sumOf3And5():
    return sumUpTo(3, 999) + sumUpTo(5, 999) - sumUpTo(15, 999)

def main():
    sum = sumOf3And5()
    print(sum)

main()