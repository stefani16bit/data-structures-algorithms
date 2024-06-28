class LinkedList:
    def __init__(self, head): 
        self.head = head

    def tail(self):
        current_node = self.head

        while True:
            if current_node.next != None:
                current_node = current_node.next

            else:
                break

        return current_node       

    def insert(self, node):
        last_tail = self.tail()
        last_tail.next = node
        node.previous = last_tail

    def insert_at_position(self, position, node):

        depth = 0
        current_node = self.head
        
        while True:
            if depth == position:
                break

            if current_node.next != None:
                current_node = current_node.next
                depth += 1

            else: 
                break

        next_node = current_node.next

        current_node.next = node
        node.next = next_node

        node.previous = current_node
        next_node.previous = node
        
    def print_nodes(self):
        current_node = self.head

        while True:
            if current_node.next != None:
                print(current_node.data)
                current_node = current_node.next

            else:
                break    

        print(current_node.data)
        

class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None
        self.previous = None

def main(): 
    list = LinkedList(Node(1))
    list.insert(Node(2))
    list.insert(Node(3))
    list.insert(Node(4))
    list.insert_at_position(2, Node(6))
    list.print_nodes()

if __name__ == "__main__":
    main()