def taxicab_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def diag_taxicab_distance(a: tuple[int, int], b: tuple[int, int]):
    return max(abs(a[0] - b[0]), abs(a[1]-b[1]))

prev_x: int = 0
prev_y: int = 0
curr_x: int = 0
curr_y: int = 0

total_distance_p1: int = 0
total_distance_p2: int = 0
with open("input-04.txt") as f:
    coords: list[list[int]] = [ [ int(x) for x in line.strip().split(",")] for line in f]

for coord in coords:
    prev_x, prev_y = curr_x, curr_y
    curr_x = coord[0]
    curr_y = coord[1]
    total_distance_p1 += taxicab_distance( (prev_x, prev_y), (curr_x, curr_y))
    total_distance_p2 += diag_taxicab_distance( (prev_x, prev_y), (curr_x, curr_y))

coords.sort(key=lambda coord: abs(coord[0]) + abs(coord[1]))
curr_x, curr_y = 0, 0
total_distance_p3: int = 0
for coord in coords:
    prev_x, prev_y = curr_x, curr_y
    curr_x = coord[0]
    curr_y = coord[1]
    total_distance_p3 += diag_taxicab_distance( (prev_x, prev_y), (curr_x, curr_y))


print(total_distance_p1)
print(total_distance_p2)
print(total_distance_p3)