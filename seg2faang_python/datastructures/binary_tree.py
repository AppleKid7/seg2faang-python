class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class NodeBasedBinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, val):
        pass

    def find(self, val):
        pass

    def delete(self, val):
        pass


class SimpleBinarySearchTree:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if val <= self.val:
            if self.left is None:
                self.left = SimpleBinarySearchTree(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = SimpleBinarySearchTree(val)
            else:
                self.right.insert(val)
    
    def find(self, val):
        if self.val == val:
            return self
        if val <= self.left:
            if self.left is None:
                return False
            return self.left.find(val)
        else:
            if self.rigth is None:
                return False
            return self.right.find(val)


    def delete(self, val):
        prev, curr = None, self
        # find the node
        while curr and curr.val != val:
            prev = curr
            curr = curr.left if val < curr.val else curr.right
        # check if the node exists
        if curr is None:
            return None

        if curr.left is None and curr.right is None:
            if prev and prev.left and prev.left.val == curr:
                prev.left = None
            else:
                prev.right = None
        elif curr.left is None or curr.right is None:
            self._delete_helper_for_node_with_one_child(prev, curr)
        else:
            temp = curr.right.minimum()
            curr.delete(temp.val)
            curr.val = temp.val

    def _delete_helper_for_node_with_one_child(self, prev, curr):
        # curr is left child of prev
        if prev.left and prev.left.val == curr.val:
            if curr.left is None:
                temp = curr.right
                prev.left = temp
                curr.right = None
            elif curr.right is None:
                temp = curr.left
                prev.left = None
            else:
                pass
        else:
            if curr.left is None:
                temp = curr.right
                prev.right = temp
                curr.right = None
            elif curr.right is None:
                temp = curr.left
                prev.right = temp
            else:
                pass

    def minimum(self):
        node = self
        while node.left is not None:
            node = node.left
        return node

    def __str__(self):
        ret = ''
        if self.left is not None:
            ret += str(self.left)

        ret += ' ' + str(self.val)
        if self.right is not None:
            ret += str(self.right)
        return ret

    def delete2(self, val):
        prev, curr = None, self
        while curr and curr.val != val:
            prev = curr
            curr = curr.left if val < curr.val else curr.right

        if curr is None:
            return None

        if curr.left is None and curr.right is None:
            if prev and prev.left and prev.left.val == curr.val:
                prev.left = None
            else:
                prev.right = None
        elif curr.left is None or curr.right is None:
            self._delete_helper_for_node_with_one_child2()
        else:
            temp = curr.right.minimum()
            curr.delete(temp.val)
            curr.val = temp.val

    def _delete_helper_for_node_with_one_child2(self, prev, curr):
        if prev.left and prev.left.val == curr.val:
            if curr.left is None:
                temp = curr.right
                prev.left = temp
                curr.right = None
            elif curr.right is None:
                temp = curr.left
                prev.left = temp
                curr.left = None
            else:
                pass
        else:
            if curr.left is None:
                temp = curr.right
                prev.right = temp
                curr.right = None
            elif curr.right is None:
                temp = curr.left
                prev.right = temp
                curr.left = None
            else:
                pass


def main():
    pass


if __name__ == '__main__':
    main()