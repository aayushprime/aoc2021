def part1(lines):
    seen = dict()
    for line in lines:
        start, end = list(map(lambda k: k.split(","), line))
        if start[0] == end[0] or start[1] == end[1]:
            i = 1 if start[0] == end[0] else 0
            coords = [int(start[i]), int(end[i])]
            coords = [min(coords), max(coords) + 1]
            for j in range(*coords):
                key = (
                    start[0].zfill(3) + ":" + str(j).zfill(3)
                    if i == 1
                    else str(j).zfill(3) + ":" + start[1].zfill(3)
                )
                if key not in seen:
                    seen[key] = 1
                else:
                    seen[key] += 1
    c = len([a for a in seen.values() if a != 1])
    print(c)


def diagonal(start, end):
    return (end[1] - start[1]) / (end[0] - start[0]) in [-1, 1]


def part2(lines):
    seen = dict()
    for line in lines:
        start, end = list(map(lambda k: k.split(","), line))
        start = list(map(lambda x: int(x), start))
        end = list(map(lambda x: int(x), end))
        if start[0] == end[0] or start[1] == end[1]:
            i = 1 if start[0] == end[0] else 0
            coords = [start[i], end[i]]
            coords = [min(coords), max(coords) + 1]
            for j in range(*coords):
                key = (
                    str(start[0]).zfill(3) + ":" + str(j).zfill(3)
                    if i == 1
                    else str(j).zfill(3) + ":" + str(start[1]).zfill(3)
                )
                if key not in seen:
                    seen[key] = 1
                else:
                    seen[key] += 1
        elif diagonal(start, end):
            dx = start[0] - end[0]
            dy = start[1] - end[1]
            longer = max(abs(dx), abs(dy))
            sx = 1 if dx >= 0 else -1
            sy = 1 if dy >= 0 else -1
            for i in range(longer + 1):
                key = str(end[0]).zfill(3) + ":" + str(end[1]).zfill(3)
                if key not in seen:
                    seen[key] = 1
                else:
                    seen[key] += 1
                end[0] += sx
                end[1] += sy
    c = len([a for a in seen.values() if a != 1])
    print(c)


if __name__ == "__main__":
    with open("./input/day5.txt", "r") as f:
        lines = [(k.strip().split(" -> ")) for k in f.readlines()]
    part1(lines)
    part2(lines)
