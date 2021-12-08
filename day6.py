from functools import cache


@cache
def score(t, day):
    if t >= day:
        return 1
    else:
        return score(6, day - t - 1) + score(8, day - t - 1)


def part1(nums):
    s = map(lambda x: score(x, 80), nums)
    print(sum(s))


def part2(nums):
    s = map(lambda x: score(x, 256), nums)
    print(sum(s))


if __name__ == "__main__":
    with open("./input/day6.txt", "r") as f:
        lines = [int(a.strip()) for a in f.readline().split(",")]
    part1(lines)
    part2(lines)
