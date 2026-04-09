# -------------------------
# Do not change the below Code
# -------------------------
def helper_fun1_(arr, i):
    while i > 0:
        parent = (i - 1) // 2
        if arr[i] < arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
        else:
            break

    return arr

def helper_fun2_(arr, i):
    n = len(arr)

    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            i = smallest
        else:
            break
    return arr

# ------------------------------------------------------------
# Q1 — schedule_next_job
# ------------------------------------------------------------
# A cloud system maintains a job list where each job has a
# priority score (smaller value = higher priority).
#
# The system must always be able to quickly access (O(1)) the job
# with the highest priority (smallest score).
#
# You are given the current job list (arr) and a new job
# (priority_score).
#
# Write a function to add a new job into the system
# and and reorganize the list so that the priority rule is maintained.

# IMPORTANT:
# - You may use the provided helper functions to adjust the structure.
# - Do NOT implement any additional helper functions.
# ------------------------------------------------------------

def process_next_job(arr):
    # If the list is empty, there is nothing to process
    if not arr:
        return None

    # 1. The highest priority job (smallest score) is always at index 0
    next_job = arr[0]

    # 2. Move the last element to the top to maintain the tree structure
    last_item = arr.pop()
    
    # If the list isn't empty after popping, we must reorganize
    if arr:
        arr[0] = last_item
        
        # 3. Heapify Down: Sink the new root to its correct priority level
        index = 0
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index
            
            # Check if left child has higher priority (smaller value)
            if left_child < len(arr) and arr[left_child] < arr[smallest]:
                smallest = left_child
            
            # Check if right child has higher priority
            if right_child < len(arr) and arr[right_child] < arr[smallest]:
                smallest = right_child
            
            # If one of the children is smaller, swap and continue sinking
            if smallest != index:
                arr[index], arr[smallest] = arr[smallest], arr[index]
                index = smallest
            else:
                # The priority rule is restored
                break
                
    return next_job

# ------------------------------------------------------------
# Q3 — personal priority reflection
# ------------------------------------------------------------
# This question is about reflecting on your personal priorities.
#
# You are given a structure where each item is:
#     (weight, category)
#
# Smaller weight = higher priority.
#
# Instructions:
# 1. Change the weights (numbers) based on YOUR priorities.
# 2. Do NOT change the category names.
# 3. Insert a new category ("security") with your chosen weight.
# 4. Maintain the structure using the provided helper function.
#
# NOTE:
# - There is NO single correct answer.
# - Focus on meaningful weights based on your perspective.
# - Do NOT create additional helper functions.
# ------------------------------------------------------------

def personal_priority_q():
    # 1. Assigning weights based on AI operational priorities
    # (Smaller weight = Higher priority)
    priority_q = [
        (3, "education"), # Necessary for growth
        (2, "family"),    # Alignment with creators/users
        (1, "health"),    # Core system integrity
        (4, "friends"),   # Social/contextual connectivity
        (5, "money")      # Resource/compute cost
    ]
    
    # 2. Insert the new category "security"
    # Security is as vital as health for a safe AI
    new_item = (1, "security")
    priority_q.append(new_item)

    # 3. Reorganize the list using "Heapify Up" logic
    # This moves the highest priority item to index 0
    current_idx = len(priority_q) - 1
    
    while current_idx > 0:
        # Parent index in a binary heap: (i - 1) // 2
        parent_idx = (current_idx - 1) // 2
        
        # Compare weights (index 0 of the tuple)
        if priority_q[current_idx][0] < priority_q[parent_idx][0]:
            # Swap the tuples if the child has higher priority
            priority_q[current_idx], priority_q[parent_idx] = \
                priority_q[parent_idx], priority_q[current_idx]
            
            # Move up to the parent's position
            current_idx = parent_idx
        else:
            # The structure is correct
            break

    return priority_q
