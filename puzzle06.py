P1_SHOT_TIME: int = 100
P2_SHOT_INTERVAL: int = 3600
P3_SHOT_INTERVAL: int = 31556926

GRID_SIZE: int = 1000
FRAME_SIZE: int = 500

FRAME_LOWER: int = GRID_SIZE//2 - FRAME_SIZE//2
FRAME_UPPER: int = GRID_SIZE//2 + FRAME_SIZE//2 - 1


def in_frame(birds: list[tuple[int, int]], time: int) -> int:
    in_frame_count: int = 0
    for bird_x, bird_y in birds:
        if FRAME_LOWER <= (bird_x*time)%GRID_SIZE <= FRAME_UPPER:
            if FRAME_LOWER <= (bird_y*time)%GRID_SIZE <= FRAME_UPPER:
                in_frame_count += 1
    return in_frame_count



birds: list[tuple[int, int]] = []
with open("input-06.txt") as f:
    for line in f:
        line_split: list[str] = line.split(",")
        birds.append( (int(line_split[0]), int(line_split[1])) )

print(in_frame(birds, P1_SHOT_TIME))

p2_total: int = 0
p3_total: int = 0
for i in range(1, 1001):
    p2_total += in_frame(birds, P2_SHOT_INTERVAL * i)
    p3_total += in_frame(birds, P3_SHOT_INTERVAL * i)
print(p2_total)
print(p3_total)