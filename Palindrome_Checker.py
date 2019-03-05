class Dequeue:
    def __init__(self,capacity):
        """
        :param capacity:capacity of the dequeue
        """
        self.capacity=capacity
        self.front=0
        self.rear=0
        self.dequeue=[]*capacity

    def insert_at_rear(self,lower_case):
        """
        it will insert elements to the dequeue
        :return:it will not return anything
        """
        if self.capacity==self.rear:
            print("Dequeue is full")
        else:

            for i in lower_case:
                self.dequeue.append(i)
                self.rear+=1

    def display(self):
        """
        it will display the dequeue
        :return: it will not return anything
        """
        if self.front==self.rear:
            print("empty dequeue")
        else:
            for i in range(self.rear):
                print(self.dequeue[i],end=" ")
                self.rear-=1

    def remove_from_front(self):
        """
        :return:it will returns the front element of the dequeue
        """
        if self.front==self.rear:
            print("empty dequeue")
        else:
            # print("dequeued from front ", self.dequeue[self.front])
            self.front += 1
            return self.dequeue[self.front-1]


    def remove_from_rear(self):
        """
        :return:it return the rear element of the dequeue
        """
        if self.rear==self.front:
            print("empty dequeue")
        else:
            # print("dequeued from rear ", self.dequeue[self.rear-1])
            self.rear-=1
            return self.dequeue[self.rear]

if __name__=='__main__':
    element = input("enter a string to check palindrome or not: ")
    lower_case = element.lower()
    d=Dequeue(len(lower_case))
    d.insert_at_rear(lower_case)
    for i in range(len(lower_case)//2):
        if d.remove_from_front()==d.remove_from_rear():
            if i==(len(lower_case)//2)-1:
                print("palindrome")
        else:
            print("not palindrome")
            break;


