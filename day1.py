def part1(lines):
    prev = lines[0]
    more = 0
    for i in range(len(lines) - 1):
        if lines[i+1] > prev:
            more += 1
        prev = lines[i+1]
    print(more)

def part2(lines):
    window = []
    for i in range(len(lines) - 2):
        window.append(sum(lines[i:i+3]))
    print(part1(window))

if __name__ =='__main__':
    with open('./input/day1.txt', 'r') as f:
        lines = [int(a.strip()) for a in f.readlines()]
    part1(lines)
    part2(lines)
