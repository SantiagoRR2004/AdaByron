# Accepted

n = int(input())

for _ in range(n):
    word = list(input())

    letters = set(word)

    count = word.count(word[0])

    for l in letters:
        if word.count(l) != count:
            print("NO")
            break
    else:
        print("SI")
