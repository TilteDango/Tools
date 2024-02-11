import argparse
import pyfiglet
import os

parser = argparse.ArgumentParser(
    description='Tool for bypassing login restrictions by combining a valid username and password to evade systems that detect consecutive invalid login attempts.',
    usage='%(prog)s -u VALID_USERNAME -p VALID_PASSWORD -U USERFILE -P PASSFILE'
)

print(pyfiglet.figlet_format('TilteDango'))
parser.add_argument('-u', '--valid_username', help='The valid username used to perform a successful login. This username will be combined with other possible usernames for testing.', required=True)
parser.add_argument('-p', '--valid_password', help='The valid password used to perform a successful login. This password will be combined with other possible passwords for testing.', required=True)
parser.add_argument('-U', '--userfile', help='A file containing a list of possible usernames to be tested during the brute-force attack. Each line in the file represents a potential username.', required=True)
parser.add_argument('-P', '--passfile', help='A file containing a list of possible passwords to be tested during the brute-force attack. Each line in the file represents a potential password.', required=True)
args = parser.parse_args()


def read_names_from_file(archivo):
    with open(archivo, 'r') as file:
        names = file.read().splitlines()
    return names

valid_name = args.valid_username
valid_pass = args.valid_password
brute_users = args.userfile
brute_pass = args.passfile

if args.userfile.endswith('.txt'):
    file_name = read_names_from_file(args.userfile)
    if file_name:
        brute_users = file_name
else:
    brute_users = args.userfile

if args.passfile.endswith('.txt'):
    file_name = read_names_from_file(args.passfile)
    if file_name:
        brute_pass = file_name
else:
    brute_pass = args.passfile

subfolder_name = 'OutputBruteFiles'
os.makedirs(subfolder_name, exist_ok=True)

user_brute_file_path = os.path.join(subfolder_name, "userFile.txt")
pass_brute_file_path = os.path.join(subfolder_name, "passFile.txt")

user_brute_file = open(user_brute_file_path, "w")
pass_brute_file = open(pass_brute_file_path, "w")

for i in range(len(brute_pass)):
    pass_brute_file.write(f"{valid_pass}\n{brute_pass[i]}\n")

    user_index = i % len(brute_users)
    user_brute_file.write(f"{valid_name}\n{brute_users[user_index]}\n")

pass_brute_file.close()
user_brute_file.close()

print(f"✔ Brute user file saved in '{user_brute_file_path}'.")
print(f"✔ Brute password file saved in '{pass_brute_file_path}'.")

