# https://stackoverflow.com/questions/76270040/solving-algorithm-for-a-rotating-pipes-game


class Connection:
    def __init__(self, row, col, row2, col2):
        self.row = row
        self.col = col
        self.row2 = row2
        self.col2 = col2

    def __eq__(self, other) -> bool:
        if isinstance(other, Connection):
            one = (
                self.row == other.row
                and self.col == other.col
                and self.row2 == other.row2
                and self.col2 == other.col2
            )
            two = (
                self.row == other.row2
                and self.col == other.col2
                and self.row2 == other.row
                and self.col2 == other.col
            )
            return one or two
        return False

    def __hash__(self) -> int:
        pairs = sorted([(self.row, self.col), (self.row2, self.col2)])
        return hash((pairs[0], pairs[1]))

    def notConnected(self, matrix) -> list:
        """
        This returns which of the coordinates has a value different than 0
        """
        if matrix[self.row][self.col] != 0:
            return self.row, self.col
        elif matrix[self.row2][self.col2] != 0:
            return self.row2, self.col2
        return None


def getConnections(matrix, row, col, restriction: Connection = None):
    """
    This function returns the possible connections for a given cell in the matrix

    Each connection is formed by 4 numbers:
        - The row of the origin
        - The column of the origin
        - The row of the destination
        - The column of the destination

    """
    if matrix[row][col] == 4:
        allConections = [
            [
                Connection(row, col, row + 1, col),
                Connection(row, col, row - 1, col),
                Connection(row, col, row, col + 1),
                Connection(row, col, row, col - 1),
            ]
        ]
    elif matrix[row][col] == 3:
        allConections = [
            [
                Connection(row, col, row + 1, col),
                Connection(row, col, row - 1, col),
                Connection(row, col, row, col + 1),
            ],
            [
                Connection(row, col, row + 1, col),
                Connection(row, col, row - 1, col),
                Connection(row, col, row, col - 1),
            ],
            [
                Connection(row, col, row + 1, col),
                Connection(row, col, row, col + 1),
                Connection(row, col, row, col - 1),
            ],
            [
                Connection(row, col, row - 1, col),
                Connection(row, col, row, col + 1),
                Connection(row, col, row, col - 1),
            ],
        ]
    elif matrix[row][col] == 2:
        allConections = [
            [Connection(row, col, row + 1, col), Connection(row, col, row, col + 1)],
            [Connection(row, col, row + 1, col), Connection(row, col, row, col - 1)],
            [Connection(row, col, row - 1, col), Connection(row, col, row, col + 1)],
            [Connection(row, col, row - 1, col), Connection(row, col, row, col - 1)],
        ]
    elif matrix[row][col] == 1:
        allConections = [
            [Connection(row, col, row + 1, col)],
            [Connection(row, col, row - 1, col)],
            [Connection(row, col, row, col + 1)],
            [Connection(row, col, row, col - 1)],
        ]

    toret = []

    if restriction:
        for conns in allConections:
            if restriction in conns:
                conns.remove(restriction)
                toret.append(conns)
    else:
        toret = allConections
    return toret


def solvePuzzle(matrix, connections) -> bool:
    # First we check if something needs to be connected
    if not connections:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                value = matrix[row][col]
                if value != 0:
                    # We get a list of the possibilities for the connections
                    # It only needs one to be possible for the puzzle to be solvable
                    newConnections = getConnections(matrix, row, col)
                    matrix[row][col] = 0
                    for con in newConnections:
                        solvable = solvePuzzle(matrix, con)
                        if solvable:
                            return True
                    matrix[row][col] = value
                    # If we reach this point it means that the puzzle with the current value is not solvable
                    return False
        # If all the values are 0 this means it is solvable
        return True
    else:
        # We need to check that all the connections are possible
        for con in connections:
            # We need to see which of the values is not cero
            notConnected = con.notConnected(matrix)
            if notConnected:
                value = matrix[notConnected[0]][notConnected[1]]
                newConnections = getConnections(
                    matrix, notConnected[0], notConnected[1], restriction=con
                )
                matrix[notConnected[0]][notConnected[1]] = 0
                for newCons in newConnections:
                    con2 = connections.copy()
                    con2.remove(con)
                    for connection in newCons:
                        if connection in connections:
                            con2.remove(connection)
                        else:
                            con2.append(connection)
                    solvable = solvePuzzle(matrix, con2)
                    if solvable:
                        return True
                matrix[notConnected[0]][notConnected[1]] = value
                return False
            else:
                # If both values are 0 it means the connection is impossible
                return False
        return False


filas, columnas = [int(x) for x in input().split()]

while filas != 0 and columnas != 0:

    matrix = [[0 for x in range(columnas + 2)]]
    for i in range(filas):
        data = input().split()
        row = [0]
        for number in data:
            if number == "x":
                row.append(0)
            else:
                row.append(len(number))
        row.append(0)
        matrix.append(row)
    matrix.append([0 for x in range(columnas + 2)])

    if sum([sum(row) for row in matrix]) % 2 != 0:
        print("NOSOLUCIONABLE")
    else:

        # Now we have a matrix of numbers that has ceros on the borders
        solvable = solvePuzzle(matrix, [])

        if solvable:
            print("SOLUCIONABLE")
        else:
            print("NOSOLUCIONABLE")

    filas, columnas = [int(x) for x in input().split()]
