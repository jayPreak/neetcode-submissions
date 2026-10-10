# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxCount = 1
        if root is None:
            return 0
        # print("left", root.left)
        # print("right", root.right)
        if root.left is None and root.right is None:
            return 1
        leftCount = 0
        if root.left is not None:
            leftCount += self.maxDepth(root.left)
        rightCount = 0
        if root.right is not None:
            rightCount += self.maxDepth(root.right)

        print("l c", leftCount)
        print("r c ", rightCount)

        return 1+max(leftCount, rightCount)

        