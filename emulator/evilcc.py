'''
a simple command console in python for remote administration of Azure resources

'''
import qE

def printEntities(listofentities, col, headers):
    headlen = 0
    heads = ''
    for header in headers:
        headlen += len(header)
        heads += str(header) + " | "
    print(heads)
    heads = ''
    for i in range(headlen + 3 * len(headers)):
        heads += '-'
    if heads != '':
        print(heads)
    

def loadEntities(filename, col, headers):
    f = open(filename, 'r')
    cup = ''
    entities = []
    for line in f:
        qE.add(line)
    
    while not qE.isEmpty():
        s = qE.pop()
        for c in s:
            if c == ',':
                entities.append(cup)
                cup = ''
            else:
                cup += c
    
    printEntities(entities, col, headers)
    return entities

print(loadEntities('listofstuff.txt', 3, ['entityID', 'email', 'password']))
    
