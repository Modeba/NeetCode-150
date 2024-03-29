class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

root5 = TreeNode(5, None, None)
root4 = TreeNode(4, None, None)
root3 = TreeNode(3, None, None)
root2 = TreeNode(2, root4, root5)
root1 = TreeNode(1, root2, root3)

solution = Solution
print(solution.maxDepth(root1))