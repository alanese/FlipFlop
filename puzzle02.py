from functools import cache

@cache
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

height_p1: int = 0
max_height_p1: int = 0
height_p2: int = 0
max_height_p2: int = 0
momentum: int= 0
height_p3 = 0
max_height_p3 = 0
with open("input-02.txt") as f:
    for char in f.read():
        match char:
            case "^":
                height_p1 += 1
                if height_p1 > max_height_p1:
                    max_height_p1 = height_p1
                if momentum >= 0:
                    momentum += 1
                else:
                    height_p3 -= fib(abs(momentum))
                    momentum = 1
                height_p2 += momentum
                if height_p2 > max_height_p2:
                    max_height_p2 = height_p2

            case "v":
                height_p1 -= 1
                if momentum <= 0:
                    momentum -= 1
                else:
                    height_p3 += fib(momentum)
                    if height_p3 > max_height_p3:
                        max_height_p3 = height_p3
                    momentum = -1
                height_p2 += momentum

if momentum > 0:
    height_p3 += fib(momentum)
    if height_p3 > max_height_p3:
        max_height_p3 = height_p3
else:
    height_p3 -= fib(abs(momentum))

print(max_height_p1)
print(max_height_p2)
print(max_height_p3)