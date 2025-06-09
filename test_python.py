import unittest
import runFile
import os


def create_test_method_python(
    name: str, programmingLanguage: str, extension: str
) -> callable:
    """
    Create a test method for the given test case.

    Args:
        - name: The name of the test case.

    Returns:
        - A test method.
    """

    def test_method(self):

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
        
        # Get the run_script_ dinamically
        scriptByLanguageName = f"run_script_{programmingLanguage}"
        scriptByLanguage = getattr(runFile, scriptByLanguageName)

        # We loop through all the input files
        for file in ins.union(answers):
            with open(os.path.join("tests", name, file + ".in")) as inputFile:
                output, error = scriptByLanguage(
                    name + extension, inputFile.read()
                )

            with open(os.path.join("tests", name, file + ".ans")) as outputFile:
                self.assertEqual(output, outputFile.read() + "\n")

    test_method.__name__ = f"test_{programmingLanguage}"
    return test_method


def addTests(cls: type) -> None:
    name = cls.__name__

    if os.path.exists(f"{name}.py"):
        # Create a test method for the class
        testMethod = create_test_method_python(
            name, programmingLanguage="python", extension=".py"
        )
        setattr(cls, testMethod.__name__, testMethod)

    if os.path.exists(f"{name}.cpp"):
        # Create a test method for the class
        testMethod = create_test_method_python(
            name, programmingLanguage="cpp", extension=".cpp"
        )
        setattr(cls, testMethod.__name__, testMethod)


# We find all the folders in the tests folder
folders = os.listdir("tests")

# Add methods to the DynamicTestCase class.
for folderName in folders:
    # Create the class dynamically
    DynamicTestClass = type(folderName, (unittest.TestCase,), {})

    # Add the test methods to the class
    addTests(DynamicTestClass)

    # Add the class to the globals() dictionary so that unittest can find it
    globals()[folderName] = DynamicTestClass
