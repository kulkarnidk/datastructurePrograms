def factorial(num):
    """
    @:param calculates the factorial of num
    :param num:input for factorial method for calculation of factorial
    :return:returns factorial number of num
    """
    res = 1
    for i in range(1, num + 1):
        res = res * i
    return res
tree_values=[]
tree_count=[]
num=int(input("enter number : "))
for i in range(1, num+1):
    print("enter ",i,"value ")
    tree_values.append(int(input()))
print("Trees :",tree_values)
for i in tree_values:
    countBST1 = factorial(2 * i)
    countBST2 = factorial(i + 1) * factorial(i)
    tree_count.append(countBST1 // countBST2)
print("binary tree count: ",tree_count)
