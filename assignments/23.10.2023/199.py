# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = list()
        result = []

        if root is not None:
           q.append(root)
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            result.append(node.val)
            q = level
        
        return result
        




        