from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()

pi_string = ''
lines = contents = contents.splitlines()
for line in lines:
    pi_string += line.strip()

birthdate = input("Enter your birthdate (dd/mm/yyyy): ")
if birthdate in pi_string:
    print("Your birthdate appears in the first million digits of PI!")
else:
    print("Your birthdate does not appear in the first million digits of PI.")