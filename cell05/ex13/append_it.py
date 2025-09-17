import sys 

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
        return
    
    for ar in args:
        if ar.endswith("ism"):
            continue
        print(f'{ar}ism')

if __name__ == "__main__":
    main()