class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):

    if root is None:
        return True

    def mirror(left, right):

        # Both empty
        if left is None and right is None:
            return True

        # One empty
        if left is None or right is None:
            return False

        # Values must match
        if left.val != right.val:
            return False

        # Cross comparison
        return (
            mirror(left.left, right.right)
            and
            mirror(left.right, right.left)
        )

    return mirror(root.left, root.right)


# Input
root = TreeNode(
    1,
    TreeNode(
        2,
        TreeNode(3),
        TreeNode(4)
    ),
    TreeNode(
        2,
        TreeNode(4),
        TreeNode(3)
    )
)

# Function call
result = is_symmetric(root)

# Output
print("Is the tree symmetric?", result)