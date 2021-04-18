class Node:
    def __init__(self, data: int):
        # Node structure
        self.data = data
        self.next = None


class LinkedList:
    curr = None

    def __init__(self):
        self.head = None

    def print_linked_list(self):
        # display list
        self.curr = self.head
        while self.curr:
            print('->', self.curr.data, end='')
            self.curr = self.curr.next

    def generate_random_data(self, limit: int):
        # insert data to list
        n = Node(0)
        self.head = n
        self.curr = self.head
        for i in range(1, limit):
            n = Node(i)
            self.curr.next = n
            self.curr = self.curr.next


if __name__ == '__main__':
    l = LinkedList()
    l.generate_random_data(10)
    l.print_linked_list()
