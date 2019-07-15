# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp1 = even = ListNode(0)
        temp2 = odd = ListNode(0)

        while head != None:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even != None else None

        odd.next = temp1.next
        return temp2.next
            
