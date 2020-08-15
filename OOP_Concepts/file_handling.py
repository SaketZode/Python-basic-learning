# reading an existing file
"""
By default, file is opened in read-only mode.
While opening file in 'w' mode, the previous content written in file is erased and
a fresh blank file is opened.
"""

try:
    read_file = open("read_file.txt", 'r')
except FileNotFoundError:
    print("File does not exist")

print("reading file....\n")
print(read_file.read())

try:
    read_file.write("writing content to file")
except IOError:
    print("Exception : not allowed to write file")

read_file.close()

# appending content to a file
# if file specified in argument is not present, a new file is created at run-time

try:
    append_file = open("read_file.txt", "a")
except FileNotFoundError:
    print("Exception : File does not exist")

try:
    append_file.write("\nappending content to file")
except IOError as exception:
    print("Exception : ", exception)

append_file.close()

write_file = open("write_file.txt", 'w')
write_file.write("Writing something to file")
write_file.close()

write_file = open("write_file.txt", 'w')
write_file.write("Again writing something")
write_file.close()
