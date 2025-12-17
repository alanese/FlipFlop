from collections import defaultdict

UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input-05.txt") as f:
    sequence: str = f.read()

pairs: dict[str, list[int]] = defaultdict(list)
visited: dict[str, None] = {}
endpoints: dict[int, int] = {}

for i, char in enumerate(sequence):
    visited[char] = None
    pairs[char].append(i)
    if len(pairs[char]) == 2:
        endpoints[pairs[char][0]] = pairs[char][1]
        endpoints[pairs[char][1]] = pairs[char][0]

tunnel_distance: int = 0
tunnel_distance_p3: int = 0
pos: int = 0
while pos < len(sequence):
    if sequence[pos] in visited:
        del visited[sequence[pos]]
    pos = endpoints[pos]
    cur_tunnel_distance: int = pairs[sequence[pos]][1] - pairs[sequence[pos]][0]
    tunnel_distance += cur_tunnel_distance
    if sequence[pos] in UPPERCASE:
        tunnel_distance_p3 -= cur_tunnel_distance
    else:
        tunnel_distance_p3 += cur_tunnel_distance
    pos += 1

print(tunnel_distance)
print("".join(visited.keys()))
print(tunnel_distance_p3)