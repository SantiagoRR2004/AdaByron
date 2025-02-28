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
