n = int(input())

buenos = []
malos = []

for _ in range(n):
    persona = input()
    if persona[0] == "+":
        buenos.append(persona[1:])
    else:
        malos.append(persona[1:])

