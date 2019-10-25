'''
this module is a simple FIFO queue
'''
import os


q = []

def help():
    print('this script is a simple process safe general queue managed as a list')
    print('the queue is intended as a FIFO queue, where you cannot get the values of any')
    print('items in the queue without calling the pop function')
    print('use the isEmpty() function to test if the queue is empty')
    print('use the pop() function to pop the first item from the queue')
    print('note, this will remove the item from the queue and return it to the var calling the pop function')
    print('use the add(item) function to add the item to the queue, all types supported')
    print('use the dump() function to dump a copy of the queue to the console, or redirect output to a text file')

def isEmpty():
    if len(q) <= 0:
        return True
    else:
        return False

def pop():
    global q
    #print(q) #debug
    item = q[0]
    #print(item) #debug
    r = []
    for i in range(1, len(q)):
        r.append(q[i])
    #print('r', r) #debug
    q = r
    #print('q', q) #debug
    return item

def add(thing):
    q.append(thing)

def dump():
    print(q)


if __name__ != '__main__':
    print("qE imported")

if __name__ == '__main__':
    print("qE not imported")
    for i in range(10):
        add(i)
    print('q initalized for troubleshooting')
    