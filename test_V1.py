import unittest
import runFile


class TestV7(unittest.TestCase):
    def test_105(self):
        tests = [
            {
                "input": """185.50
250.36
163.45
535.20
950.22
450.38
185.50
250.36
163.45
535.20
950.22
100.00
185.50
250.36
185.50
535.20
950.22
950.22
185.50
250.36
163.45
535.20
950.22
400.00
185.50
250.36
165.50
535.20
950.22
950.22
-1""",
                "output": """SABADO JUEVES SI
SABADO DOMINGO NO
EMPATE EMPATE SI
SABADO JUEVES NO
EMPATE JUEVES SI\n""",
            },
        ]

        for test in tests:
            output, error = runFile.run_script("105.py", test["input"])
            self.assertEqual(output, test["output"])

    def test_120(self):
        tests = [
            {
                "input": """5 1
3 0
3 4
0 0""",
                "output": """65
12
24\n""",
            },
            {"input": "5 1\n0 0", "output": "65\n"},
            {"input": "3 0\n0 0", "output": "12\n"},
            {"input": "3 4\n0 0", "output": "24\n"},
        ]

        for test in tests:
            output, error = runFile.run_script("120.py", test["input"])
            self.assertEqual(output, test["output"])
