class Node (object):
    def __init__(self, value):
        self.value = value
        self.next = None

class  LinkedList(object):
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
    
    def printlist(self):
        node = self.head
        
        while(True):
            print("{0}  ".format(node.value))
            if node.next != None:
                node = node.next
            else:
                break

    def traverseToIndex(self, index):
        count = 0
        node = None

        if index >= self.length:
            return None

        cur = self.head
        node = cur
        while(count < index):
            node = cur
            cur = cur.next
            count += 1
            
        return node

    def append(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def insert(self, index, value):

        if index == 0:
            self.prepend(value)
            return
        elif index >= self.length:
            self.append(value)
            return

        new_node = Node(value)    
        i = 0
        cur_node = self.head
        while(i < index-1):
            i += 1
            cur_node = cur_node.next

        temp = cur_node.next
        new_node.next = temp
        cur_node.next = new_node        
        self.length += 1

    def remove(self, value):
        cur_node = self.head

        if cur_node.value == value:
            self.head = cur_node.next
            self.length -= 1
            return

        while(cur_node != None):
            if cur_node.next.value == value:
                cur_node.next = cur_node.next.next
                self.length -= 1
                break
            else:
                cur_node = cur_node.next

linkedlist = LinkedList(10)
linkedlist.append(15)
linkedlist.append(20)
linkedlist.prepend(5)
linkedlist.insert(0, 100)
linkedlist.insert(10, 7)
linkedlist.printlist()
linkedlist.remove(15)
# print("== after deletion ==")
# linkedlist.printlist()
index = 0
node = linkedlist.traverseToIndex(index)
if node is not None:
    print ("Value at index {0} is {1}".format(index, node.value))
else:
    print ("Value not found in index {0}".format(index))
    