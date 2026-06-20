'''
    Files are divided into two categories:
    1. Text files: .txt, .docx, .log
    2. Binary files: .mp4, .png, .mov, .jpg
'''

# opening a file. Syntax: open(filename, mode = 'r')
f = open('test.txt', 'r')
file_data = f.read() # we can pass the number of characters we wanna read as argument
print(file_data)
print(type(file_data))  # prints <class: str>
'''
    file opening modes:
         ``r''   Open text file for reading.  The stream is positioned at the beginning of the file.

        ``r+''  Open for reading and writing.  The stream is positioned at the beginning of the file.

        ``w''   Truncate file to zero length or create text file for writing. The stream is positioned at the beginning of the file.

        ``w+''  Open for reading and writing.  The file is created if it does not exist, otherwise it is truncated.  The stream is positioned at the beginning of the file.

        ``a''   Open for writing.  The file is created if it does not exist. The stream is positioned at the end of the file.  Subsequent writes to the file will always end up at the then current end of file,
                irrespective of any intervening fseek(3) or similar.

        ``a+''  Open for reading and writing.  The file is created if it does not exist.  The stream is positioned at the end of the file.  Subsequent writes to the file will always end up at the then current end of file, irrespective of any intervening fseek(3) or similar.
        
        'b': binary
        't': text mode(default)
        '+': open a disk file for updating(reading and writing)
'''
f.close()

# reopening the file, because previously the file pointer was moved to the end of the file
f = open('text.txt')
print(f.readline())  # prints the first line, and move the file pointer to the next line
print(f.readline())  # prints the second line
f.close()



