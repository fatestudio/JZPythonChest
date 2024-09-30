import heapq

# Initial list of tasks (priority, task name)
tasks = [
    (3, "Write code"),
    (1, "Respond to emails"),
    (2, "Prepare for meeting"),
    (5, "Take a break"),
    (4, "Review code"),
]

# 1. heapify: Convert the list into a heap in-place
# Transform list x into a heap, in-place, in linear time.       default is
# min-heap
heapq.heapify(tasks)
print(f"Initial heapified tasks: {tasks}")

# 2. heappush: Add a new task to the heap
heapq.heappush(tasks, (2, "Finish documentation"))
print(f"Heap after adding a task: {tasks}")

# 3. heappop: Remove and return the smallest priority task
next_task = heapq.heappop(tasks)
print(f"Task with highest priority to process next: {next_task}")
print(f"Heap after removing the highest priority task: {tasks}")

# 4. heappushpop: Push a new task and pop the smallest one in a single
# operation
replaced_task = heapq.heappushpop(tasks, (3, "Attend conference call"))
print(f"Task added and then removed in pushpop: {replaced_task}")
print(f"Heap after pushpop operation: {tasks}")

# 5. heapreplace: Pop the smallest item and then add a new task
replaced_task = heapq.heapreplace(tasks, (1, "Schedule appointment"))
print(f"Task replaced using heapreplace: {replaced_task}")
print(f"Heap after heapreplace operation: {tasks}")

# 6. nsmallest: Retrieve the 3 tasks with the highest priority
top_tasks = heapq.nsmallest(3, tasks)  # it is O(N log N), which re-heapify the
print(f"Top 3 tasks with highest priority: {top_tasks}")
print(f"Heap after nsmallest operation: {tasks}")

# 7. nlargest: Retrieve the 2 tasks with the lowest priority
lowest_priority_tasks = heapq.nlargest(
    2, tasks)  # it requires O(n) extra space for an internal heap
print(f"Top 2 tasks with lowest priority: {lowest_priority_tasks}")
print(f"Heap after nlargest operation: {tasks}")
