# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        head = None
        prev = None
        while l1 != None and l2 != None:
            node = None
            if l1.val < l2.val:
                node = l1
                l1 = l1.next
                node.next = None
            else:
                node = l2
                l2 = l2.next
                node.next = None
            
            if head == None:
                head = node
                prev = node
            else:
                prev.next = node
                prev = node

        while l1 != None:
            node = l1
            l1 = l1.next
            node.next = None

            if head == None:
                head = node
                prev = node
            else:
                prev.next = node
                prev = node

        while l2 != None:
            node = l2
            l2 = l2.next
            node.next = None

            if head == None:
                head = node
                prev = node
            else:
                prev.next = node
                prev = node

        return head
