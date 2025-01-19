letters = list(input())
numWords = int(input())

solution = ""

for i in range(numWords):
    word = input()
    # First we check if it can be better
    if len(word) > len(solution) or (len(word) == len(solution) and word < solution):
        lettersCopy = letters.copy()
        contained = True
        # Then we check if it is possible
        for letter in word:
            if letter in lettersCopy:
                lettersCopy.remove(letter)
            else:
                contained = False
                break
        if contained:
            solution = word


if solution == "":
    print("No es posible")
else:
    print(solution)
