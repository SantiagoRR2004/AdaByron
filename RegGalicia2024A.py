gramosTotalMasa, tiposChorizo, masaSinRelleno, precioSinRelleno = [int(x) for x in input().split()]

conChorizo = []

for _ in range(tiposChorizo):
    gramosTotalChorizo, gramosChorizo, gramosMasa, precio = [int(x) for x in input().split()]
    conChorizo.append({"BollosTotales":gramosTotalChorizo//gramosChorizo, "GramosMasa":gramosMasa, "Precio":precio})

