
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, new_data):
        to_insert = ListNode(new_data)
        was_empty = self.head == None and self.tail == None
        to_insert.next = self.head
        if self.head is not None:
            self.head.prev = to_insert
        self.head = to_insert
        if was_empty:
            self.tail = self.head

    def append(self, new_data):
        new_node = ListNode(new_data)
        was_empty = self.head is None and self.tail is None
        new_node.prev = self.tail
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if was_empty:
            self.head = self.tail

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            return

        if prev_node == self.tail:
            self.append(new_data)
            return

        new_node = ListNode(new_data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node


    def delete(self, node_to_delete):
        if node_to_delete is None:
            return

        if node_to_delete == self.head and node_to_delete == self.tail:
            self.head = None
            self.tail = None
            return

        if node_to_delete == self.head:
            self.head = node_to_delete.next

        if node_to_delete == self.tail:
            self.tail = node_to_delete.prev

        if node_to_delete.prev is not None:
            node_to_delete.prev.next = node_to_delete.next

        if node_to_delete.next is not None:
            node_to_delete.next.prev = node_to_delete.prev
    
        node_to_delete.next = None
        node_to_delete.prev = None


    def __str__(self):
        cur = self.head
        acc = ''
        while cur:
            if acc == '':
                acc = str(cur.val)
            else:
                acc = f'{acc}, {str(cur.val)}'
            cur = cur.next
        return acc


def main():
    ll = DoublyLinkedList()
    ll.append(1)
    print(ll)
    ll.prepend(2)
    print(ll)
    ll.insert_after(ll.tail, 3)
    print(ll)
    ll.delete(ll.head.next)
    print(ll)
    ll.delete(ll.head)
    print(ll)
    ll.delete(ll.tail)
    print(ll)

if __name__ == '__main__':
    main()
