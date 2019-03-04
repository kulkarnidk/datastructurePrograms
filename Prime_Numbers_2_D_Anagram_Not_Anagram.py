from array import array
import numpy


def prime_Anagram(str1):
    """generating prime numbers by taking
    method argument str1"""
    anagram = []
    non_Anagram = []
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
    """
    Anagram Code For Prime Number
    comparing length of two strings if 
    they are equal in length then sorting both and 
    comparing if found equal then appending to array
    
    """
    flag = True
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if len(str(arr[i])) == len(str(arr[j])):
                var1 = ''.join(sorted(str(arr[i])))
                var2 = ''.join(sorted(str(arr[j])))
                if var1 == var2:
                    anagram.append(arr[i])
                    anagram.append(arr[j])
                    flag = False
        if flag:
            non_Anagram.append(arr[i])
        else:
            flag = True
    """
    declaring numpy for 2 rows and 158 columns
    """
    numarray = numpy.zeros((2, 158))
    for j in range(0, len(anagram)):
        numarray[0][j] = anagram[j]
    for k in range(0, len(non_Anagram)):
        numarray[1][k] = non_Anagram[k]
    """
    printing 2D numpy array for anagram and non-anagram prime numbers
    """
    print(numarray)

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
