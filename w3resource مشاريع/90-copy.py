def copy_the_src_code(first, dest):
    with open(first, 'r') as f, open(dest, 'w') as d:
        d.write(f.read())

copy_the_src_code('90-copy.py', 'copy.py')

with open('copy.py', 'r') as fd:
    for line in fd:
        print(line, end='')
