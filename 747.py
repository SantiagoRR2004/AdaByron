# https://aceptaelreto.com/problem/statement.php?id=747
# https://en.wikipedia.org/wiki/Flood_fill
# BFS


def is_path_exists(matrix):
    rows, cols = len(matrix), len(matrix[0])
    if matrix[0][0] != 0 or matrix[rows - 1][cols - 1] != 0:
        return False

    # Directions for moving up, down, left, right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Initialize queue with the starting position and mark it as visited
    queue = [(0, 0)]
    visited = set()
    visited.add((0, 0))

    while queue:
        x, y = queue.pop(0)

        if (x, y) == (rows - 1, cols - 1):
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and matrix[nx][ny] == 0
                and (nx, ny) not in visited
            ):
                queue.append((nx, ny))
                visited.add((nx, ny))

    return False


rows, cols = [int(x) for x in input().split()]

while rows != 0 and cols != 0:

    matrix = []
    for _ in range(rows):
        row = []
        for i in list(input()):
            if i == ".":
                row.append(0)
            else:
                row.append(1)

        matrix.append(row)

    if is_path_exists(matrix):
        print("SI")
    else:
        print("NO")

    rows, cols = [int(x) for x in input().split()]
