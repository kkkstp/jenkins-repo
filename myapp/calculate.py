import sys

def plus(a, b):
    return a+b

def minus(a, b):
    return a-b

if __name__ == "__main__":
    a = 5
    b = 2
    print(a, b)
    print(f'plus result: {plus(a, b)}')
    print(f'minus result: {minus(a, b)}')
