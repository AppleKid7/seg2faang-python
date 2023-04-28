
class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def __str__(self):
        acc = ''
        for i in self.items:
            if acc == '':
                acc = str(i)
            else:
                acc = f'{acc}, {str(i)}'
        return acc

def main():
    stack = Stack()
    stack.push(1)
    print(stack)
    stack.push(2)
    print(stack)
    stack.pop()
    print(stack)
    print(stack.peek())


if __name__ == '__main__':
    main()