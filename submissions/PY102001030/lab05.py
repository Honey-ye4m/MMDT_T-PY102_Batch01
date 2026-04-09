# -------------------------
# Do not change the below Code
# -------------------------
from typing import Optional, List

class TreeNode:
    def __init__(self, value: int, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)

def print_all_nodes(root: TreeNode|None):
    if root is None:
        return
    for value in inorder(root):
        print(value)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

# ------------------------------------------------------------
# Q1 — sorted_array_to_bst
# ------------------------------------------------------------
# Given a sorted array nums (ascending order),
# build and return a height-balanced BST.
#
# Requirements:
# - Choose the middle element as the root.
# - Use Python integer division:
#       mid = (left + right) // 2
# - Recursively build left and right subtrees.
# ------------------------------------------------------------

def _build(nums: List[int], left: int, right: int):
    # Base case: if the range is invalid, return None
    if left > right:
        return None
    
    # Calculate middle index as per requirements
    mid = (left + right) // 2
    
    # Create the root node for this range
    node = TreeNode(nums[mid])
    
    # Recursively build left and right subtrees
    node.left = _build(nums, left, mid - 1)
    node.right = _build(nums, mid + 1, right)
    
    return node

def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    return _build(nums, 0, len(nums) - 1)

def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
   new_tree_root = _build(nums, 0, len(nums) - 1)
   return new_tree_root

# ------------------------------------------------------------
# Q2 — insert_bst
# ------------------------------------------------------------
# Write a function insert_bst(root, value) that inserts
# a value into a Binary Search Tree (BST).
#
# Requirements:
# - If root is None, create and return a new TreeNode.
# - If value < root.value, insert into the left subtree.
# - If value > root.value, insert into the right subtree.
# - Do NOT allow duplicate values.
# - Return the root of the tree after insertion.
# ------------------------------------------------------------

def insert_bst(root: Optional[TreeNode], value: int):
    # If root is None, create and return a new TreeNode
    if root is None:
        return TreeNode(value)
    
    # If value is less, insert into the left subtree
    if value < root.value:
        root.left = insert_bst(root.left, value)
    # If value is greater, insert into the right subtree
    elif value > root.value:
        root.right = insert_bst(root.right, value)
    
    # Do NOT allow duplicates (if value == root.value, we do nothing)
    return root
# ------------------------------------------------------------
# Q3 — BST in real life application
# ------------------------------------------------------------
# In this course, each student has a PY102 ID (e.g., 1001, 1002, ...).
#
# Task:
# 1) Create a list of consecutive PY102 IDs for your group.
#    Example: if init_id = 1001 and num_stus = 6,
#    then the list should be:
#        [1001, 1002, 1003, 1004, 1005, 1006]
#
# 2) Use your sorted_array_to_bst(nums) function from Q1
#    to build a height-balanced BST from this list.
#
# 3) Then, insert additional out-of-order IDs
#    (if any) using your insert_bst(root, value) function from Q2.
#
# 4) Print all nodes of the final BST using provided function.
#
# 5) Print the max possible iterations to search a student id in your final BST. 
# ------------------------------------------------------------

def build_class_bst():
    init_id = 1001
    num_stus = 6
    nums = [init_id + k for k in range(num_stus)]
    ## 2) Build height-balanced BST from the sorted list
    root = sorted_array_to_bst(nums)
    
    # 3) Insert additional out-of-order IDs
    # Adding some IDs to show the insertion works
    extra_ids = [1000, 1010, 1007, 1009]
    for eid in extra_ids:
        root = insert_bst(root, eid)
    
    # 4) Print all nodes (Inorder traversal)
    print("All IDs in the BST:")
    print_all_nodes(root)
    
    # 5) Max iterations to search (This is equal to the height of the tree)
    # Each level represents one comparison/iteration.
    max_iters = height(root)
    print(f"\nMax possible iterations to search: {max_iters}")

# Execute Q3
if __name__ == "__main__":
    build_class_bst()