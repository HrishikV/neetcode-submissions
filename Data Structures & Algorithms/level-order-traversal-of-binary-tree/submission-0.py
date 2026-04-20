# Definition for a binary tree node.
# class TreeNode:
#     def __init__(DefaultDict, self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order=defaultdict(list)
        def dfs(r,depth):
            if r is None:
                return
            order[depth].append(r.val)

            dfs(r.left,depth+1)
            dfs(r.right,depth+1)

        dfs(root,0)
        return list(order.values())