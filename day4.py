def part1(baords, chosen):
    seen = set()
    for number in chosen:
        seen.add(number)
        if len(seen) < 5:
            continue
        for board in boards:
            for row in board:
                if number not in row:
                    continue
                i = row.index(number)
                if all([k in seen for k in row]) or all([k[i] in seen for k in board]):
                    s = 0
                    for row in board:
                        s += sum([k for k in row if k not in seen])
                    print(s * number)
                    return


def part2(boards, chosen):
    seen = set()
    win = [False for _ in range(len(boards))]
    for number in chosen:
        seen.add(number)
        if len(seen) < 5:
            continue
        for bi, board in enumerate(boards):
            if win[bi]:
                continue
            for row in board:
                if number not in row:
                    continue
                i = row.index(number)
                # are all columns/rows marked?
                if all([k in seen for k in row]) or all([k[i] in seen for k in board]):
                    # is this the last board that won?
                    if win.count(False) == 1:
                        wboard = win.index(False)
                        s = 0
                        for row in boards[wboard]:
                            s += sum([k for k in row if k not in seen])
                        print(s * number)
                        return
                    # mark this board has won
                    win[bi] = True
                    break


if __name__ == "__main__":
    with open("./input/day4.txt", "r") as f:
        chosen = [int(a) for a in f.readline().strip().split(",")]
        boards = []
        board = []
        for line in f.readlines():
            if line in ["\n", "", "\r"]:
                continue

            board.append([int(a) for a in line.strip().split(" ") if a != ""])

            if len(board) == 5:
                boards.append(board)
                board = []
    part1(boards, chosen)
    part2(boards, chosen)
