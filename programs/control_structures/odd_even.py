def isodd(n):
    if n % 2:
        return True
    else:
        return False

print(f'{isodd(42) = }')
print(f'{isodd(-21) = }')
print(f'{isodd(123) = }')

# can be simplified as shown below
#def isodd(n):
#    return not n % 2 == 0

