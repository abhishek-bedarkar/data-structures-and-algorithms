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
        print()

    def generate_random_data(self, limit: int):
        # insert data to list
        n = Node(0)
        self.head = n
        self.curr = self.head
        for i in range(1, limit):
            n = Node(i)
            self.curr.next = n
            self.curr = self.curr.next

    def add_node_at_first(self, data: int):
        # Add Node at first
        n = Node(data)
        n.next = self.head
        self.head = n

    def add_node_at_last(self, data: int):
        n = Node(data)
        self.curr = self.head
        while self.curr.next:
            self.curr = self.curr.next
        self.curr.next = n

    def add_node_after(self, after_node: int, data: int) -> bool:
        # Add after data after given node
        self.curr = self.head
        while self.curr.next:
            if self.curr.data == after_node:
                break
            self.curr = self.curr.next
        if self.curr.next is None:
            return False
        else:
            n = Node(data)
            n.next = self.curr.next
            self.curr.next = n
            return True

    def delete_node(self, data: int) -> bool:
        # Delete given node from linked list if present
        self.curr = self.head
        prev = self.head
        while self.curr:
            if self.curr.data == data:
                break
            prev = self.curr
            self.curr = self.curr.next
        if self.curr is None:
            return False
        else:
            if self.curr is prev:
                # first node to be deleted
                self.head = self.curr.next
                return True
            else:
                prev.next = self.curr.next
                return True

    def delete_node_by_position(self, position: int) -> bool:
        self.curr = self.head
        prev = None
        while position != 0:
            if self.curr is None:
                break
            else:
                prev = self.curr
                self.curr = self.curr.next
                position -= 1

        if position == 0:
            if self.curr is prev:
                self.head = self.curr.next
            else:
                prev.next = self.curr.next
            return True
        else:
            return False

    def length_of_linked_list_iterative(self):
        length = 0
        self.curr = self.head
        while self.curr is not None:
            length += 1
            self.curr = self.curr.next
        return length

    def get_count(self, crr: Node):
        if crr is None:
            return 0
        else:
            return 1 + self.get_count(crr.next)

    def length_of_linked_list_recursive(self):
        return self.get_count(self.head)

    def is_present(self, data: int) -> int:
        found_count = 0
        self.curr = self.head
        while self.curr:
            if self.curr.data == data:
                found_count += 1
            self.curr = self.curr.next
        return found_count

    def swap_node(self, src_data: int, des_data: int) -> bool:
        # check if both node present in list and only once
        if self.is_present(src_data) == 0 or self.is_present(src_data) > 1 or (
                self.is_present(des_data) == 0 or self.is_present(des_data) > 1):
            return False
        prev_x = None
        curr_x = None
        self.curr = self.head
        while self.curr is not None or self.curr.data != src_data:
            prev_x = self.curr
            curr_x = self.curr.next
            self.curr = self.curr.next

        prev_y = None
        curr_y = None
        self.curr = self.head
        while self.curr is not None or self.curr.next != des_data:
            prev_y = self.curr
            curr_y = self.curr.next
            self.curr = self.curr.next

        # if x is not head of list
        if prev_x is not None:
            prev_x.next = curr_y
        else:
            self.head = curr_y

        # if y is not head of list
        if prev_y is not None:
            prev_y.next = curr_x
        else:
            self.head = curr_x

        # Swap next pointers

        temp = curr_x.next
        curr_x.next = curr_y.next
        curr_y.next = temp

        return True


if __name__ == '__main__':
    l = LinkedList()
    l.generate_random_data(10)
    l.print_linked_list()

    l.add_node_at_first(-1)
    l.add_node_at_last(11)
    l.add_node_after(9, 10)
    l.print_linked_list()

    l.delete_node(2)
    l.delete_node(11)
    l.delete_node(-1)
    l.delete_node_by_position(1)
    l.print_linked_list()

    print(l.length_of_linked_list_iterative())
    print(l.length_of_linked_list_recursive())
