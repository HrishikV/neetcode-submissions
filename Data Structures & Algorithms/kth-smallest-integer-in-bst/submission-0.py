# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l=[]
        def traverse(r):
            if not r:
                return
            
            l.append(r.val)

            traverse(r.left)
            traverse(r.right)
        
        traverse(root)
        l.sort()
        return l[k-1]