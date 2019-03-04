from array import array
import numpy

"""Implemented Stack using Linked List """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        """push operation, pushes the data into the node"""
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        """pop the data which is there in node"""
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def display(self):
        """Displays the contents"""
        n = self.head
        while n is not None:
            print(n.data, end=" ")
            n = n.next


def prime_Anagram(str1):
    """generating prime numbers by taking
    method argument str1"""
    anagram = []
    arr = array('i', [])
    for i in range(0, str1):
        count = 0
        if i != 0 and i != 1:
            for j in range(2, i):
                if i % j == 0:
                    count = count + 1
                    break
            if count == 0:
                arr.append(i)

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if len(str(arr[i])) == len(str(arr[j])):
                var1 = ''.join(sorted(str(arr[i])))
                var2 = ''.join(sorted(str(arr[j])))
                if var1 == var2:
                    anagram.append(arr[i])
                    anagram.append(arr[j])

    """creating object of stack class"""
    s = Stack()
    for i in anagram:
        s.push(i)
    for i in range(0, 158):
        p = s.pop()
        print(p, end=" ")

    """ Main Method"""


if __name__ == '__main__':
    """
        start of main method
        validation of the range
        Calling the prime anagram Method 
        with start as Method Argument

    """
    start = int(input("Enter Range: "))
    if start == 1000:
        prime_Anagram(start)
    else:
        print("Range should be 1000")
