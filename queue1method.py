'''
here is, i'm adding the element from the right side to list and 
removing the element from the the left side. (Right-Left)
'''

queue = []

def enqueue():
    if len(queue) == limit:
        print("queue is full !!")
    else:
        element = int(input("enter the element = "))
        queue.append(element)
        print(element, 'is added to the queue')

def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e = queue.pop(0)
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

        
        
        
        
#output
'''
how many itmes you want to add in queue: 3
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 1
enter the element = 10
10 is added to the queue
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 1
enter the element = 20
20 is added to the queue
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 1
enter the element = 30
30 is added to the queue
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 1
queue is full !!
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 3
[10, 20, 30]
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 2
remove element: 10
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 3
[20, 30]
select the operation 1.add 2.remove 3.show 4.quit
enter your choice: 4

'''
        
        

        
        
        


