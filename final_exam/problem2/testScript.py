import os
import subprocess
import re
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))


def read_input_and_expected_output(input_file, output_file):
    with open(input_file, 'r') as f:
        input_val = f.read().strip()

    with open(output_file, 'r') as f:
        expected_output = f.read().strip()

    return input_val, expected_output


def test_rec_function(i, input_val, expected_output):
    python_path = sys.executable
    test_script_path = os.path.join(script_dir, '../solved/test2.py')
    input_val_str = str(input_val) + '\n'
    result = subprocess.run([python_path, test_script_path],
                            input=input_val_str, text=True, capture_output=True)
    actual_output = result.stdout.strip()
    if actual_output != expected_output:
        print(
            f"case{i} X : Test failed\nExpected: {expected_output}\nGot: {actual_output}")
    else:
        print(f"case{i} O : Test passed")


def run_tests():

    inputs_dir = os.path.join(script_dir, 'inputs')
    outputs_dir = os.path.join(script_dir, 'outputs')
    i = 1
    filename = [f for f in os.listdir(inputs_dir) if f.startswith('input_')]

    def extract_number(filename):
        s = re.findall("\d+", filename)
        return int(s[0]) if s else -1

    test_files = sorted([f for f in os.listdir(inputs_dir)
                        if f.startswith('input_')], key=extract_number)

    for test_file in test_files:
        input_file = os.path.join(inputs_dir, test_file)
        output_file = os.path.join(
            outputs_dir, f"output_{test_file.split('_')[1]}")
        input_val, expected_output = read_input_and_expected_output(
            input_file, output_file)
        test_rec_function(i, input_val, expected_output)
        i += 1


run_tests()
