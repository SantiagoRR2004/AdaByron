import unittest
import runFile


class TestV7(unittest.TestCase):
    def test_742(self):
        tests = [
            {"input": "1\n010101", "output": "Girar\n"},
            {"input": "1\n000111", "output": "No girar\n"},
            {"input": "1\n0011", "output": "Da igual\n"},
            {"input": "2\n010101\n000111", "output": "Girar\nNo girar\n"},
            {
                "input": "3\n010101\n000111\n0011",
                "output": "Girar\nNo girar\nDa igual\n",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("742.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_743(self):
        tests = [
            {"input": "1\n1\n0", "output": "0\n"},
            {"input": "1\n2\n0", "output": "1\n"},
            {"input": "3\n2 1 1\n0", "output": "1\n"},
            {"input": "1\n1\n1\n2\n3\n2 1 1\n0", "output": "0\n1\n1\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("743.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_746(self):
        tests = [
            {
                "input": "5 10\n1 9 2 8 5\n5 10\n5 8 2 9 1\n5 10\n1 2 3 4 5\n0 0",
                "output": "2\n2\n0\n",
            },
            {"input": "5 10\n1 9 2 8 5\n0 0", "output": "2\n"},
            {"input": "5 10\n5 8 2 9 1\n0 0", "output": "2\n"},
            {"input": "5 10\n1 2 3 4 5\n0 0", "output": "0\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("746.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_747(self):
        tests = [
            {
                "input": """4 5
.X...
.XX..
..X..
.....
2 6
...X..
...X..
0 0""",
                "output": "SI\nNO\n",
            },
            {
                "input": """4 5
.X...
.XX..
..X..
.....
0 0""",
                "output": "SI\n",
            },
            {
                "input": """2 6
...X..
...X..
0 0""",
                "output": "NO\n",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("747.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_748(self):
        tests = [
            {
                "input": """9
Buford 1
Stubble 1
Ceegar 1
Buford 2
Buck 1
? 2 Buford Buck
Needles 1
Buford 1
? 3 Ceegar Stubble Buford
0""",
                "output": "4\n3\n---\n",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("748.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_750(self):
        tests = [
            {
                "input": """1
20
506
0""",
                "output": "10\n21\n32\n",
            },
            {
                "input": """1
0""",
                "output": "10\n",
            },
            {
                "input": """20
0""",
                "output": "21\n",
            },
            {
                "input": """506
0""",
                "output": "32\n",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("750.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_751(self):
        tests = [
            {
                "input": """4
1756 1791 1770 1827
1756 1791 1706 1790
1642 1727 1769 1821
1706 1790 1642 1727""",
                "output": "22\n35\n0\n22\n",
            },
            {"input": "1\n1756 1791 1770 1827", "output": "22\n"},
            {"input": "1\n1756 1791 1706 1790", "output": "35\n"},
            {"input": "1\n1642 1727 1769 1821", "output": "0\n"},
            {"input": "1\n1706 1790 1642 1727", "output": "22\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("751.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_752(self):
        tests = [
            {
                "input": """5 4
1 1 3 3
3 5
0 1 1 1 1
8 3
5 0 2
0 0""",
                "output": "2 3\n3 2\nNO ENTRAN\n",
            },
            {
                "input": """5 4
1 1 3 3
0 0""",
                "output": "2 3\n",
            },
            {
                "input": """3 5
0 1 1 1 1
0 0""",
                "output": "3 2\n",
            },
            {
                "input": """8 3
5 0 2
0 0""",
                "output": "NO ENTRAN\n",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("752.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_754(self):
        tests = [
            {
                "input": """lamentablemente
rollo
conocen
reordenando
ala
palindromo""",
                "output": """aeelmntbtnmleea
lorol
cnoeonc
denoraroned
ala
NO HAY
""",
            },
            {"input": "lamentablemente", "output": "aeelmntbtnmleea\n"},
            {"input": "rollo", "output": "lorol\n"},
            {"input": "conocen", "output": "cnoeonc\n"},
            {"input": "reordenando", "output": "denoraroned\n"},
            {"input": "ala", "output": "ala\n"},
            {"input": "palindromo", "output": "NO HAY\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("754.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_755(self):
        tests = [
            {
                "input": """4
10 10
5 10
8 6
46349 46351""",
                "output": """1
2
12
2148322499
""",
            },
            {"input": """1\n 10 10""", "output": "1\n"},
            {"input": """1\n 5 10""", "output": "2\n"},
            {"input": """1\n 8 6""", "output": "12\n"},
            {"input": """1\n 46349 46351""", "output": "2148322499\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("755.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_756(self):
        tests = [
            {
                "input": """1 2 3 4 5 6 7 8 9 10 11 12 13 15 14 16
2 3 1 4 5 6 7 8 9 10 11 12 13 14 15 16
2 3 1 4 5 6 7 8 9 10 11 12 13 15 14 16""",
                "output": """NO
SI
NO
""",
            },
            {"input": "1 2 3 4 5 6 7 8 9 10 11 12 13 15 14 16", "output": "NO\n"},
            {"input": "2 3 1 4 5 6 7 8 9 10 11 12 13 14 15 16", "output": "SI\n"},
            {"input": "2 3 1 4 5 6 7 8 9 10 11 12 13 15 14 16", "output": "NO\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("756.py", test["input"])
            self.assertEqual(output, test["output"])
