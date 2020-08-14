class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev = None):
        if self.head == None:
            return None
        if node.get_next() == None:
            self.head = node
            return
        self.reverse_list(node.get_next())
        current = node.get_next()
        current.set_next(node)
        node.set_next(None) 
        
        #! None doesn't need to reversed as it should still be the tail, only the nodes get reversed
        #? 1->2->3->None becomes
        #? 3->2->1->None