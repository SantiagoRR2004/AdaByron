from functools import lru_cache

N, E, S, W = 1, 2, 4, 8


def rotate90(mask: int) -> int:
    res = 0
    if mask & N:
        res |= E
    if mask & E:
        res |= S
    if mask & S:
        res |= W
    if mask & W:
        res |= N
    return res


filas, columnas = [int(x) for x in input().split()]

while filas != 0 and columnas != 0:

    opts = [[None] * columnas for _ in range(filas)]

    for i in range(filas):
        pieces = input().split()
        for j in range(columnas):
            s = pieces[j]

            mask = 0
            if s != "x":
                for ch in s:
                    if ch == "N":
                        mask |= N
                    elif ch == "E":
                        mask |= E
                    elif ch == "S":
                        mask |= S
                    elif ch == "W":
                        mask |= W

            cur = mask
            seen = set()
            for _ in range(4):
                seen.add(cur)
                cur = rotate90(cur)

            opts[i][j] = tuple(seen)

    @lru_cache(None)
    def dfs(r: int, c: int, mask: int, next_mask: int, left_need: int) -> bool:
        if r == filas:
            return mask == 0

        if c == columnas:
            return dfs(r + 1, 0, next_mask, 0, 0)

        need_north = (mask >> c) & 1

        for m in opts[r][c]:
            n = (m & N) != 0
            e = (m & E) != 0
            s = (m & S) != 0
            w = (m & W) != 0

            if r == 0 and n:
                continue
            if r == filas - 1 and s:
                continue
            if c == 0 and w:
                continue
            if c == columnas - 1 and e:
                continue

            if n != need_north:
                continue
            if w != left_need:
                continue

            nm = next_mask
            if s:
                nm |= 1 << c
            else:
                nm &= ~(1 << c)

            if dfs(r, c + 1, mask, nm, int(e)):
                return True

        return False

    print("SOLUCIONABLE" if dfs(0, 0, 0, 0, 0) else "NOSOLUCIONABLE")

    filas, columnas = [int(x) for x in input().split()]
