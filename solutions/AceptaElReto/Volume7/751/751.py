# https://aceptaelreto.com/problem/statement.php?id=751

n = int(input())


for _ in range(n):
    start1, end1, start2, end2 = [int(x) for x in input().split()]

    start = max(start1, start2)
    end = min(end1, end2)

    if start <= end:
        print(end - start + 1)
    else:
        print(0)
