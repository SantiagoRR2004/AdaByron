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
