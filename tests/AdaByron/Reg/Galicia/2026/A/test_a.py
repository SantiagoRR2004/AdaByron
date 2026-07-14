import subprocess
import random
import sys
import os

currentDirectory = os.path.dirname(os.path.abspath(__file__))
repoRoot = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(currentDirectory)))
        )
    )
)

SCRIPT = os.path.join(
    repoRoot, "solutions", "AdaByron", "Reg", "Galicia", "2026", "A", "A.py"
)


def test_a():
    for _ in range(10000):

        n = random.randint(1, 1000)
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)

        minimumC = max(x + 1, n - x) + max(y + 1, n - y) - 1

        C = minimumC + random.randint(0, 1000)

        proc = subprocess.Popen(
            [sys.executable, str(SCRIPT)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        nTries = 5 * n

        proc.stdin.write(f"{n}\n")
        proc.stdin.flush()

        for _ in range(nTries):
            line = proc.stdout.readline().strip()
            control, xGuess, yGuess = line.split()
            assert control in {"?", "!"}, f"Unexpected control character: {control}"

            if control == "?":
                xGuess, yGuess = int(xGuess), int(yGuess)
                temperature = C - abs(x - xGuess) - abs(y - yGuess)
                proc.stdin.write(f"{temperature}\n")
                proc.stdin.flush()

            elif control == "!":
                xGuess, yGuess = int(xGuess), int(yGuess)
                assert (xGuess, yGuess) == (
                    x,
                    y,
                ), f"Expected ({x}, {y}), got ({xGuess}, {yGuess})"
                proc.stdin.close()
                proc.stdout.close()
                proc.stderr.close()
                return

        else:
            proc.stdin.close()
            proc.stdout.close()
            proc.stderr.close()
            raise AssertionError(
                "Exceeded maximum number of tries without finding the correct coordinates"
            )
