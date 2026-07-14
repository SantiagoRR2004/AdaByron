import subprocess
import random
import os

currentDirectory = os.path.dirname(os.path.abspath(__file__))
files = ["H.py", "H0.py"]


def test(length, values):
    power = max(values)
    response = ""

    while response != "FALLIDA\n":
        input_data = f"{length} {power}\n"
        input_data += " ".join([str(v) for v in values])
        input_data += "\n"

        outputs = set()

        for file in files:
            process = subprocess.Popen(
                ["python3", os.path.join(currentDirectory, file)],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,  # Ensures the inputs and outputs are treated as strings
            )
            output, error = process.communicate(input=input_data)

            outputs.add(output)

        if len(outputs) > 1:
            with open(os.path.join(currentDirectory, "differentAnswers.log"), "a") as f:
                f.write(input_data)
            # We exist immediately
            response = "FALLIDA\n"
        else:
            response = output

        power -= 1


def run_test(nTest: int = 1):
    for _ in range(nTest):
        length = random.randint(1, 20)
        values = [random.randint(1, 50) for _ in range(length)]
        test(length, values)


if __name__ == "__main__":

    for _ in range(10**9):
        run_test()
