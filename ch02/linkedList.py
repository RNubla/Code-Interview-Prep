class Node:
    def __init__(self, data, next=None):
        self.data = data
        # self.next = None
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def appendToTail(self, data):
        endData = Node(data, None)
        if self.head is None:
            self.head = Node(data, None)
            # self.insertAtBeginning(data)
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = endData

    def deleteNode(self, data):
        current = self.head
        if current is None:
            raise Exception('Invalid data')

        while current.next != None:
            if current.data == data:
                current.next = current.next.next
                # self.head.next = current.next
                break
        current = current.next

    def printLinkedList(self):
        string = ''
        itr = self.head
        while itr:
            string += str(itr.data) + '-->'
            itr = itr.next
        print(string)


if __name__ == '__main__':
    ll = LinkedList()
    ll.appendToTail(2)
    ll.appendToTail(3)
    ll.appendToTail(4)
    ll.printLinkedList()
    ll.deleteNode(3)
    ll.printLinkedList()
