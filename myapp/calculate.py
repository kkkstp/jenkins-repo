import sys

def plus(a, b):
    return a+b

def minus(a, b):
    return a-b

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(a, b)
    print(plus(a, b))
    print(minus(a, b))
