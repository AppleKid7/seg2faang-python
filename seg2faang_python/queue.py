
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        to_enqueue = ListNode(value)
        if self.head is None:
            self.head = to_enqueue
            self.tail = to_enqueue
            return
        self.tail.next = to_enqueue
        self.tail = to_enqueue

    def dequeue(self):
        if self.head is None:
            return None
        to_ret = self.head.value

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return to_ret
        
        old_head = self.head
        self.head = old_head.next
        old_head.next = None
        return to_ret

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def __str__(self):
        acc = ''
        cur = self.head
        while cur:
            if acc == '':
                acc = str(cur.value)
            else:
                acc = f'{acc}, {str(cur.value)}'
            cur = cur.next
        return acc

def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(2)
    print(q)
    t = q.dequeue()
    print(q)
    print(f'element: {t}')
    print(f'peek: {q.peek()}')


if __name__ == '__main__':
    main()