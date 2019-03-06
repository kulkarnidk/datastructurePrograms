class Node:
    def __init__(self, data):
        """
        :param data:elements inserted into node using data attribute
        """
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """
        constructor of the linkedlist class
        """
        self.head = None
        self.pre_node = None

    def insert_with_sorting(self, data):
        """
        :param data:data is inserted into the node and sorted
        :return:will not return anything
        """
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        elif self.head.data > newNode.data:
            newNode.next = self.head
            self.head = newNode
        else:
            n = self.head
            while n is not None:
                if n.data > newNode.data:
                    newNode.next = n
                    self.pre_node.next = newNode
                    break
                self.pre_node = n
                n = n.next
            self.pre_node.next = newNode

    def search(self,element):
        """
        :param element:element to be search from the list be passed here
        :return:if data present will returns true if not present
        returns false
        """
        current = self.head
        while current != None:
            if current.data == element:
                return True
            current = current.next
        return False

    def delete(self, element):
        """
        :param element:deleting a perticular element from node
        :return:not return anything
        """
        current = self.head
        while current != None:
            if self.head.data == element:
                self.head = self.head.next
                break
            if current.data == element:
                self.last_node.next = current.next
                break
            self.last_node = current
            current = current.next

    def display1(self):
        """
        it will display the elements
        :return: it will not return anything
        """
        n = self.head
        while n is not None:
            print(n.data, end=" ")
            n = n.next

    def returnvalue(self):
        """
        it will display the elements
        :return: it will not return anything
        """
        values=[]
        n = self.head
        while n is not None:
            values.append(n.data)
            n = n.next
        return values

"""main method"""
if __name__ == '__main__':
    arr = []
    ll = []
    l = LinkedList()
    for i in range(11):
        l = LinkedList()
        ll.append(l)
    fo = open("Hashing.txt", "r")
    arr = fo.read()
    words = arr.strip().split(' ')
    fo.close()
    print("File Output: ")
    print(words)
    for i in range(len(words)):
        ll[int(words[i]) % 11].insert_with_sorting(int(words[i]))
    for i in range(len(ll)):
        print(ll[i].display1())

    print("enter element to search in linked list")
    element = int(input())
    element_hash = element % 11
    # for i in range(len(words)):
    var = ll[element_hash].search(element)
    print(var)
    if var:
        print("element found and removed from list")
        ll[element_hash].delete(element)
    else:
        print("element not found")
        print(element, " is added to list")
        ll[element_hash].insert_with_sorting(element)

    for i in range(len(ll)):
        print(ll[i].display1())
    a=[]
    for i in range(0,11):
        a.append(ll[element_hash].returnvalue())
        element_hash+=1
    print("updated list is: ",end=" ")
    print(a)






