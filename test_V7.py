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
