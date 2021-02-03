import fileinput

with fileinput.input(inplace=True) as f:
    for ip_line in f:
        op_line = ip_line.rstrip('\n').capitalize() + '.'
        print(op_line)

