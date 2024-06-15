import subprocess


def run_script(script_name: str, input_data: str) -> tuple:
    """
    Run a script and return the output and error.

    Args:
        script_name (str): the name of the script to run
        input_data (str): the input to the script

    Returns:
        tuple: the output and error of the script"""
    process = subprocess.Popen(
        ["python3", script_name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,  # Ensures the inputs and outputs are treated as strings
    )
    output, error = process.communicate(input=input_data)
    return output, error
