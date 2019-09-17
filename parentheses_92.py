from stack_92 import Stack
import sys

def matcher(line):
    l = Stack()
    lefties, righties = "({[", ")}]"
    pairs = ["{}", "()", "[]"]
    for c in line:
        if c in lefties:
            l.push(c)
        if c in righties:
            if l.is_empty():
                return False
            elif l.pop() + c not in pairs:
                return False
            
    return l.is_empty()

def main():

    for line in sys.stdin:
        print(matcher(line.strip()))

if __name__ == '__main__':
    main()
