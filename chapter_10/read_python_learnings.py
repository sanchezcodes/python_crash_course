from pathlib import Path

file = Path("learning_python.txt")
contents = file.read_text()
print(contents, "\n")


for line in contents.splitlines():
    line = line.replace("Python", "C++")
    print(line)