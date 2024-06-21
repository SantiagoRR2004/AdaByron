import unittest
import runFile


class TestV7(unittest.TestCase):
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

    def test_749(self):
        tests = [
            {
                "input": """2 2 0
2 2 2
2 1 1 2
6 6 12
1 1 2 1 3 1 4 1 5 1 6 1 5 2 6 2 6 3 6 4 3 5 3 6
0 0 0""",
                "output": "4\n0\n35\n",
            },
            {
                "input": """2 2 0
0 0 0""",
                "output": "4\n",
            },
            {
                "input": """2 2 2
2 1 1 2
0 0 0""",
                "output": "0\n",
            },
            {
                "input": """6 6 12
1 1 2 1 3 1 4 1 5 1 6 1 5 2 6 2 6 3 6 4 3 5 3 6
0 0 0""",
                "output": "35\n",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("749.py", test["input"])
            self.assertEqual(output, test["output"])
