nCases = int(input())

letters = {"R", "C", "H"}

while nCases != 0:
    music = input().split()

    if not ("R" in music and "C" in music and "H" in music):
        print("NO SE PUEDE")
    else:
        r = music.index("R")
        c = music.index("C")
        h = music.index("H")
        minimum = nCases

        for i in range(min(r, c, h), nCases):
            if music[i] == "R":
                r = i
            if music[i] == "C":
                c = i
            if music[i] == "H":
                h = i

            minimum = min(minimum, max(r, c, h) - min(r, c, h) + 1)

        print(minimum)

    nCases = int(input())
