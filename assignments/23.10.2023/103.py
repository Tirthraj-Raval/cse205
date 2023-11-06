# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = list()
        result = []
        if root is not None:
            q.append(root)
        odd = 0

        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                if not node:
                    continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            
            if level:
                if odd%2 == 0:
                    result.append(level)
                else:
                    result.append(level[::-1])
            odd+=1
            
        return result
