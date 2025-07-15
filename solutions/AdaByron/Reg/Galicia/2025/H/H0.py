"""
This is mean to be a version that always works to check
that the result is the same with the faster ones
"""


def getPath(initialIndex: int, currentPower: int) -> list:

    exitFlag = False
    indDown = initialIndex - 1
    indUp = initialIndex + 1
    path = [initialIndex]

    # We no longer need it
    del initialIndex

    while not exitFlag:
        if len(path) == length:
            # We have finished the path
            print(" ".join([str(x + 1) for x in path]))
            quit()

        elif (
            indDown >= 0  # Valid indDown
            and values[indDown] <= currentPower  # Enough power
        ):
            path += [indDown]
            indDown -= 1
            currentPower += 1

        elif (
            indUp < len(values)  # Valid indUp
            and values[indUp] <= currentPower  # Enough power
        ):
            path += [indUp]
            indUp += 1
            currentPower += 1

        else:
            # Both borders are too strong
            exitFlag = True

    return path


length, IPower = [int(x) for x in input().split()]

values = [int(x) for x in input().split()]

validIndexes = [x for x in range(length) if values[x] <= IPower]


for index in validIndexes:

    path = getPath(
        index,
        IPower + 1,
    )


print("FALLIDA")
