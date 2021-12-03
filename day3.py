def part1(lines):
    l = [[0,0] for _ in lines[0]]
    for line in lines:
        for j,c in enumerate(line):
            l[j][int(c)] += 1
    gamma_bin = ['0' if k[0] > k[1] else '1' for k in l]
    gamma = int("".join(gamma_bin), 2)
    epsilon = int("".join(['0' if k == '1' else '1' for k in gamma_bin]), 2)
    print(gamma * epsilon)

def part2(lines):
    ox_rate = lines
    for i in range(len(lines[0])):
        if len(ox_rate) == 1:
            break
        ones = 0
        for line in ox_rate:
            if line[i] == '1':
                ones += 1
        bit = '1' if ones >= len(ox_rate) - ones else '0'
        ox_rate = list(filter(lambda x: x[i] == bit, ox_rate))

    co_rate = lines
    for i in range(len(lines[0])):
        if len(co_rate) == 1:
            break
        ones = 0
        for line in co_rate:
            if line[i] == '1':
                ones += 1
        bit = '1' if ones < len(co_rate) - ones else '0'
        co_rate = list(filter(lambda x: x[i] == bit, co_rate))

    co = int(co_rate[0], 2)
    ox = int(ox_rate[0], 2)
    print(co*ox)

if __name__ =='__main__':
    with open('./input/day3.txt', 'r') as f:
        lines = [a.strip() for a in f.readlines()]
    part1(lines)
    part2(lines)
