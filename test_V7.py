import unittest
import runFile


class TestV7(unittest.TestCase):
    def test_742(self):
        tests = [
            {"input": "1\n010101", "output": "Girar\n"},
            {"input": "1\n000111", "output": "No girar\n"},
            {"input": "1\n0011", "output": "Da igual\n"},
            {"input": "2\n010101\n000111", "output": "Girar\nNo girar\n"},
            {"input": "3\n010101\n000111\n0011", "output": "Girar\nNo girar\nDa igual\n"}
        ]

        for test in tests:
            output, error = runFile.run_script("742.py", test["input"])
            self.assertEqual(output, test["output"])


    def test_743(self):
        tests = [
            {"input": "1\n1\n0\n", "output": "0\n"},
            {"input": "1\n2\n0\n", "output": "1\n"},
            {"input": "3\n2 1 1\n0\n", "output": "1\n"},
            {"input": "1\n1\n1\n2\n3\n2 1 1\n0", "output": "0\n1\n1\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("743.py", test["input"])
            self.assertEqual(output, test["output"])
