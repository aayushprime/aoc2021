from collections import Counter


def part1(start, steps):
    # naive solution
    rules = {}
    for step in steps.split("\n"):
        dw, w = step.split(" -> ")
        rules[dw] = w

    for i in range(10):
        s = ""
        for j in range(len(start) - 1):
            s += start[j] + rules[start[j : j + 2]]
        s += start[-1]
        start = s

    c = Counter(s)
    print(max(c.values()) - min(c.values()))


# thanks random reddit user
def part2(start, steps):
    # the rules of polymer growth
    rules = {}
    for step in steps.split("\n"):
        dw, w = step.split(" -> ")
        rules[dw] = w

    # count the characters (final answer will be here)
    chars = Counter(start)
    # count number of 2 character pairs NNCB => NN, NC, CB
    template = Counter(a + b for a, b in zip(start, start[1:]))

    for _ in range(40):
        # create a new dictionary for new 2 character pairs to live
        new_template = Counter()
        # ab = NN, value = (how many NN there are)
        for (a, b), value in template.items():
            # find the new character to insert
            insert = rules[a + b]
            # each entry is increased by value
            # because there are 'value' number of similar elements
            # insert new 2 letter pairs if NN => H then NH and HN
            new_template[a + insert] += value
            new_template[insert + b] += value
            # increase the number of newly inserted character
            chars[insert] += value
        template = new_template
    print(max(chars.values()) - min(chars.values()))


if __name__ == "__main__":
    with open("./input/day14.txt", "r") as f:
        lines = [a.strip() for a in f.read().split("\n\n")]
    part1(lines[0], lines[1])
    part2(lines[0], lines[1])
