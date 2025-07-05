from collections import deque

height, width = [int(x) for x in input().split()]

tableroUnos = [
    (i, j)
    for i in range(height)
    for j, val in enumerate(input().split())
    if int(val) == 1
]
plantillaUnos = [
    (i, j)
    for i in range(height)
    for j, val in enumerate(input().split())
    if int(val) == 1
]

visited = [[False] * width for _ in range(height)]
queue = deque()

# Add all 1's from board as BFS start points
for i in tableroUnos:
    queue.append((i[0], i[1], 0))  # (row, col, distance)
    visited[i[0]][i[1]] = True


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

while queue:
    x, y, dist = queue.popleft()

    if (x, y) in plantillaUnos:
        if dist == 0:
            # print(set(tableroUnos))
            # print(set(plantillaUnos))
            # print(set(tableroUnos) & set(plantillaUnos))
            print(len(tableroUnos)- len(set(tableroUnos) & set(plantillaUnos)))
        else:
            print(dist + len(tableroUnos) - 1)
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < height and 0 <= ny < width and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny, dist + 1))
