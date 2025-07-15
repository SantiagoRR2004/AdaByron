import sys
from collections import deque


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
            if downPath.get(indDown):
                distance = downPath[indDown]
                path += list(range(indDown, indDown - distance, -1))
                indDown -= distance
                currentPower += distance

            else:
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


"""
These are shortcuts meant to help with the search
The key is the starting index and the value the length of the shortcut

How do we ensure that following the entire shortcut keeps the
ascending order?

We always choose the lower number of the borders to be explored
or the one on the left if they are equal.

x₂ is the shortcut stored.
x₁ and x₃ are the borders that can't be reached from inside the shortcut.
The current path has y₁ and x₃ and it's borders are x₂ₙ and y₂
We need to prove that all from inside x₂ are lower than y

x₁, (x₂₁, ..., x₂ₙ), x₃, (y₁₁, ..., y₁ₘ), y₂

    x₁ > n + InitialPower
    ∀x ∈ {x₂}, x < x₁
    x₃ > n + InitialPower
    ∀x ∈ {x₂}, x < x₃
    x₃ <= m + InitialPower
    y₂ >= m + InitialPower

==>

    y₂ >= x₃
    ∀x ∈ {x₂}, y₂ > x
    
The next step would be to choose between x₁ and y
"""
downPath = {}


length, IPower = [int(x) for x in input().split()]

values = []
miniPath = deque()
nReapetedValues = 1
ascending = False


while len(values) < length:
    # Iterate this way to preprocess
    n = ""
    while True:
        char = sys.stdin.read(1)
        if char == " " or char == "\n" or not char:
            break
        n += char

    n = int(n)
    values.append(n)

    if not miniPath:
        miniPath.append(n)
    else:
        if n < miniPath[-1]:
            if not ascending:
                miniPath.append(n)
            else:
                downPath[len(values) - 2] = len(miniPath)
                miniPath = deque([miniPath[-1]] * nReapetedValues + [n])
                ascending = False

            nReapetedValues = 1

        elif n > miniPath[-1]:
            if ascending:
                miniPath.append(n)
            else:
                miniPath = deque([miniPath[-1]] * nReapetedValues + [n])
                ascending = True

            nReapetedValues = 1

        else:
            # Equals
            miniPath.append(n)
            nReapetedValues += 1


"""
In the validIndexes we keep the indexes that we
can explore.

When we find a partial path we know that starting from any position
in the path we can't find a solution
"""
validIndexes = [x for x in range(length) if values[x] <= IPower]


while validIndexes:

    path = getPath(
        validIndexes[0],
        IPower + 1,
    )

    downPath[max(path)] = len(path)

    pathSet = set(path)
    validIndexes = [item for item in validIndexes if item not in pathSet]


print("FALLIDA")
