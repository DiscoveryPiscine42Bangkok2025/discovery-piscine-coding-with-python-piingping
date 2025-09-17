import sys 

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
        return
        
    print(f"parameters: {len(args)}")
    for ar in args:
        print(f"{ar}: {len(ar)}")
        
if __name__ == "__main__":
    main()