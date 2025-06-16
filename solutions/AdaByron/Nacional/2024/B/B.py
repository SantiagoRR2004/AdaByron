# Accepted

n_fil, n_camb = [int(x) for x in input().split()]
while n_fil != 0:

    filas = list(range(1, (n_fil * 6) + 1))

    for _ in range(n_camb):
        a, b = [int(x) for x in input().split()]
        a_index = a - 1
        b_index = b - 1

        if a_index // 6 <= b_index // 6:
            filas[b_index], filas[a_index] = filas[a_index], filas[b_index]
        else:
            if a % 2 == 0:
                a_pareja = a_index - 1
            else:
                a_pareja = a_index + 1
            if b % 2 == 0:
                b_pareja = b_index - 1
            else:
                b_pareja = b_index + 1

            aux = filas[a_pareja]
            filas[a_pareja] = filas[b_pareja]
            filas[b_pareja] = aux

    i = 0
    for i in range(n_fil):
        print(" ".join([str(x) for x in filas[i * 6 : (i + 1) * 6]]))
    print("---")

    n_fil, n_camb = [int(x) for x in input().split()]

    if n_fil == 0:
        break
