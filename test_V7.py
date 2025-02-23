import unittest
import runFile


class TestV7(unittest.TestCase):
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

    def test_757(self):
        tests = [
            {
                "input": """3
TTTST
STSTTSSS
TTTTTT""",
                "output": """3\n2\n6\n""",
            },
            {"input": "1\nTTTST", "output": "3\n"},
            {"input": "1\nSTSTTSSS", "output": "2\n"},
            {"input": "1\nTTTTTT", "output": "6\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("757.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_758(self):
        tests = [
            {
                "input": """3
7
9
11""",
                "output": """33 16
45 36
57 64
""",
            },
            {"input": "1\n7", "output": "33 16\n"},
            {"input": "1\n9", "output": "45 36\n"},
            {"input": "1\n11", "output": "57 64\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("758.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_745_1(self):
        tests = [
            {
                "input": "1 27 51 703 1000 0\n19397 940476005 0\n0",
                "output": "A AA AY AAA ALL\nABRA CADABRA\n",
            },
            {"input": "1 27 51 703 1000 0\n0", "output": "A AA AY AAA ALL\n"},
            {"input": "19397 940476005 0\n0", "output": "ABRA CADABRA\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("745.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_745_2(self):

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            input = f"{alphabet.index(letter)+1} 0\n0"
            output = f"{letter}\n"
            output, error = runFile.run_script("745.py", input)
            self.assertEqual(output, output)
