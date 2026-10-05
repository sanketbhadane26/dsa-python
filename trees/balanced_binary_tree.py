class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root):

    def height(node):

        if node is None:
            return 0

        left_height = height(node.left)

        if left_height == -1:
            return -1

        right_height = height(node.right)

        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return height(root) != -1


# Input
root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3)
)

# Function call
result = is_balanced(root)

# Output
print("Is the tree balanced?", result)