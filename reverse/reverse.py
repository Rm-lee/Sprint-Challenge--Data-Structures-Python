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

    def reverse_list(self, node, prev):
        arr = []
        current_node = self.head
        if self.head:
            while current_node.get_next() is not None:
                current_node = current_node.get_next()
                arr.append(current_node)
        for i in arr:
         self.add_to_head(i.value)
            
        


        # tail = self.head
        # prior_to_tail = None

        # if self.head:
        #     while self.head.get_next() is not None:            
        #         next_node = self.head.get_next()
        #         if next_node.get_next().get_next() == None:
        #             prior_to_tail = next_node.get_next()
        #         tail = next_node.get_next()
        #         return 
        # new_tail = self.head
        # self.head = tail
        # prior_to_tail.set_next(new_tail)

