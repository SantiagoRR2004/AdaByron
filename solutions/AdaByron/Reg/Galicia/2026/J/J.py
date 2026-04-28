nCases = int(input())

for _ in range(nCases):
    nCols = int(input())
    cols = [int(i) for i in input().split()]

    if nCols % 2 != 0:
        print("CELTA")
    elif not (1 in cols and 0 in cols):
        print("CELTA")
    elif sum(cols) != nCols / 2:
        print("CELTA")
    else:
        char_i = cols[0]
        while cols[-1] == cols[0]:
            cols.insert(0, char_i)
            cols.pop()

        ct = 1
        idx = 1
        while cols[idx] == char_i:
            ct += 1
            idx += 1

        if nCols % ct != 0:
            print("CELTA")

        else:
            counter = 1
            booleanFlag = True
            char_i = not char_i
            while idx < nCols:
                currentList = cols[idx : idx + ct]
                if sum(currentList) == char_i * ct:
                    idx += ct
                    counter += 1
                    char_i = not char_i
                else:
                    print("CELTA")
                    booleanFlag = False
                    break
            if booleanFlag:
                print(counter)
