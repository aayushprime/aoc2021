from statistics import median

def part1(nums):
    m = median(nums)
    s = sum(abs(i - m) for i in nums)
    print(s)

def part2(nums):
    c = min(sum(n*(n+1)/2 for n in (abs(k-i) for k in nums)) for i in range(min(nums),max(nums)+1))
    print(c)

if __name__ =='__main__':
    with open('./input/day7.txt', 'r') as f:
        lines = [int(a.strip()) for a in f.readline().split(",")]
    part1(lines)
    part2(lines)
