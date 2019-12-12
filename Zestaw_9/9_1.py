class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class List:

    def __init__(self):
        self.head = Node(None, None)
        self.tail = self.head

    def __str__(self):
        list = ""
        node = self.head.next

        while node is not None:
            list += str(node.data) + " "
            node = node.next

        return list

    def add(self, value):
        if self.head.next is None:
            self.tail = Node(value, None)
            self.head.next = self.tail
        else:
            new_node = Node(value, None)
            self.tail.next = new_node
            self.tail = new_node

    def remove_tail(self):
        if self.head.next is None:
            raise ValueError('Cannot removed element from empty list')

        node = self.head.next
        previous = Node(None, None)

        while node.next is not None:
            previous = node
            node = node.next

        previous.next = None
        self.tail = previous
        removed_node = node
        node = None

        return removed_node

    def merge(self, other):
        other_node_element = other.head.next
        if other_node_element is None:
            return
        else:
            while other_node_element.next is not None:
                self.add(other_node_element)
                other_node_element = other_node_element.next

            self.add(other_node_element)
            self.tail = other_node_element

    def clear(self):
        self.head = Node(None, None)
        self.tail = self.head

    
    
    
# TEST
#
# list1 = List()
#
# list1.add(1)
# list1.add(2)
# list1.add(3)
# list1.add(4)
#
# list2 = List()
# 
# list2.add(5)
# list2.add(6)
# list2.add(7)
#
# list1.merge(list2)
# list1.remove_tail()
#
# print(list1)
