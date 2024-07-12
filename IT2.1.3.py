import subprocess
import time
def execute_command_in_directory(command, directory):
    try:
        result = subprocess.run(command, cwd=directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print("Error executing command:")
            print(result.stderr.strip())
            return None
    except Exception as e:
        print("Exception occurred:", e)
        return None
    
def parse_output(output):
    packages = []
    lines = output.split('\n')
    for line in lines:
        element = line.split()
        package = element[0].split('/')
        version = element[1].lstrip('v')
        package_vendor = package[0]
        package_name = package[1]
        package_dict = {
            'vendor': package_vendor,
            'name': package_name,
            'version': version
        }
        packages.append(package_dict)
    return packages


directory_path = "/home/user/Desktop/cybersec/conduit-backend-tests"
command = ['composer', 'show', '-i']
output = execute_command_in_directory(command, directory_path)

if output is not None:
    package_list = parse_output(output)
    for package in package_list:

        subprocess.run(["python3", "1.4.Script.py", "a",package["vendor"], package['name'], package['version']]) 
        time.sleep(15)    
else:
    print("Failed to execute the first command or get output.")

