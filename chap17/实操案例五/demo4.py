import math

for i in range(100, 1000):
    if math.pow((i % 10), 3) + math.pow((i // 10 % 10), 3) + math.pow((i // 100), 3) == i:
        print(i)
