# https://en.wikipedia.org/wiki/Monotone_priority_queue

from collections import deque

nCases = int(input())


def deslizamiento(array: list, N: int) -> tuple:
    W = len(array)
    min_window = [0] * (W - N + 1)
    max_window = [0] * (W - N + 1)

    min_deque = deque()
    max_deque = deque()

    for j in range(W):
        # Quitar elementos fuera de la ventana para mínimo
        while min_deque and min_deque[0] <= j - N:
            min_deque.popleft()
        # Mantener creciente para mínimo
        while min_deque and array[min_deque[-1]] >= array[j]:
            min_deque.pop()
        min_deque.append(j)

        # Quitar elementos fuera de la ventana para máximo
        while max_deque and max_deque[0] <= j - N:
            max_deque.popleft()
        # Mantener decreciente para máximo
        while max_deque and array[max_deque[-1]] <= array[j]:
            max_deque.pop()
        max_deque.append(j)

        # Guardar valores cuando la ventana está completa
        if j >= N - 1:
            min_window[j - N + 1] = array[min_deque[0]]
            max_window[j - N + 1] = array[max_deque[0]]

    return min_window, max_window


MAXNUMBER = 10**6 + 1

for _ in range(nCases):
    height, width, m, n = [int(x) for x in input().split()]

    finalResult = MAXNUMBER

    maximumsRows = [deque() for _ in range(width - n + 1)]
    minimumsRows = [deque() for _ in range(width - n + 1)]

    for h in range(height):
        values = [int(x) for x in input().split()]
        min_window, max_window = deslizamiento(values, n)

        # Don't wait until the end to have smaller loops
        for i in range(width - n + 1):
            maximumsRows[i].append(max_window[i])
            minimumsRows[i].append(min_window[i])

            # The deques are now full
            if h >= m - 1:

                max_col = max(maximumsRows[i])
                min_col = min(minimumsRows[i])
                finalResult = min(finalResult, max_col - min_col)

                maximumsRows[i].popleft()
                minimumsRows[i].popleft()

    print(finalResult)
