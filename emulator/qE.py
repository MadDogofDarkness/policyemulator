'''
this module is a simple FIFO queue
'''


q = []

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
    