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

        # We check that the python file exists
        if not os.path.exists(f"{name}.py"):
            raise Exception(f"File {name}.py not found")

        # Get the name of all the files in tests/name
        files = os.listdir(os.path.join("tests", name))

        # We get the names of the input and output files
        ins = set([f[:-3] for f in files if f.endswith(".in")])
        answers = set([f[:-4] for f in files if f.endswith(".ans")])

        # We check that there are input and output files
        if len(ins) == 0:
            raise Exception(f"No input files found")

        if len(answers) == 0:
            raise Exception(f"No output files found")

        # We check that the names of the input and output files are the same
        if ins != answers:
            extraIns = ins - answers
            extraAnswers = answers - ins
            raise Exception(
                f"Not corresponding .ans of {extraAnswers}.\n Not corresponding .in of {extraIns}"
            )

        # We loop through all the input files
        for file in ins.union(answers):
            with open(os.path.join("tests", name, file + ".in")) as inputFile:
                output, error = runFile.run_script(name + ".py", inputFile.read())

            with open(os.path.join("tests", name, file + ".ans")) as outputFile:
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
