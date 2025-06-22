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


def deslizamientoMax(array: list, N: int) -> list:
    """
    Versión simplificada de deslizamiento para obtener solo el máximo.
    """
    W = len(array)
    max_window = [0] * (W - N + 1)

    max_deque = deque()

    for j in range(W):

        # Quitar elementos fuera de la ventana para máximo
        while max_deque and max_deque[0] <= j - N:
            max_deque.popleft()
        # Mantener decreciente para máximo
        while max_deque and array[max_deque[-1]] <= array[j]:
            max_deque.pop()
        max_deque.append(j)

        # Guardar valores cuando la ventana está completa
        if j >= N - 1:
            max_window[j - N + 1] = array[max_deque[0]]

    return max_window


def deslizamientoMin(array: list, N: int) -> list:
    """
    Versión simplificada de deslizamiento para obtener solo el mínimo.
    """
    W = len(array)
    min_window = [0] * (W - N + 1)

    min_deque = deque()

    for j in range(W):
        # Quitar elementos fuera de la ventana para mínimo
        while min_deque and min_deque[0] <= j - N:
            min_deque.popleft()
        # Mantener creciente para mínimo
        while min_deque and array[min_deque[-1]] >= array[j]:
            min_deque.pop()
        min_deque.append(j)

        # Guardar valores cuando la ventana está completa
        if j >= N - 1:
            min_window[j - N + 1] = array[min_deque[0]]

    return min_window


for _ in range(nCases):
    height, width, m, n = [int(x) for x in input().split()]

    maximumsRows = [[] for _ in range(width - n + 1)]
    minimumsRows = [[] for _ in range(width - n + 1)]

    for h in range(height):
        values = [int(x) for x in input().split()]
        min_window, max_window = deslizamiento(values, n)
        [maximumsRows[i].append(x) for i, x in enumerate(max_window)]
        [minimumsRows[i].append(x) for i, x in enumerate(min_window)]

    maximums = []
    minimums = []

    for w in range(width - n + 1):
        max_window = deslizamientoMax(maximumsRows[w], m)
        maximums.append(max_window)

        min_window = deslizamientoMin(minimumsRows[w], m)
        minimums.append(min_window)

    # Now we find the minimum of the difference
    answer = maximums[0][0] - minimums[0][0]

    for i in range(len(maximums)):
        for j in range(len(maximums[i])):
            diff = maximums[i][j] - minimums[i][j]
            if diff < answer:
                answer = diff

    print(answer)
