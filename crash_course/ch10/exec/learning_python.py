
filename = 'data/learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print()

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print()

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
