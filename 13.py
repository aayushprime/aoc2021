def key(x, y):
    return str(x).zfill(5) + str(y).zfill(5)


def key_to_coords(key):
    return (int(key[:5]), int(key[5:]))


def part1(lines, fold):
    about, value = fold.split("\n")[0].split("along")[1].strip().split("=")
    value = int(value)
    coords = set()

    for line in lines.split("\n"):
        x, y = line.split(",")
        x, y = int(x), int(y)
        if about == "x" and x > value:
            n = 2 * value - x
            coords.add(key(n, y))
        elif about == "y" and y > value:
            n = 2 * value - y
            coords.add(key(x, n))
        else:
            coords.add(key(x, y))

    print(len(coords))


def part2(lines, fold):
    folds = []
    for f in fold.split("\n"):
        about, value = f.split("along")[1].strip().split("=")
        folds.append((about, int(value)))

    coords = set()

    for point in lines:
        x, y = point.split(",")
        x, y = int(x), int(y)
        coords.add(key(x, y))

    newset = set()
    for fold in folds:
        for point in coords:
            x, y = key_to_coords(point)
            about, value = fold
            if about == "x" and x > value:
                n = 2 * value - x
                newset.add(key(n, y))
            elif about == "y" and y > value:
                n = 2 * value - y
                newset.add(key(x, n))
            else:
                newset.add(key(x, y))

        coords = newset
        newset = set()

    for j in range(7):
        for i in range(48):
            print("#" if key(i, j) in coords else ".", end="")
        print("")


if __name__ == "__main__":
    with open("./input/day13.txt", "r") as f:
        lines = [a.strip() for a in f.read().split("\n\n")]
    part1(lines[0], lines[1])
    part2(lines[0].split("\n"), lines[1])
