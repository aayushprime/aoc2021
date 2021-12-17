# credits: https://github.com/SiddhantAttavar/Competitive-Programming
from functools import reduce


def part1(packet):
    def parse(bits):
        c = 0
        res = 0
        while c < len(bits) and "1" in bits[c:]:
            version = int(bits[c : c + 3], 2)
            res += version
            c += 3
            type_id = int(bits[c : c + 3], 2)
            c += 3
            if type_id == 4:
                # raw packet
                num = ""
                while bits[c] == "1":
                    num += bits[c + 1 : c + 5]
                    c += 5
                num += bits[c + 1 : c + 5]
                c += 5
                num = int(num, 2)
            else:
                length_type = int(bits[c], 2)
                c += 1
                if length_type == 0:
                    num = int(bits[c : c + 15], 2)
                    c += 15
                else:
                    num = int(bits[c : c + 11], 2)
                    c += 11
        return res

    # packet = "C0015000016115A2E0802F182340"
    in_bits = int(packet, 16)
    pad = len(packet) * 4
    in_bits = f"{in_bits:0{int(pad)}b}"
    # in_bits = "11010001010"
    print(parse(in_bits))


def part2(packet):
    # pad the bits to have 4 bit boundaries
    in_bits = int(packet, 16)
    pad = len(packet) * 4
    bits = f"{in_bits:0{int(pad)}b}"

    # functions map
    functions = {
        0: sum,
        1: lambda a: reduce(lambda x, y: x * y, a),
        2: min,
        3: max,
        5: lambda a: int(a[0] > a[1]),
        6: lambda a: int(a[0] < a[1]),
        7: lambda a: int(a[0] == a[1]),
    }

    # function to evaluate a packet (node in ast)
    def evaluate(u):
        # if packet is a raw packet
        if packets[u][1] == 4:
            return packets[u][2]
        # if packet is not raw packet
        res = []
        for v in graph[u]:
            # evaluate the sub nodes
            res.append(evaluate(v))
        # select the operation and apply it to res
        return functions[packets[u][1]](res)

    # parse packets into this array
    packets = []
    c = 0
    while c < len(bits) and "1" in bits[c:]:
        version = int(bits[c : c + 3], 2)
        c += 3
        type_id = int(bits[c : c + 3], 2)
        c += 3

        if type_id == 4:
            # raw packet
            num = ""
            while bits[c] == "1":
                num += bits[c + 1 : c + 5]
                c += 5
            num += bits[c + 1 : c + 5]
            c += 5
            num = int(num, 2)
            packets.append([version, type_id, num, c])
        else:
            # operator packet
            length_type = int(bits[c], 2)
            c += 1
            if length_type == 0:
                num = int(bits[c : c + 15], 2)
                c += 15
            else:
                num = int(bits[c : c + 11], 2)
                c += 11
            packets.append([version, type_id, length_type, num, c])

    stack = []
    graph = [[] for _ in range(len(packets))]

    # +23

    # building the graph (ast)
    for i, packet in enumerate(packets):
        # if something is in stack
        if len(stack) > 0:
            p = stack[-1]
            # put the new node in the graph corresponding to stack element
            graph[p].append(i)
            packets[p][3] -= 1
            if packets[p][3] == 0:
                stack.pop()

        while len(stack) > 0:
            p = stack[-1]
            # if the top of stack is raw packet and
            if packets[p][2] == 0 and packets[p][3] <= packet[-1] - packets[p][-1]:
                stack.pop()
            else:
                break

        # if the currently scanned packet is not raw push it into stack
        if packet[1] != 4:
            stack.append(i)

    print(evaluate(0))


if __name__ == "__main__":
    with open("./input/day16.txt", "r") as f:
        lines = [a.strip() for a in f.readlines()]
    part1(lines[0])
    part2(lines[0])
