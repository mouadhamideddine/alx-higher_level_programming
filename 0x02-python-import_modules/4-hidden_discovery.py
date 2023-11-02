#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for attr in (dir(hidden_4)):
        if attr[0] == '_':
            pass
        else:
            print(attr)
