with open('ip.txt', mode='r', encoding='ascii') as f:
    for ip_line in f:
        op_line = ip_line.rstrip('\n').capitalize() + '.'
        print(op_line)

