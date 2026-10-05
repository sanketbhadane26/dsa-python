class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):

    # Both nodes are empty
    if p is None and q is None:
        return True

    # One is empty and the other is not
    if p is None or q is None:
        return False

    # Values are different
    if p.val != q.val:
        return False

    # Check left and right subtrees
    return (
        is_same_tree(p.left, q.left)
        and
        is_same_tree(p.right, q.right)
    )


# Tree 1
tree1 = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3)
)

# Tree 2
tree2 = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3)
)

# Function call
result = is_same_tree(tree1, tree2)

# Output
print("Are the trees same?", result)