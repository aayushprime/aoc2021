from functools import reduce
import operator


def part1(lines):
    def inbounds(i, j):
        return 0 <= i < len(lines) and 0 <= j < len(lines[0])

    def neighbours(i, j):
        return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

    count = 0
    for i, line in enumerate(lines):
        for j, n in enumerate(line):
            if all(n < lines[k[0]][k[1]] for k in neighbours(i, j) if inbounds(*k)):
                count += int(n) + 1
    print(count)


def part2(lines):
    def inbounds(i, j):
        return 0 <= i < len(lines) and 0 <= j < len(lines[0])

    def neighbours(i, j):
        return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

    def key(i, j):
        return str(i).zfill(3) + str(j).zfill(3)

    seen = set()
    sizes = []
    for i, line in enumerate(lines):
        for j, n in enumerate(line):
            if n == "9" or key(i, j) in seen:
                continue
            size = 0
            q = [(i, j)]
            while len(q) != 0:
                coord = q.pop(0)
                if key(*coord) in seen:
                    continue
                size += 1
                seen.add(key(*coord))
                q.extend(
                    [
                        k
                        for k in neighbours(*coord)
                        if key(*k) not in seen
                        and inbounds(*k)
                        and lines[k[0]][k[1]] != "9"
                    ]
                )
            sizes.append(size)
    print(reduce(operator.mul, sorted(sizes)[-3:]))


if __name__ == "__main__":
    with open("./input/day9.txt", "r") as f:
        lines = [a.strip() for a in f.readlines()]
    part1(lines)
    part2(lines)
