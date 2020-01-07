def sumOf3And5():
    x = []
    sum = 0
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            x.append(i)
    print(x[-1])
    for j in range(0, len(x)):
        sum += x[j]
    return sum

def main():
    sum = sumOf3And5()
    print(sum)

main()
