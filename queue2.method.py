'''
here is, i'm adding the element from the left side to list and 
removing the element from the the right side. (Left-Right)
'''

queue = []

def enqueue():
    if len(queue) == limit:
        print("queue is full !!")
    else:
        element = int(input("enter the element = "))
        queue.insert(0,element)
        print(element, 'is added to the queue')

def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e = queue.pop()
        print("remove element:", e)

def display():
    print(queue)

limit = int(input("how many itmes you want to add in queue: "))
while True:
    print("select the operation 1.add 2.remove 3.show 4.quit")
    choice = int(input("enter your choice: "))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("select correct choice")


'''
#output

how many itmes you want to add in queue: 3
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 1
enter the element = 12
12 is added to the queue
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 1
enter the element = 13
13 is added to the queue
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 1
enter the element = 14
14 is added to the queue
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 1
queue is full !!
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 3
[14, 13, 12]
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 2
remove element: 12
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 3
[14, 13]
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 2
remove element: 13
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 3
[14]
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 4

'''