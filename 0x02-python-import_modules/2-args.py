#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv)
    if (argv_len == 1):
        print("0 arguments.")
    elif (argv_len == 2):
        print(f'1 argument: \n1: {sys.argv[1]}')
    elif (argv_len > 2):
        count = 1
        print(f'{argv_len - 1} arguments:')
        while (count != argv_len):
            print(f'{count}: {sys.argv[count]}')
            count += 1
