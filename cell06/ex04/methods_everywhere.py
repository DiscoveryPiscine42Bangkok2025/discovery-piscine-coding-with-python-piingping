import sys

def shrink(txt):
    return (txt[:8])

def enlarge(txt):
    return (txt + 'Z'*(8-len(txt)))

if len(sys.argv) == 1:
    print('none')
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            print(shrink(arg))
        elif len(arg) < 8:
            print(enlarge(arg))
        else:
            print(arg)

