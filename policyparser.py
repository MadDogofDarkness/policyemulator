'''parses xml formatted apim policies'''
document = []
policy = []

class Element:
    def __init__(self, tagname):
        self.tagname = tagname
    
    def tostring(self):
        return self.tagname

def findtags(docc):
    count = 0 #debug
    tagname = ''
    tag = False
    for line in docc:
        for c in line:
            if c == '<':
                count += 1 #debug
                tag = True
            elif c == ' ' or c == '>':
                policy.append(tagname)
                tagname = ''
                tag = False
            else:
                tagname += c
    print(count)


if __name__ == '__main__':
    fn = input("input a file to parse: ")
    try:
        f = open(fn, 'r')
    except FileNotFoundError:
        print("file not found")
        exit()

    for line in f:
        document.append(line)
    f.close()
    print(document)
    findtags(document)
    exit()
