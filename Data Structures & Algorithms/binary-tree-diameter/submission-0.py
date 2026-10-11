# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            self.res = max(self.res, left+right)

            return 1 + max(left, right)
        dfs(root)
        return self.res
        
        # if root is None:
        #     return 0
        # leftSide = 0
        # # if root.left is None:
        # #     return 0
        # if root.left is not None:
        #     leftSide += self.diameterOfBinaryTree(root.left)
            

        # rightSide = 0
        # if root.right is not None:
        #     rightSide += self.diameterOfBinaryTree(root.right)
        # print("root val", root.val)
        # print("left", leftSide)
        # print("right", rightSide)
        # res = max(leftSide, rightSide)
        # resFinal = 1 + max(leftSide, rightSide)
        # if resFinal > res:
        #     return resFinal
        # else:
        #     returen res


        