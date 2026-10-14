# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            if q is None:
                return True
            else:
                return False
        
        if q is None:
            if p is None:
                return True
            else:
                return False


        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        if left and right:
            return True
        else:
            return False
        # def isSame(root1, root2):
            
            
        #     if root1.val != root2.val:
        #         return False

        #     isSame(root1.left, root2.left)
        #     isSame(root2.right, root2.right)

        #     return True

        # isSame(p, q)

        return False

        