number = input("enter any number with commas: ")
separators = ''
for char in number:
    if not char.isnumeric():
        separators = separators + char

char.isupper()
print(separators)
values = "".join(char if char not in separators else "  " for char in number).split()
print(sum([int(val) for val in values]))