
with open('data/pi_digits.txt') as file_object:
    contents = file_object.read()
    # read() returns an empty string when it reaches EOF.
    # print(contents)
    print(contents.rstrip())
