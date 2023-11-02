#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_index = 1
    total = 0
    while (argv_index != len(sys.argv)):
        total += int(sys.argv[argv_index])
        argv_index += 1
    print(f'{total}')
