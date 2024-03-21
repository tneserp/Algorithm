from itertools import permutations
import sys

input = sys.stdin.readline

N = int(input().strip())

number = list(map(int, input().split()))

operationNumber = list(map(int, input().split()))

# +, -, x, /

operations = list()

for _ in range(operationNumber[0]):
    operations.append("+")

for _ in range(operationNumber[1]):
    operations.append("-")

for _ in range(operationNumber[2]):
    operations.append("x")

for _ in range(operationNumber[3]):
    operations.append("/")

maxValue = float("-inf")
minValue = float("inf")

for i in set(permutations(operations, len(operations))):
    result = number[0]
    for j in range(len(i)):
        if i[j] == '+':
            result = int(result + number[j + 1])
        elif i[j] == '-':
            result = int(result - number[j + 1])
        elif i[j] == 'x':
            result = int(result * number[j + 1])
        else:
            result = int(result / number[j + 1])

    maxValue = max(maxValue, result)
    minValue = min(minValue, result)

print(maxValue)
print(minValue)
