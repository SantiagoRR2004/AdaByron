import unittest
import runFile


class TestV7(unittest.TestCase):
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

    def test_744(self):
        tests = [
            {"input": "1\n1 2 3 4 0", "output": "2\n"},
            {"input": "4\n2 2 3 7 11 20 0", "output": "3\n"},
            {"input": "1\n1 2 3 4 0\n4\n2 2 3 7 11 20 0", "output": "2\n3\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("744.py", test["input"])
            self.assertEqual(output, test["output"])


