lut = {2: 1, 4: 4, 3: 7, 7: 8}


def part1(lines):
    c = sum(len([1 for k in l[1].strip().split(" ") if len(k) in lut]) for l in lines)
    print(c)


def part2(lines):
    count = 0
    for line in lines:
        slots = ["" for i in range(10)]
        len6, len5 = [], []
        for number in line[0].strip().split(" "):
            number = "".join(sorted(number))
            if len(number) in lut:
                # 1,4,7,8 found here
                slots[lut[len(number)]] = number
            elif len(number) == 6:
                len6.append(number)
            elif len(number) == 5:
                len5.append(number)
            else:
                assert False
        # finding remaining numbers
        slots[6] = [i for i in len6 if any(k not in i for k in slots[1])][0]
        slots[9] = [i for i in len6 if all(k in i for k in slots[4])][0]
        slots[0] = [i for i in len6 if i not in slots][0]
        slots[3] = [i for i in len5 if all(k in i for k in slots[1])][0]
        slots[5] = [i for i in len5 if all(k in slots[6] for k in i)][0]
        slots[2] = [i for i in len5 if i not in slots][0]

        s = 0
        for n in line[1].strip().split(" "):
            n = "".join(sorted(n))
            s = s * 10 + slots.index(n)
        count += s
    print(count)


if __name__ == "__main__":
    with open("./input/day8.txt", "r") as f:
        lines = [a.strip().split("|") for a in f.readlines()]
    part1(lines)
    part2(lines)
