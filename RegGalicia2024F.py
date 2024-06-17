# https://en.wikipedia.org/wiki/Narcissistic_number


number = input()

while int(number) > 0:
    length = int(len(number))
    total = sum([int(x) ** length for x in number])

    if int(number) == total:
        print("SEGURO")
    else:
        print("INSEGURO")

    number = input()
