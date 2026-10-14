# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and (abs(left[1]-right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
        # if root is None:
        #     return True

        # leftHeight = 0
        # rightHeight = 0
        # if root.left is not None:
        #     leftHeight += 1
        #     self.isBalanced(root.left)

        # if root.right is not None:
        #     rightHeight += 1
        #     self.isBalanced(root.right)

        # return False if rightHeight == leftHeight else True
        
        