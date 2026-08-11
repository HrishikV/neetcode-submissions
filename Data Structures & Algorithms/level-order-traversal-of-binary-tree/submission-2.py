# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol={}
        def dfs(depth,root):
            if not root:
                return None
            if depth not in sol:
                sol[depth]=[]
            sol[depth].append(root.val)
            dfs(depth+1,root.left)
            dfs(depth+1,root.right)
        dfs(0,root)
        return list(sol.values())
