class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):

    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


# Input
root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3)
)

# Function call
result = max_depth(root)

# Output
print("Maximum Depth:", result)