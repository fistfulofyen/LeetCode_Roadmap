
class node:
    def __init__(self,data=None) -> None:
        self.data = data
        self.next = None

class linked_list:
    def __init__(self) -> None:
        self.head = node()

    def append(self,data):
        new_node = node(data)
        current = self.head
        #finding last node, check if the next node is empty, if not assign current as next node
        while current.next != None:
            current = current.next
        #when current is the last element in the linked list, link new node behind current 
        current.next = new_node

    def length(self):
        length = 0
        current = self.head
        while current.next != None:
            length += 1
            current = current.next

        return length
    
    #display element in linked list
    def display(self):
        element = []
        current = self.head
        while current.next != None:
            current = current.next
            element.append(current.data)
        print(element)

    def get(self,index):
        current_index = 0
        current = self.head
        while current.next != None:
            current = current.next
            if current_index == index:
                return current.data
            
            current_index += 1

    def erase(self,index):
        current_index = 0
        current = self.head
        while current.next != None:
            privous = current
            current = current.next
            if current_index == index:
                privous.next = current.next
            
            current_index += 1

class circularLinkedList:
    def __init__(self) -> None:
        self.head = node()
        self.head.next = self.head

    def is_empty(self):
        return self.head.next is self.head
    
    # def append(self,data):
    #     new_node = node(data)
    #     if self.is_empty():
    #         self.next = new_node
    #         new_node.next = self.head
    #     else:
    #         current_node = self.head.next
    #         while current_node.next != self.head:
    #             current_node = current_node.next

    #         current_node.next = new_node
    #         new_node.next = self.head

    def append(self,data):
        new_node = node(data)
        current = self.head
        #finding last node, check if the next node is empty, if not assign current as next node
        while current.next != self.head:
            current = current.next
        #when current is the last element in the linked list, link new node behind current 
        current.next = new_node
        new_node.next = self.head

    def display(self):
        element = []
        current = self.head
        while current.next != self.head:
            current = current.next
            element.append(current.data)
        print(element)
    


if __name__ == '__main__':
    ll = linked_list()
    for i in range(9):
        ll.append(i)
    
    ll.erase(3)
    ll.display()
    print(ll.get(2))

    print()

    cll = circularLinkedList()
    for i in range(9):
        cll.append(i)
    cll.display()

