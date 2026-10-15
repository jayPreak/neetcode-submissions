# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def isSametree(root, subRoot):
            if root is None:
                if subRoot is None:
                    return True
                else:
                    return False
            
            if subRoot is None:
                return False

            if root.val != subRoot.val:
                return False

            left = isSametree(root.left, subRoot.left)
            right = isSametree(root.right, subRoot.right)

            if left and right:
                return True
            else:
                return False

        if root is None:
            if subRoot is None:
                return True
            else:
                return False
        
        if subRoot is None:
            return False

        same = isSametree(root, subRoot)

        print("root", root.val)
        print("subroot", subRoot.val)
        print("same?", same)


        

        if same:
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)

            if left or right:
                return True

        return False