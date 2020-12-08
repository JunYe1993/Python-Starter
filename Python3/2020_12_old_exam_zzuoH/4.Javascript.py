# Question:
# What is event loop in JavaScript, what is its `nextTick`?

# 1. Ans:
# Event loop usually implemented like a loop which keep process message.
# Each message is processed completely before ant other message is processed.

# 2. Ans:
# When event loop done a operation (finish an element in Call stack), We call it a tick.
# nextTick will be processed right after current operation.
# nextTick allow a callback to run after the call stack has unwound.
