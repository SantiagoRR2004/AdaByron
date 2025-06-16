# https://aceptaelreto.com/problem/statement.php?id=754

import sys


for line in sys.stdin:
    letters = {}
    for letter in line.strip():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    numberOfOdds = sum(1 for count in letters.values() if count % 2 != 0)
    if numberOfOdds > 1:
        print("NO HAY")

    else:
        solution = ""
        middle = ""

        for letter in sorted(letters, reverse=True):
            solution = (
                letter * (letters[letter] // 2)
                + solution
                + letter * (letters[letter] // 2)
            )

            if letters[letter] % 2 != 0:
                middle = letter

        solution = (
            solution[: len(solution) // 2] + middle + solution[len(solution) // 2 :]
        )

        print(solution)
