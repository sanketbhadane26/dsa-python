class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):

    if root is None:
        return None

    # Swap left and right
    root.left, root.right = root.right, root.left

    # Invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root


def print_tree(root):

    if root is None:
        return

    print(root.val, end=" ")
    print_tree(root.left)
    print_tree(root.right)


# Input tree
root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3)
)

print("Before inversion:")
print_tree(root)

# Function call
invert_tree(root)

print("\nAfter inversion:")
print_tree(root)