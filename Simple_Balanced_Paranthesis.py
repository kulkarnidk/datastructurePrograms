class Stack:
    def __init__(self):
        """
        constructor of the stack
        creating empty array
        """
        self.stack_Array=[]

    def push(self,d):
        """
        :param d:appending data d to the array
        :return:will not return anything
        """
        self.stack_Array.append(d)

    def pop(self):
        """
        throws exception if stack is empty
        :return: returns poped elements
        """
        try:
            return self.stack_Array.pop()
        except Exception:
            print("stack is empty can't pop")
    def is_Empty(self):
        return self.stack_Array==[]

    def size(self):
        """
        :return:returns length of the stack
        """
        return len(self.stack_Array)

    def print_Stack(self):
        """
        prints the stack in reversed order
        :return: will not return anything
        """
        for i in reversed(self.stack_Array):
            print(i)

if __name__=='__main__':
    s=Stack()
    push_count=0
    pop_count=0
    expression=[]
    expression=input("enter the arithmatic expression: ")
    for i in range(len(expression)):
        if expression[i] == '(':
            s.push(i)
            push_count+=1
            print(" ( is pushed at index ",i)
        elif expression[i]==')':
            if s.is_Empty():
                s.pop()
                pop_count += 1
                print("cant pop stack is empty")
                break
            else:
                s.pop()
                pop_count += 1
                print(" ) is poped at index ", i)
if push_count==pop_count:
    print("parenthes is balanced")
else:
    print("parenthesis not balanced")



