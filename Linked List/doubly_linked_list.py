class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data, prev):
        # if head == None
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def print(self):
        if self.head == None:
            print('The dll is empty')
            return
        itr = self.head
        dllStr = ''
        while itr:
            dllStr += str(itr.data) + '-->'
            itr = itr.next
        print(dllStr)

    def print_backwards(self):
        if self.head == None:
            print('The dll is empty')
            return
        itr = self.head
        dllStr = ''
        while itr:
            dllStr += str(itr.data) + '-->'
            itr = itr.next
        print(dllStr)

    def print_forward(self):
        if self.head == None:
            print('The dll is empty')
            return
        itr = self.getLastNode()
        dllStr = ''
        while itr:
            dllStr += str(itr.data) + '-->'
            itr = itr.prev
        print(dllStr)

    def getLastNode(self):
        if self.head == None:
            print('Empty List')
            return
        itr = self.head
        while itr.next:
            # self.head = itr
            itr = itr.next

        return itr

    def insertAfter(self, data, newData):
        if self.head == None:
            print('Empty list')
            return
        itr = self.head
        while itr:
            if itr.data == data:
                node = Node(newData, itr.next, itr)
                # [3] [2] [1]
                # assigns node [1]'s prev to node
                if node.next:
                    node.next.prev = node
                # assigns node [2]'s next to node
                itr.next = node
                break
            itr = itr.next

    def remove(self, data):
        if self.head == None:
            print('Empty List')
            return
        itr = self.head
        while itr:
            """ EX: [3] [2] [1]
                    if data = 2
                        if 
             """
            if itr.data == data:
                if itr.prev == None:
                    self.head = itr.next
                else:
                    itr.prev.next = itr.next
                if itr.next == None:
                    self.head = itr.prev
                else:
                    itr.next.prev = itr.prev
                break
            itr = itr.next


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insertAtBeginning(1, None)
    dll.insertAtBeginning(2, None)
    dll.insertAtBeginning(3, None)
    # dll.insertAfter(2, 4)
    # dll.insertAfter(2, 6)
    # dll.print()
    dll.print_backwards()
    dll.remove(2)
    dll.print_backwards()
    # dll.print_forward()
