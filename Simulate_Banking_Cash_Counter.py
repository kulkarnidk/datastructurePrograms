class Queue:

    def __init__(self, capacity):
        """
        :param capacity:constructor of Queue class with capacity as argument
        """
        self.capacity = capacity
        self.q = [] * self.capacity
        self.front = 0
        self.rear = 0
        self.balance=0

    def enqueue(self):
        """
        enqueues the elements
        :return:will not return anything
        """
        if self.capacity == self.rear:
            print("queue is full")
        else:
            deposit_amount = int(input("Enter the Amount:"))
            print("Rupees ",deposit_amount, " is depositd")
            self.balance=self.balance+deposit_amount
            print("Your Balance is :",self.balance)
            self.q.append(deposit_amount)
            self.rear += 1
            print(self.q)

    def dequeue(self):
        """
        dequeues the elements from the queue
        :return:will not return anything
        """
        if self.front == self.rear:
            print("queue is empty")
        else:
            print("Enter the amount to be Withdraw :")
            withdraw_amount=int(input())
            self.balance=self.balance-withdraw_amount
            self.q.append(self.balance)
            print("Your Remaining Balance is :",self.balance)
            print("dequeued from queue", self.q[self.front])
            self.rear -= 1
            for i in range(self.front, self.rear):
                self.q[i] = self.q[i + 1]

    def display_Queue(self):
        """
        will display the elements in the queue
        :return: will not return anything
        """
        if self.front == self.rear:
            print("queue is empty")
        else:
            print("queue elements are")
            for i in range(self.front, self.rear):
                print("People in Queue :",self.q[i])
            self.rear -= 1



"""main method"""
if __name__ == '__main__':
    q = Queue(5)
while True:
    print()
    print("========Banking Cash Counter=========")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Number of people in Queue")
    print("4.Quit")
    choice = int(input())
    if choice == 1:
        q.enqueue()
    elif choice == 2:
        q.dequeue()
    elif choice==3:
        q.display_Queue()
    elif choice==4:
        break