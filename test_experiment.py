import unittest
import runFile


def create_test_method(name: str, inputPath: str, filePath: str, outputPath: str) -> callable:
    """
    Create a test method for the given test case.
    
    Args:
        - name: The name of the test case.
        - inputPath: The path to the input file.
        - filePath: The path to the script file.
        - outputPath: The path to the output file.
    
    Returns:
        - A test method.
    """
    def test_method(self):
        with open(inputPath) as inputFile:
            output, error = runFile.run_script(filePath, inputFile.read())

        with open(outputPath) as outputFile:
            self.assertEqual(output, outputFile.read() + "\n")

    test_method.__name__ = f"test_{name}"
    return test_method


# Dynamically create test methods.
class DynamicTestCase(unittest.TestCase):
    pass


# Test configurations.
test_cases = [
    ("105", "tests/105/1.in", "105.py", "tests/105/1.ans"),
    # Add more test cases as needed.
]

# Add methods to the TestCase class.
for test_id, input_path, file_path, output_path in test_cases:
    test_method = create_test_method(test_id, input_path, file_path, output_path)
    setattr(DynamicTestCase, test_method.__name__, test_method)

