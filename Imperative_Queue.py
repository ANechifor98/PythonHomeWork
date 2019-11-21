#recursive function
import timeit

todo_queue = ""

def add_item_to_queue(item):
    global todo_queue
    todo_queue += item
    return todo_queue

#an imperative implementation of the len() function because len() utilises a list
def length(string):
    count = 0
    for char in string:
        count += 1
    return count

def delete_task():
    global todo_queue
    count = 0
    i = 0
    while i < length(todo_queue):
        if todo_queue[i:i+1] == "\n":
            count += 1
        if count == 6:  #the whole task has encountered and is ready to be removed from the list
            todo_queue = todo_queue[i+1:] #removes task from queue
            break #end loop
        i += 1
    return todo_queue

def delete_event():
    global todo_queue
    count = 0
    i = 0
    while i < length(todo_queue):
        if todo_queue[i:i+1] == "\n":
            count += 1
        if count == 5: #the whole event has encountered and is ready to be removed from the list
            todo_queue = todo_queue[i+1:] #removes event from queue
            break #end loop
        i += 1
    return todo_queue


def remove_item_from_queue():
    global todo_queue
    i = 0
    while i < length(todo_queue):
        if todo_queue[i:i+6] == "\nTask\n": #detects if the next item in the queue is a task
            delete_task()
            break
        if todo_queue[i:i+7] == "\nEvent\n": #detects if the next item in the queue is an event
            delete_event()
            break
        i += 1
    return todo_queue

#for testing purposes only, only one use of a print function at a time is recommended for clarity and readibility purposes
if __name__ == "__main__":
    start = timeit.default_timer()
    task1 = "\nTask\nDate: 1/1/2020\nStart Time: 1100\nDuration: 4 hours\nPeople Assigned: Train Wrecks, Fish Moley\n"
    task2 = "\nTask\nDate: 1/1/2021\nStart Time: 1200\nDuration: 5 hours\nPeople Assigned: Jess Jones, Sarah Smiles\n"
    event1 = "\nEvent\nDate: 1/1/2022\nStart Time: 1300\nLocation: Paris\n"
    event2 = "\nEvent\nDate: 1/1/2023\nStart Time: 1400\nLocation: Dubai\n"
    add_item_to_queue(task1)
    add_item_to_queue(task2)
    add_item_to_queue(event1)
    print(add_item_to_queue(event2))
    remove_item_from_queue()
    remove_item_from_queue()
    remove_item_from_queue()
    remove_item_from_queue()
    stop = timeit.default_timer()
    print(stop - start) #runtime of this queue
