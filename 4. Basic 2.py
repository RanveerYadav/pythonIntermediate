# Example 1 to read a file
openFile = open('Basic 2.txt')
readFile = openFile.read()
openFile.close()
print(readFile)

# Example 2, open and reads automatically, no need to close explictly
with open('Basic 2.txt') as file:
    read = file.read()
    print(read)