#  https://aceptaelreto.com/problem/statement.php?id=743
n = int(input())

while n != 0:
    finalPage = 0

    list1 = [int(x) for x in input().split()]
    start = sum(list1)
    end = sum([x // 2 if x % 2 == 0 else x // 2 + 1 for x in list1])

    print(start - end)

    n = int(input())
