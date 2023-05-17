class LLString:
    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next

    def __init__(self, s):
        self.head = None
        self.tail = None

        for char in s:
            self.append(char)

    def append(self, new_val):
        new_node = LLString.Node(new_val, None)

        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

        if self.head is None:
            self.head = new_node

    def print(self):
        trav = self.head
        while trav is not None:
            print(trav.val, end='')
            trav = trav.next
        print()

    def to_string(self):
        s = ''
        trav = self.head
        while trav is not None:
            s += trav.val
            trav = trav.next
        return s

    def print_every_other(self):
        trav = self.head
        while trav is not None:
            print(trav.val, end='')

            # If there's no next node,
            # we need to end here.
            if trav.next is None:
                break

            # Advance two nodes forward.
            # trav.next.next might be None,
            # but that will be caught by
            # the while loop test.
            trav = trav.next.next
        print()

    def __char_at(self, i, node):
        if node is None:
            return None
        if i == 0:
            return node.val
        return self.__char_at(i - 1, node.next)

    def char_at(self, i):
        return self.__char_at(i, self.head)

    def concat(self, other_llstring):
        trav = self.head
        prev = None

        while trav is not None:
            prev = trav
            trav = trav.next

        if prev is None:
            self.head = other_llstring.head
        else:
            prev.next = other_llstring.head

    def __reverse(self, node):
        if node is None:
            return None

        reversed_rest = self.__reverse(node.next)
        reversed_rest.next = node
        return node

    def reverse(self):
        self.head = self.__reverse(self.head)

    def __index_of(self, c, node):
        if node is None:
            return -1
        if node.val == c:
            return 0

        index_in_rest = self.__index_of(c, node.next)
        if index_in_rest == -1:
            return -1
        else:
            return index_in_rest + 1

    def index_of(self, c):
        return self.__index_of(c, self.head)
