from itertools import product, count


def solve(lines):
    moves = list(product([1, -1, 0], repeat=2))
    moves.remove((0, 0))
    fcount = 0

    def flash(i, j):
        nonlocal fcount
        fcount += 1
        for move in moves:
            x, y = i + move[0], j + move[1]
            if not all([0 <= x < len(lines[0]), 0 <= y < len(lines)]):
                continue
            lines[x][y] += 1
            if lines[x][y] == 10:
                flash(x, y)

    for step in count(1):
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                line[j] = c + 1
                if line[j] == 10:
                    flash(i, j)
        ans = 0
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c >= 10:
                    ans += 1
                    line[j] = 0
        if step == 100:
            print(fcount)
        if ans == len(lines) * len(lines[0]):
            print(step)
            return


if __name__ == "__main__":
    with open("./input/day11.txt", "r") as f:
        lines = [[int(k) for k in a.strip()] for a in f.readlines()]
    solve(lines)
