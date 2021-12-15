import heapq


def solve(start, size):
    # parse the weights into an array
    risks = [[int(k[i]) for i in range(len(k))] for k in lines]
    # fill the weights of each node with an unusually large value
    # it is of larger size!
    weights = [
        [1e300 for _ in range(len(risks[0]) * size)] for _ in range(len(risks) * size)
    ]

    # abstraction to make risk appear as a array of larger size
    def get_risk(x, y):
        res = (
            risks[x % len(risks[0])][y % len(risks)]
            + x // len(risks[0])
            + y // len(risks)
        )
        return 1 + (res - 1) % 9

    # give neighbours of a cell
    def neighbours(x, y):
        possible = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [
            (a, b)
            for (a, b) in possible
            if 0 <= a < len(risks[0]) * size and 0 <= b < len(risks) * size
        ]

    # priority queue needed for dijkstra
    pq = [(0, (0, 0))]
    # while queue is not empty
    while len(pq) != 0:
        # pop from pq
        dist, (x, y) = heapq.heappop(pq)
        # if distance in less than the previous distance
        if dist <= weights[x][y]:
            # update the neighbours distance and push them if distance reduced
            for n in neighbours(x, y):
                d = dist + get_risk(n[0], n[1])
                if d < weights[n[0]][n[1]]:
                    weights[n[0]][n[1]] = d
                    heapq.heappush(pq, (d, n))
    # last cell is our goal
    print(weights[-1][-1])


if __name__ == "__main__":
    with open("./input/day15.txt", "r") as f:
        lines = [a.strip() for a in f.read().split("\n") if a != ""]
    solve(lines, 1)
    solve(lines, 5)
