"""
rb stands for read-binary.
Used to read/write other files like images mp3, videos etc.
"""

try:
    file = open("image.jpg", 'rb')
except IOError:
    print("File does not exist")

file_contents = file.read()

copy = open("img_copy.jpg", 'ab')
copy.write(file_contents)
copy.close()
