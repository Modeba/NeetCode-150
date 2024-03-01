def maxDepth(self, root: Treenode) -> int:
    if not root:
        return 0
    
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))