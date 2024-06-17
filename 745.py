# https://aceptaelreto.com/problem/statement.php?id=745


list1 = [int(x) for x in input().split()][:-1]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while list1:
    solution = []
    for code in list1:
        word = ""
        while code > 0:
            code -= 1
            word = alphabet[code % 26] + word
            code //= 26
        solution.append(word)

    print(" ".join(solution))
    list1 = [int(x) for x in input().split()][:-1]
