# https://aceptaelreto.com/problem/statement.php?id=753


def can(nums, index: int, suma: int, target: int) -> bool:
    """
    Recursive function to check if a subset of nums can sum to target.

    It checks thge next number or skips it recursively.
    """
    if suma == target:
        # Exit condition
        return True
    if suma > target or index == len(nums):
        # If the sum exceeds the target or we have considered all elements
        return False

    tempSum = suma
    for i in range(index, len(nums)):
        tempSum += nums[i]
        if tempSum > suma:
            break
        if tempSum == suma:
            # Exit condition
            return True

    return can(nums, index + 1, suma + nums[index], target) or can(
        nums, index + 1, suma, target
    )


nStones = int(input())


while nStones != 0:

    stones = [int(x) for x in input().split()]
    suma = sum(stones)

    if can(stones, 0, 0, suma // 2):
        print("SI")
    else:
        print("NO")

    nStones = int(input())

"""
Pista 1
Suma todos los pesos y divide por dos para saber lo que tienes que poner en cada lado de la balanza.

Pista 2
Haz una función que mire si existe algún subconjunto de los pesos cuya suma sea un valor dado (la mitad del total).

Pista 3
El número máximo de pesos es pequeño. Puedes utilizar recursión aunque pueda haber algo de solapamiento.
"""
