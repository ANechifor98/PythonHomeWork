class Task:
    def __init__(self, date, start_time, duration, people_assigned = []):
        self.date = date
        self.start_time = start_time
        self.duration = duration
        self.people_assigned = people_assigned
        
    def __str__(self):
        output = "Task -> Date: {} | Start Time: {} | Duration: {} | People Assigned: {} |".format(self.date, self.start_time, self.duration, self.people_assigned)
        return output

class Event:
    def __init__(self, date, start_time, location):
        self.date = date
        self.start_time = start_time
        self.location = location

    def __str__(self):
        output = "Event -> Date: {} | Start Time: {} | Location: {} |".format(self.date, self.start_time, self.location)
        return output

#Queue -> First In First Out
class Queue: 
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        return self.queue.pop(0)

#test
if __name__ == "__main__":
    task1 = Task("1/1/2020", "0800", "2 hours", ["Jim Jones", "Sally Springs"])
    task2 = Task("1/1/2021", "0900", "3 hours", ["Bob Bones", "Polly Pockets"])
    event1 = Event("1/1/2022", "0800", "Dublin")
    event2 = Event("1/1/2023", "0900", "Berlin")
    q = Queue()
    q.enqueue(task1)
    q.enqueue(task2)
    q.enqueue(event1)
    q.enqueue(event2)
    print('{}'.format(q.dequeue()))
    print('{}'.format(q.dequeue()))
    print('{}'.format(q.dequeue()))
    print('{}'.format(q.dequeue()))
