class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f"{str(node.data)} -> "
            node = node.next_node

        ll_string += " None"
        print(ll_string)

    def insert_beginning(self, data):
        new_node = Node(data, self.head)
        if self.head is None:
            self.head = new_node
            self.last_node = self.head
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def to_list(self):
        list_of_nodes = []
        if self.head is None:
            return list_of_nodes

        node = self.head
        while node:
            list_of_nodes.append(node.data)
            node = node.next_node
        return list_of_nodes

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] == int(user_id):
                return node.data
            node = node.next_node
        return None
