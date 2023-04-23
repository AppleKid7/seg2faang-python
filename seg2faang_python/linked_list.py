# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        to_insert = ListNode(value, None)
        if not self.head:
            self.head = to_insert
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(value, None)

    def delete(self, val_to_delete):
        if not self.head:
            return
        curr = self.head
        if curr.value == val_to_delete:
            self.head = curr.next
            curr.next = None
            return

        prev = None
        while curr.next:
            if curr.value == val_to_delete:
                break
            prev = curr
            curr = curr.next

        if curr is None:
            return

        prev.next = curr.next
        curr.next = None
        

    def __str__(self):
        acc = ''
        curr = self.head
        while curr:
            if acc == '':
                acc = str(curr.value)
            else:
                acc = f'{acc}, {curr.value}'
            curr = curr.next
        return acc

def main():
    ll = LinkedList(ListNode(1, None))
    print(ll)
    ll.insert(2)
    print(ll)
    ll.insert(3)
    ll.insert(4)
    print(ll)
    ll.delete(3)
    print(ll)

if __name__ == '__main__':
    main()
