import numpy


def day(month, year, day):
    """
    @:param this method is for calculation of day
    :param month:takes month as user input
    :param year: takes year as user input
    :param day: takes day as 1
    :return: returns value of d0
    """
    y0 = year - (14 - month) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = month + 12 * ((14 - month) // 12) - 2
    d0 = (day + x + 31 * m0 // 12) % 7
    return d0

def isleapyear(year):
    """
    @:param this method is for finding leap year
    :param year:will take year as input and calculates leap year
    :return: returns true if leap otherwise returns false
    """
    if int(year) % 4 == 0:
        return True
    else:
        return False


months = ["", "january", "fabruary", "march", "april", "may", "june", "july", "august", "september", "october",
          "november", "december"]
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
if month == 2 and isleapyear(year):
    days[month] = 29
space = day(month, year, 1)
array = numpy.zeros((6, 7), dtype=int)
x = 1
dayz = space
for i in range(6):
    for j in range(space, 7):
        if x <= days[month]:
            array[i][j] = x
            x += 1
    space = 0
for j in range(dayz):
    array[0][j] = array[5][j] = 0

print("       CALENDAR  ", month, " ", year)
print("------------------------------------")
print("", months[month], "         ", year)
print("------------------------------------")
print("SUN   MON   TUE  WED  THU  FRI  SAT")
print("------------------------------------")

for i in range(5):
    for j in range(7):
        if array[i][j] != 0:
            print(array[i][j], end="    ")
        else:
            print(end="      ")
    print()
