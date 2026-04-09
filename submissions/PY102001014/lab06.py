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

def schedule_next_job(jobs, new_job):
    # 1. Add the new job to the end of the list
    jobs.append(new_job)
    
    # 2. Identify the index of the newly added job
    current_idx = len(jobs) - 1
    
    # 3. Move it upward as needed
    while current_idx > 0:
        # Calculate the index of the parent node
        parent_idx = (current_idx - 1) // 2
        
        # If the new job is smaller than its parent, swap them
        if jobs[current_idx] < jobs[parent_idx]:
            jobs[current_idx], jobs[parent_idx] = jobs[parent_idx], jobs[current_idx]
            
            # Update the current index to the parent's position to keep climbing
            current_idx = parent_idx
        else:
            # The heap property is restored; we can stop
            break
            
    return jobs

# ------------------------------------------------------------
# Q2 — process_next_job
# ------------------------------------------------------------
# A system processes jobs based on priority score
# (smaller value = higher priority).
#
# The job with the highest priority is always processed first.
#
# Given the current job list (arr), remove and return the
# next job to process.
#
# After removal, reorganize the list to maintain the
# priority rule.
#
# IMPORTANT:
# - You may use the provided helper functions to adjust the structure.
# - Do NOT implement any additional helper functions.
#
# ------------------------------------------------------------

def process_next_job(arr):
    if not arr:
        return None

    # 1. The highest priority job is always at the root (index 0)
    highest_priority_job = arr[0]

    # 2. Move the last element to the root and remove the last index
    last_job = arr.pop()
    
    # If there are still jobs left, place the last job at the root and reorganize
    if arr:
        arr[0] = last_job
        
        # 3. Reorganize the list (Heapify Down)
        current_idx = 0
        while True:
            left_child_idx = 2 * current_idx + 1
            right_child_idx = 2 * current_idx + 2
            smallest = current_idx
            
            # Check if left child exists and is smaller than current smallest
            if left_child_idx < len(arr) and arr[left_child_idx] < arr[smallest]:
                smallest = left_child_idx
            
            # Check if right child exists and is smaller than current smallest
            if right_child_idx < len(arr) and arr[right_child_idx] < arr[smallest]:
                smallest = right_child_idx
            
            # If the smallest is no longer the current index, swap and continue
            if smallest != current_idx:
                arr[current_idx], arr[smallest] = arr[smallest], arr[current_idx]
                current_idx = smallest
            else:
                # Priority rule is restored
                break
                
    return highest_priority_job

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
    # 1. Assigning weights (Smaller = Higher Priority)
    # health and security are the foundation of my operation.
    priority_q = [
        (3, "education"),
        (2, "family"),
        (1, "health"),
        (4, "friends"),
        (5, "money")
    ]
    
    # 2. Insert new category "security"
    new_item = (1, "security")
    priority_q.append(new_item)

    # 3. Maintain the structure (Heapify Up logic)
    # We move the new item up until the priority rule is satisfied.
    current_idx = len(priority_q) - 1
    
    while current_idx > 0:
        parent_idx = (current_idx - 1) // 2
        
        # Compare weights (index 0 of the tuple)
        if priority_q[current_idx][0] < priority_q[parent_idx][0]:
            # Swap tuples to bring higher priority to the top
            priority_q[current_idx], priority_q[parent_idx] = \
                priority_q[parent_idx], priority_q[current_idx]
            current_idx = parent_idx
        else:
            # Structure is maintained
            break

    return priority_q

