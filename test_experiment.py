import unittest
import runFile


class TestV7(unittest.TestCase):
    def test_105(self):
        inputPath = "tests/105/1.in"
        filePath = "105.py"
        outputPath = "tests/105/1.ans"

        output, error = runFile.run_script(filePath, open(inputPath).read())

        self.assertEqual(output, open(outputPath).read() + "\n")
