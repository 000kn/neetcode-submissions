# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        first = head

        prev, curr = None, second
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp

        while prev:
            tmp1, tmp2 = first.next, prev.next
            first.next = prev
            prev.next = tmp1
            first = tmp1
            prev = tmp2