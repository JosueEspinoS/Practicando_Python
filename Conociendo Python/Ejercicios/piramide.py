def pyra(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))
pyra(6)
print('\n')
def pyraR(r):
    for x in reversed(range(r)):
        print(' '*(r-x-1)+'*'*(2*x+1))
pyraR(6)