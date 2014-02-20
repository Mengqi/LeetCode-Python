# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self._depthMap = dict()
    
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True

        depthMap = self._depthMap
        left = root.left
        right = root.right
        if left != None and right != None:
            if self.isBalanced(left) and self.isBalanced(right):
                depthMap[root] = max(depthMap[left], depthMap[right]) + 1
                return abs(depthMap[left] - depthMap[right]) <= 1
            else:
                return False
        elif left != None:
            if self.isBalanced(left):
                depthMap[root] = depthMap[left] + 1
                return  depthMap[left] == 0
            else:
                return False
        elif right != None:
            if self.isBalanced(right):
                depthMap[root] = depthMap[right] + 1
                return depthMap[right] == 0
            else:
                return False
        else:
            depthMap[root] = 0
            return True
