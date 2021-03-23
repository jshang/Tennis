import fileinput
with fileinput.input(files=('V006.txt'), inplace=1) as f:
    print(f)
    for line in f:
        print(line.replace('new', 'SVE'), end='')