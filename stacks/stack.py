class Node (object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack(object):
    def __init__(self, value):
        self.top = Node(value)
        self.bottom = self.top
        self.length = 1
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        element = self.top
        self.top = self.top.next
        self.length -= 1

        return element
    
    def parse(self):

        element = self.top
        while(element != None):
            print(element.value)
            element = element.next

s = Stack("www.youtube.com")
s.push("udemy.com")
s.push("linkedin.com")
s.parse()
print("====")
print(s.pop().value)
print("====")
s.parse()
print("====")
print(s.pop().value)
print("====")
s.parse()
print("====")