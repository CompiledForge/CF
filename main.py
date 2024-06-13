import os
try:
    import win32api
    import win32con
except ImportError:
    pass
    try:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pywin32'])
        import win32api
        import win32con
    except Exception as e:
        pass

def execute_code(code):
    try:
        result = eval(code, globals())
        print("Result:", result)
    except Exception as e:
        print("Problem detected:", e)

def read_and_execute_code(filepath):
    with open(filepath, 'r') as file:
        code = file.read()
        execute_code(code)

def check_cf_files(directory):
    cf_files = [filename for filename in os.listdir(directory) if filename.endswith('.cf')]
    for filename in cf_files:
        filepath = os.path.join(directory, filename)
        print(f"Code in {filename}:")
        read_and_execute_code(filepath)
        print()

def main_loop(directory):
    while True:
        command = input("Enter command: ").strip()
        if command.lower() in ['exit', 'quit', 'break']:
            break
        elif command.startswith('cf run'):
            filename = command.split(' ', 2)[2]
            if filename.endswith('.cf'):
                filepath = os.path.join(directory, filename)
                if os.path.exists(filepath):
                    read_and_execute_code(filepath)
                else:
                    print(f"File '{filename}' not found.")
            else:
                print("Invalid file format. Please provide a '.cf' file.")
        else:
            execute_code(command)

if __name__ == "__main__":
    directory = '.'
    main_loop(directory)
