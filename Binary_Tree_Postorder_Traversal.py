# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        traversalList = []
        if (root is None):
            return traversalList

        leftTraversal = self.postorderTraversal(root.left)
        traversalList.extend(leftTraversal)

        rightTraversal = self.postorderTraversal(root.right)
        traversalList.extend(rightTraversal)

        traversalList.append(root.val)

        return traversalList
