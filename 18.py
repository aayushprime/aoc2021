import ast
from itertools import permutations


def add(n1, n2):
    return ["["] + n1 + [","] + n2 + ["]"]


def explode(s, i):
    pair = int(s[i + 1]), int(s[i + 3])
    c = i
    while i != 0:
        if s[i] not in ["[", "]", ",", ", "]:
            s[i] = str(int(s[i]) + int(pair[0]))
            break
        i -= 1

    j = c + 5
    while j < len(s):
        if s[j] not in ["[", "]", ",", ", "]:
            s[j] = str(int(s[j]) + int(pair[1]))
            break
        j += 1
    s[c : c + 5] = "0"
    return s


def split(s, i):
    num = int(s[i])
    n1 = num // 2
    n2 = num - n1
    s[i : i + 1] = ["[", str(n1), ",", str(n2), "]"]


def balance(s):
    depth = 0
    for i, c in enumerate(s):
        if c in [",", ", ", " ", " ", ""]:
            continue
        if c == "[":
            depth += 1
            if depth > 4:
                s = explode(s, i)
                balance(s)
                return
        elif c == "]":
            depth += -1

    for i, c in enumerate(s):
        if c in [",", ", ", " ", " ", "", "[", "]"]:
            continue
        elif int(c) >= 10:
            split(s, i)
            balance(s)
            return


def magnitude(n1):
    if type(n1) == int:
        return n1
    else:
        return 3 * magnitude(n1[0]) + 2 * magnitude(n1[1])


def solve(lines):

    # part 1
    s = lines[0]
    for i in range(1, len(lines)):
        s = add(s, lines[i])
        balance(s)

    string = "".join(s)
    # this function converts a string to python object
    s = ast.literal_eval(string)
    print(magnitude(s))

    # part 2
    ma = 0
    all_possible = permutations(lines, 2)
    for possible in all_possible:
        su = add(possible[0], possible[1])
        balance(su)
        mag = magnitude(ast.literal_eval("".join(su)))
        if mag > ma:
            ma = mag

    print(ma)


if __name__ == "__main__":
    with open("./input/day18.txt", "r") as f:
        lines = [list(a.strip()) for a in f.readlines()]
        solve(lines)
