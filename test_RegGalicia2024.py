import unittest
import runFile


class TestRegGalicia2024(unittest.TestCase):
    def test_A(self):
        tests = [
            {"input": "10 2 2 1\n7 3 2 100\n12 3 1 10", "output": "241\n"},
            {"input": "100 1 25 50\n15 5 20 10", "output": "200\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("RegGalicia2024A.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_B(self):
        tests = [
            {"input": "4\n-angela\n+antonia\n-nico\n+olga", "output": "2\nang\nn\n"},
            {"input": "3\n-ana\n+anabella\n+anahi", "output": "-1\n"},
            {"input": "2\n+anabel\n-anabela", "output": "1\nanabela\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("RegGalicia2024B.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_C(self):
        tests = [
            {
                "input": "3\n4 2\n1 2\n2 3\n5 3\n1 2\n2 3\n1 3\n6 3\n1 2\n3 4\n5 6",
                "output": "2 3\n3 3\n3 8\n",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("RegGalicia2024C.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_D(self):
        tests = [
            {
                "input": """7 4 5
5 4 1 1 1 1 10
3 4 5 6 5
5 4 3 7 3
1 3 3 4 6
2 3 7 4 6""",
                "output": "19\n",
            },
            {
                "input": """7 4 5
5 4 1 1 1 1 10
3 4 5 6 5
5 4 3 6 3
1 2 3 4 6
2 3 7 4 6""",
                "output": "20\n",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("RegGalicia2024D.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_E(self):
        tests = [
            {
                "input": """5 7
1 2 4 1 1 0 1
0 1 0 3 1 3 1
1 0 0 1 0 0 0
0 1 5 0 0 3 0
1 6 0 0 5 2 1
3
1 1 2 3 5
2 2 4 4 6
3 4 1 5 7""",
                "output": "3 24\n",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("RegGalicia2024E.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_F(self):
        tests = [
            {
                "input": """8
372
1634
154
0""",
                "output": """SEGURO
INSEGURO
SEGURO
INSEGURO\n""",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("RegGalicia2024F.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_G(self):
        tests = [
            {
                "input": """2
4 3
1 2
2 3
3 4
3 3
1 2
2 3
3 1""",
                "output": """Que comience la batalla
Mejor nos vamos de cena o algo\n""",
            },
            {
                "input": """1
10 10
1 2
2 3
3 4
4 1
4 5
5 6
6 7
7 4
8 9
9 1""",
                "output": "Que comience la batalla\n",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("RegGalicia2024G.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_H_1(self):
        tests = [
            {
                "input": """3 3
NW NW x
NES NESW W
E W x
2 3
ES NS x
x NE N
0 0""",
                "output": "SOLUCIONABLE\nNOSOLUCIONABLE\n",
            },
            {
                "input": """3 3
NW NW x
NES NESW W
E W x
0 0""",
                "output": "SOLUCIONABLE\n",
            },
            {
                "input": """2 3
ES NS x
x NE N
0 0""",
                "output": "NOSOLUCIONABLE\n",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("RegGalicia2024H.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_H_2(self):
        input = """3 3
NW N x
NES NESW W
E W x
0 0"""
        solution = "NOSOLUCIONABLE\n"
        output, error = runFile.run_script("RegGalicia2024H.py", input)
        self.assertEqual(solution, output)

    def test_H_3(self):
        input = """3 3
NW NW NW
NW x NW
NW NW NW
0 0"""
        solution = "NOSOLUCIONABLE\n"
        output, error = runFile.run_script("RegGalicia2024H.py", input)
        self.assertEqual(solution, output)

    def test_H_4(self):
        input = """4 4
x x x x
x NW NW x
x NW NW x
x x x x
0 0"""
        solution = "SOLUCIONABLE\n"
        output, error = runFile.run_script("RegGalicia2024H.py", input)
        self.assertEqual(solution, output)

    def test_I(self):
        tests = [
            {
                "input": """7
100 80 60 70 60 75 85
10
25 530 120 910 330 50 50 102 55 75
15
56 67 45 2 46 57 68 79 80 90 189 200 398 560 72
0""",
                "output": """1 1 1 2 1 4 6
1 2 1 4 1 1 2 3 1 2
1 2 1 1 3 4 7 8 9 10 11 12 13 14 1\n""",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("RegGalicia2024I.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_J(self):
        tests = [
            {
                "input": """10
25 50 100 25 30 25 35 5 100 5
12
8 75 30 4 50 10 10 50 10 10 60 10
7
250 50 80 50 250 70 100
0""",
                "output": """25
10
50\n""",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("RegGalicia2024J.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_K(self):
        tests = [
            {
                "input": """aaeoollgg
7
gallega
galleta
argolla
gazapo
anilla
geotermia
gallego""",
                "output": "gallega\n",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("RegGalicia2024K.py", test["input"])
            self.assertEqual(output, test["output"])
