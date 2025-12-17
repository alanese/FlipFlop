from functools import cache

@cache
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def binom(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n-k))

def product(xs: list[int]) -> int:
    total: int = 1
    for x in xs:
        total *= x
    return total

def multinom(n: int, ks: list[int]) -> int:
    return factorial(n) // product([factorial(k) for k in ks])


shortest_path_p1_sum: int = 0
shortest_path_p2_sum: int = 0
shortest_path_p3_sum: int = 0
with open("input-07.txt") as f:
    for line in f:
        coords: list[int] = [int(x) for x in line.split()]
        shortest_path_p1:int = binom(coords[0] + coords[1] - 2, coords[0] - 1)
        shortest_path_p1_sum += shortest_path_p1
        shortest_path_p2: int = multinom(coords[0] + coords[1] + coords[0] - 3, [coords[0]-1, coords[1]-1, coords[0]-1])
        shortest_path_p2_sum += shortest_path_p2
        shortest_path_p3: int = multinom(coords[0] * (coords[1] - 1), [coords[1] - 1] * coords[0])
        shortest_path_p3_sum += shortest_path_p3
print(shortest_path_p1_sum)
print(shortest_path_p2_sum)
print(shortest_path_p3_sum)
