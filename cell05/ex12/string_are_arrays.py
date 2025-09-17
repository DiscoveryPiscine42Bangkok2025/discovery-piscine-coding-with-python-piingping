import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return
    
    arg = sys.argv[1]
    count = 0

    for i in arg:
        if i == 'z':
            print('z',end='')
            count +=1
    
    if count ==  0:
        print("none")
    else:
        print()

if __name__ == "__main__":
    main()
            