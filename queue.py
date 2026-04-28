queue = []

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue elements:", queue)

front = queue[0]
print("Front element:", front)

queue.pop(0)
print("After dequeue:", queue)
