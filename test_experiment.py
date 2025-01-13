import unittest
import runFile
import os


def create_test_method(name: str) -> callable:
    """
    Create a test method for the given test case.

    Args:
        - name: The name of the test case.

    Returns:
        - A test method.
    """

    def test_method(self):
        with open(os.path.join("tests", name, "1.in")) as inputFile:
            output, error = runFile.run_script(name + ".py", inputFile.read())

        with open(os.path.join("tests", name, "1.ans")) as outputFile:
            self.assertEqual(output, outputFile.read() + "\n")

    test_method.__name__ = f"test_{name}"
    return test_method


# Dynamically create test methods.
class DynamicTestCase(unittest.TestCase):
    pass


# Test configurations.
test_cases = [
    "105",
    "120",
    # Add more test cases as needed.
]

# Add methods to the TestCase class.
for test_id in test_cases:
    test_method = create_test_method(test_id)
    setattr(DynamicTestCase, test_method.__name__, test_method)
