from typing import Optional, List

# -------------------------
# Tree Node
# -------------------------
class TreeNode:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# -------------------------
# Helper functions
# -------------------------
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)

def print_all_nodes(root: TreeNode | None):
    if root is None:
        return
    for value in inorder(root):
        print(value)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

# -------------------------
# Q1 — sorted_array_to_bst
# -------------------------
def _build(nums: List[int], left: int, right: int):
    if left > right:
        return None
    mid = (left + right) // 2
    root = TreeNode(nums[mid])
    root.left = _build(nums, left, mid - 1)
    root.right = _build(nums, mid + 1, right)
    return root

def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    return _build(nums, 0, len(nums) - 1)

# -------------------------
# Q2 — insert_bst
# -------------------------
def insert_bst(root: Optional[TreeNode], value: int):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    elif value > root.value:
        root.right = insert_bst(root.right, value)
    return root

# -------------------------
# Q3 — build_class_bst
# -------------------------
def build_class_bst():
    # Step 1: create student ID list
    init_id = 1035
    num_stus = 6
    nums = [init_id + k for k in range(num_stus)]
    
    # Step 2: build balanced BST
    root = sorted_array_to_bst(nums)
    
    # Step 3: insert extra out-of-order IDs
    root = insert_bst(root, 1043)  # example
    
    # Step 4: print all nodes (in-order)
    print("BST Nodes (Inorder Traversal):")
    print_all_nodes(root)
    
    # Step 5: print max iterations to search
    print("Max possible iteration to search a student ID:", height(root))

# -------------------------
# Run the homework function
# -------------------------
build_class_bst()