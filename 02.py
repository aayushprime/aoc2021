def part1(lines):
    hpos = 0
    height = 0
    for line in lines:
        direction, amount = line.split(" ")
        amount = int(amount)

        if direction == "forward":
            hpos += amount
        elif direction == "up":
            height -= amount
        elif direction == "down":
            height += amount
        else:
            print("wrong", direction.encode(), amount.encode())
            print("Something is wrong")
    print(height * hpos)


def part2(lines):
    hpos = 0
    aim = 0
    height = 0
    for line in lines:
        direction, amount = line.split(" ")
        amount = int(amount)
        if direction == "forward":
            hpos += amount
            height += amount * aim
        elif direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount
        else:
            print("wrong", direction.encode(), amount.encode())
            print("Something is wrong")
    print(height * hpos)


if __name__ == "__main__":
    with open("./input/day2.txt", "r") as f:
        lines = f.readlines()
    part1(lines)
    part2(lines)
