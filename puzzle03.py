from collections import Counter

def color_value(red: int, green: int, blue: int) -> int:
    if red == green or red == blue or green == blue:
        #special
        return 10
    elif red > green and red > blue:
        #red
        return 5
    elif green > red and green > blue:
        #green
        return 2
    else:
        #blue
        return 4
color_count:Counter = Counter()
most_common_color: tuple[int, ...] = tuple()
most_common_color_count: int = 0
green_count: int = 0
value_total: int = 0

with open("input-03.txt") as f:
    for line in f:
        color: tuple[int, ...] = tuple([int(x) for x in line.strip().split(",")])
        color_count[color] += 1
        if color_count[color] > most_common_color_count:
            most_common_color = color
            most_common_color_count = color_count[color]
        if color[1] > color[0] and color[1] > color[2] and color[0] != color[2]:
            green_count += 1
        value_total += color_value(color[0], color[1], color[2])

print(most_common_color)
print(green_count)
print(value_total)