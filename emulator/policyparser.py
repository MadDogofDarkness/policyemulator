'''parses xml formatted apim policies'''
document = []

class Element:
    def __init__(self, tagname):
        self.tagname = tagname
    
    def tostring(self):
        return self.tagname


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
    exit()
