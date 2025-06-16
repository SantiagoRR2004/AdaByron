import subprocess
import os


def run_script_python(script_name: str, input_data: str) -> tuple:
    """
    Run a python script and return the output and error.

    Args:
        - script_name (str): the name of the script to run
        - input_data (str): the input to the script

    Returns:
        - tuple: the output and error of the script
    """
    process = subprocess.Popen(
        ["python3", script_name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,  # Ensures the inputs and outputs are treated as strings
    )
    output, error = process.communicate(input=input_data)
    return output, error


def run_script_cpp(source_file: str, input_data: str) -> tuple:
    """
    Compiles a C++ source file and runs the resulting binary.

    Args:
        - source_file (str): Path to the C++ source file (e.g., "main.cpp").
        - input_data (str): Input data to pass to the executable.

    Returns:
        - tuple: (stdout, stderr) from running the compiled program.
    """
    # Derive binary name from source file (strip extension)
    output_binary = os.path.splitext(source_file)[0]

    # Compile the C++ file
    compile_process = subprocess.run(
        ["g++", source_file, "-o", output_binary],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Check if compilation failed
    if compile_process.returncode != 0:
        return "", f"Compilation failed:\n{compile_process.stderr}"

    # Run the compiled binary
    run_process = subprocess.Popen(
        [f"./{output_binary}"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    output, error = run_process.communicate(input=input_data)

    # Delete the binary after running
    os.remove(output_binary)

    return output, error
