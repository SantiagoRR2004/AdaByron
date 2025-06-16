# https://aceptaelreto.com/problem/statement.php?id=748

nOperation = int(input())

while nOperation > 0:
    cowboys = {}
    for _ in range(nOperation):
        operation = input().split()
        if operation[0] == "?":
            exits = int(operation[1])
            guns = 0
            for i in range(2, 2 + exits):
                if operation[i] in cowboys.keys():
                    guns += cowboys[operation[i]]
                    cowboys.pop(operation[i])
            print(guns)
        else:
            if operation[0] in cowboys.keys():
                cowboys[operation[0]] += int(operation[1])
            else:
                cowboys[operation[0]] = int(operation[1])

    print("---")
    nOperation = int(input())

