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

validIndexListIndex = 0

while validIndexListIndex < len(validIndexes):

    path = getPath(
        validIndexes[validIndexListIndex],
        IPower + 1,
    )

    validIndexes[validIndexListIndex + 1 :] = [
        x for x in validIndexes[validIndexListIndex + 1 :] if x not in path
    ]

    validIndexListIndex += 1

print("FALLIDA")
