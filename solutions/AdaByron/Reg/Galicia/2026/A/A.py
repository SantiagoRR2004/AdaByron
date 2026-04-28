size = int(input())

if size == 1:
    print("! 0 0")

else:

    print("? 0 0", flush=True)
    bottomRight = int(input())
    print(f"? 0 {size-1}", flush=True)
    topRight = int(input())

    currentRow = 0

    if bottomRight > topRight:
        for i in range(size):
            if bottomRight + i == topRight + (size - 1 - i):
                rowValue = bottomRight + i
                currentRow = i
                break
    else:
        for i in range(size - 1, 0, -1):
            if bottomRight + i == topRight + (size - 1 - i):
                rowValue = bottomRight + i
                currentRow = i
                break

    print(f"? {size-1} {currentRow}", flush=True)
    rightValue = int(input())

    if rowValue > rightValue:
        for i in range(size):
            if rowValue + i == rightValue + (size - 1 - i):
                print(f"! {i} {currentRow}", flush=True)
                break

    else:
        for i in range(size - 1, 0, -1):
            if rowValue + i == rightValue + (size - 1 - i):
                print(f"! {i} {currentRow}", flush=True)
                break
