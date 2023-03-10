# PROBLEM-1 STACK

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack.peek())  # Output: 3

my_stack.pop()

print(my_stack.peek())  # Output: 2

print(my_stack.is_empty())  # Output: False

my_stack.pop()
my_stack.pop()
my_stack.pop()

print(my_stack.is_empty())  # Output: True


# PROBLEM-2 QUEUE

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print(my_queue.peek())  # Output: 1

my_queue.dequeue()

print(my_queue.peek())  # Output: 2

print(my_queue.is_empty())  # Output: False

my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()

print(my_queue.is_empty())  # Output: True


# PROBLEM-3 BINARY SEARCH TREE

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.count += 1
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
                self.count += 1
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
                self.count += 1
            else:
                self._insert(data, current_node.right)
        else:
            # value is already in tree
            pass

    def search(self, data):
        if self.root is not None:
            return self._search(data, self.root)
        else:
            return False

    def _search(self, data, current_node):
        if data == current_node.data:
            return True
        elif data < current_node.data and current_node.left is not None:
            return self._search(data, current_node.left)
        elif data > current_node.data and current_node.right is not None:
            return self._search(data, current_node.right)
        else:
            return False

    def size(self):
        return self.count

    def delete(self, data):
        if self.root is not None:
            self.count -= 1
            return self._delete(data, self.root)

    def _delete(self, data, current_node):
        if data == current_node.data:
            # Node is leaf
            if current_node.left is None and current_node.right is None:
                return None

            # Node has one child
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Node has two children
            min_node = self._find_min_node(current_node.right)
            current_node.data = min_node.data
            current_node.right = self._delete(min_node.data, current_node.right)
            return current_node
        elif data < current_node.data:
            current_node.left = self._delete(data, current_node.left)
            return current_node
        else:
            current_node.right = self._delete(data, current_node.right)
            return current_node

    def _find_min_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


my_bst = BST()

my_bst.insert(5)
my_bst.insert(3)
my_bst.insert(7)
my_bst.insert(1)

print(my_bst.search(7))  # Output: True
print(my_bst.search(2))  # Output: False
print(my_bst.size())  # Output: 4

my_bst.delete(3)

print(my_bst.size())  # Output: 3
