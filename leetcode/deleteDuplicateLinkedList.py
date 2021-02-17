# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        current = head.next
        prev = head

        while current != None:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next
        return head


if __name__ == '__main__':
    ln5 = ListNode(3, None)
    ln4 = ListNode(3, ln5)
    ln3 = ListNode(2, ln4)
    ln2 = ListNode(1, ln3)
    ln1 = ListNode(1, ln2)

    # ln1.next(ln2)
    # ln2.next(ln3)
    # ln3.next(ln4)
    # ln4.next(ln5)

    print(ln5.val)
