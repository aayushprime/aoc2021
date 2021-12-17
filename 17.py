# credits + beautifully explained
# https://github.com/mebeim/aoc/blob/master/2021/README.md#day-17---trick-shot
def solve(xr, yr):
    x1, x2 = xr.strip().split("=")[1].split("..")
    y1, y2 = yr.strip().split("=")[1].split("..")
    x1, x2, y1, y2 = list(map(lambda x: int(x), [x1, x2, y1, y2]))

    # the probe will fall with -V(initial) and this has to be less than ymin
    print(y1 * (y1 + 1) // 2)

    def search(xmin, xmax, ymin, ymax):
        total = 0
        # search within reasonable ranges
        for v0x in range(1, xmax + 1):
            for v0y in range(ymin, -ymin):
                x, y = 0, 0
                vx, vy = v0x, v0y
                # While we did not get past the target (on either axis)
                while x <= xmax and y >= ymin:
                    # If we are inside the target, these v0x and v0y were good
                    if x >= xmin and y <= ymax:
                        total += 1
                        break
                    # Advance the trajectory following the rules
                    x, y = (x + vx, y + vy)
                    vy -= 1
                    if vx > 0:  # ... also remembering that vx can never go below 0
                        vx -= 1
        return total

    print(search(x1, x2, y1, y2))


if __name__ == "__main__":
    with open("./input/day17.txt", "r") as f:
        xr, yr = f.read().split(":")[1:][0].split(",")
        solve(xr, yr)
