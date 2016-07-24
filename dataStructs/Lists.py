class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def setNext(self,newNext):
        self.next = newNext

    def getData(self):
        return self.data

    def __next__(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata


class UnorderedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.size

    def __contains__(self,item):
        found = False
        current = self.head
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.next

        return found    

    def append(self,item):
        tmp = Node(item)
        current = self.head
        while current.next != None:
            current = current.next

        current.next = tmp
        tmp.next = none 
        self.size += 1

    def remove(self,item):
        found = False
        prev = None
        curr = self.head
        while not found and curr != None:
            if curr.data == item:
                found = True
            else:
                prev = curr
                curr = curr.next
        
        if prev == None:
            self.head = curr.next
        else:
            prev.next = curr.next
        
        curr = None
        self.size -= 1

        def __iter__(self):
            curr = self.head

            while curr is not None:
                yield curr
                curr = curr.next



class OrderedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self,data):
        tmp = Node(item)
        found = False
        curr = self.head
        prev = None
        while curr.next != None and not found:
            if item < curr.data:
                found = True
            else:
                prev = curr
                curr = curr.next

        if prev == None:            
            self.head = tmp
        else:
            prev.next = tmp

        tmp.next = curr
        self.size += 1

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def __contains__(self,item):
        found = False
        current = self.head
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.next

        return found    

    def remove(self,item):
        found = False
        prev = None
        curr = self.head
        while not found:
            if curr.data == item:
                found = True
            else:
                prev = curr
                curr = curr.next
        
        if prev == None:
            self.head = curr.next
        else:
            prev.next = curr.next
        
        curr = None
        self.size -= 1

        def __iter__(self):
            curr = self.head

            while curr is not None:
                yield curr
                curr = curr.next