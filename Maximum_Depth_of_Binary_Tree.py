# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        level = 0
        if root is None:
            return level

        currQueue = [root]
        nextQueue = []

        while len(currQueue) != 0:
            level += 1
            while len(currQueue) != 0:
                node = currQueue.pop(0)
                if node.left is not None:
                    nextQueue.append(node.left)
                if node.right is not None:
                    nextQueue.append(node.right)

            currQueue, nextQueue = nextQueue, currQueue

        return level
