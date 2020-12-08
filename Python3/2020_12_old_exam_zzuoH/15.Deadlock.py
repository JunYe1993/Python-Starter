# Question
# Please describe the deadlock.

# Answer
# Deadlock is a situation in which two programs sharing the same resource are effectively 
# preventing each other from accessing the resource, resulting in both programs ceasing to function.

# Mutual exclusion - Each resource is either currently allocated to exactly one process or it is available. (Two processes cannot simultaneously control the same resource or be in their critical section).
# Hold and Wait - processes currently holding resources can request new resources.
# No preemption - Once a process holds a resource, it cannot be taken away by another process or the kernel.
# Circular wait - Each process is waiting to obtain a resource which is held by another process