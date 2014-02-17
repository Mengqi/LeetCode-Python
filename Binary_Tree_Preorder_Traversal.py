# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        traversalList = []
        if root is None:
            return traversalList

        traversalList.append(root.val)

        leftTraversal = self.preorderTraversal(root.left)
        traversalList.extend(leftTraversal)

        rightTraversal = self.preorderTraversal(root.right)
        traversalList.extend(rightTraversal)

        return traversalList
