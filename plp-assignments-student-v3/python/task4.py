# Task 4: File I/O
# Create a text file and then read from it to show basic file operations

def write_sample(path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('This file was created by Hack-Ibrah for PLP file I/O task.\n')
        f.write('It demonstrates writing and reading files.\n')

def read_sample(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    sample = 'sample.txt'
    write_sample(sample)
    print('File contents:\n')
    print(read_sample(sample))
