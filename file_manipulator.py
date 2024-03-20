import sys

def reverse():
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    with open(input_path, 'r') as file:
        data = file.read()
    with open(output_path, 'w') as file:
        file.write(data[::-1])

def copy():
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    with open(input_path, 'r') as file:
        data = file.read()
    with open(output_path, 'w') as file:
        file.write(data)

def duplicate_contents():
    input_path = sys.argv[2]
    n = int(sys.argv[3])
    with open(input_path, 'r') as file:
        data = file.read()
    with open(input_path, 'w') as file:
        file.write(data * n)

def replace_string():
    input_path = sys.argv[2]
    needle = sys.argv[3]
    new_string = sys.argv[4]
    with open(input_path, 'r') as file:
        data = file.read()
    with open(input_path, 'w') as file:
        file.write(data.replace(needle, new_string))

action = sys.argv[1]

if action == 'reverse':
    reverse()
elif action == 'copy':
    copy()
elif action == 'duplicate':
    duplicate_contents()
elif action == 'replace':
    replace_string()
