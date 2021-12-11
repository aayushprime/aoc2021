def part1(lines):
    lut = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    complement = {
        "}": "{",
        ">": "<",
        ")": "(",
        "]": "[",
    }

    score = 0
    for line in lines:
        s = []
        for c in line:
            if c in "([{<":
                s.append(c)
                continue
            elif c in lut and s[-1] == complement[c]:
                s.pop()
            else:
                score += lut[c]
                break
    print(score)


def part2(lines):
    lut = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    complement = {
        "{": "}",
        "<": ">",
        "(": ")",
        "[": "]",
    }
    scores = []
    for line in lines:
        score = 0
        s = []
        for c in line:
            if c in "([{<":
                s.append(c)
            elif c == complement[s[-1]]:
                s.pop()
            else:
                # push closing bracket if corrupt
                s.append(c)
                break
        # check if top of stack is a closing bracket
        if s[-1] in lut:
            continue
        for i in s[::-1]:
            score = score * 5 + lut[complement[i]]
        scores.append(score)

    print(sorted(scores)[len(scores) // 2])


if __name__ == "__main__":
    with open("./input/day10.txt", "r") as f:
        lines = [a.strip() for a in f.readlines()]
    part1(lines)
    part2(lines)
