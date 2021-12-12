import copy


def part1(lines):
    paths = {}
    for line in lines:
        start, end = line.split("-")
        if start in paths:
            paths[start].append(end)
        else:
            paths[start] = [end]
        if end in paths:
            paths[end].append(start)
        else:
            paths[end] = [start]

    count = 0

    def find(paths, beginning, visited):
        nonlocal count
        for path in paths[beginning]:
            dup = copy.copy(visited)
            dup.append(path)
            if path == "end":
                count += 1
                (dup)
            elif path.islower() and path not in visited or path.isupper():
                find(paths, path, dup)

    find(paths, "start", ["start"])
    print(count)


def part2(lines):
    paths = {}
    for line in lines:
        start, end = line.split("-")
        if end != "start":
            if start in paths:
                paths[start].append(end)
            else:
                paths[start] = [end]
        if start != "start":
            if end in paths:
                paths[end].append(start)
            else:
                paths[end] = [start]

    count = 0

    def find(paths, beginning, visited, small_cave):
        nonlocal count
        for path in paths[beginning]:
            if path == "end":
                count += 1
                continue
            if path.isupper():
                find(paths, path, copy.copy(visited) + [path], small_cave)
            elif path.islower():
                if path not in visited:
                    find(paths, path, copy.copy(visited) + [path], small_cave)
                elif small_cave:
                    find(paths, path, copy.copy(visited) + [path], False)

    find(paths, "start", ["start"], True)
    print(count)


if __name__ == "__main__":
    with open("./input/day12.txt", "r") as f:
        lines = [a.strip() for a in f.readlines()]
    part1(lines)
    part2(lines)
