import sys

n = int(input().strip())
if 1 <= n <= 20:
    print(n)
    for i in range(n):
        print(i ** 2)
else:
    print("error")
