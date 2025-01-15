"""Example code to read file"""

with open('some_file.txt', 'r', encoding='utf-8') as f:
    some_file = f.read()

print(some_file)
