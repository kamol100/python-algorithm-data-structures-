def queueUsingStack(oprations):
    stack = []
    queue = []
    for item in operations:
        if item[0] == '1':
            stack.append(item[2::])
            queue.insert(0,stack[-1])
        if item == '2':
            queue.pop()
        if item == '3':
            print(queue[-1])
    print(stack)
    print(queue)




operations = ['1 42','2', '1 14','3','1 28', '3', '1 60','1 78','2', '2']
queueUsingStack(operations)