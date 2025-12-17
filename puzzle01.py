def banana_count_p1(banana: str) -> int:
    count = 0
    for i in range(len(banana)-1):
        if banana[i:i+2] in ["ba", "na", "ne"]:
            count += 1
    return count

total_p1: int = 0
total_p2: int = 0
total_p3: int = 0
with open("input-01.txt") as f:

    for line in f:
        banana_count: int = banana_count_p1(line)
        total_p1 += banana_count
        if banana_count % 2 == 0:
            total_p2 += banana_count
        if "ne" not in line:
            total_p3 += banana_count

print(total_p1)
print(total_p2)
print(total_p3)