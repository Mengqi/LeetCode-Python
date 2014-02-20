# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        currNode = head

        while currNode != None:
            nextNode = currNode.next
            if nextNode != None and nextNode.val == currNode.val:
                currNode.next = nextNode.next
            else:
                currNode = currNode.next

        return head
