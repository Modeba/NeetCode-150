def diameterOfBinaryTree(root):
    diameter = 0
    def dfs(root):
        nonlocal diameter
        if not root:
            return 0
        left_depth = dfs(root.left)
        right_depth = dfs(root.right)
        diameter = max(diameter, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)
    
    dfs(root)
    return diameter