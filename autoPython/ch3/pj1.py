import sys

try:
    inputNum = int(input())
except ValueError:
    print('Error: Invalid input, integer is expected here')
    sys.exit()

def collatz(num):
    if num % 2 == 0:
        result = num // 2
        print(result)
        return result
    else:
        result = 3 * num + 1
        print(result)
        return result

expectNum = collatz(inputNum)
while expectNum != 1:
    expectNum = collatz(expectNum)

