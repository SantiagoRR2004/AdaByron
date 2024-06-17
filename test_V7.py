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
