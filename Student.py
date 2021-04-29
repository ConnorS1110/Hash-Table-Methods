# Connor Smith
# Dr. Ferner CSC231
# 5-28-20
# A program that reads student IDs and names to create Student objects. Then reads a file of IDs and outputs the
# correct student's name, if it exists. Outputs a statement to notify of an invalid ID number.


class Student:
    def __init__(self, ID=None, name=""):
        """
        Constructor for Student object
        :param ID: Integer student ID number
        :param name: Name of student
        """
        self.__ID = ID
        self.__name = name

    def getID(self):
        """
        Getter for ID
        :return: ID
        """
        return self.__ID

    def setID(self, ID):
        """
        Setter for ID
        :param ID: Integer ID for student
        :return: None
        """
        self.__ID = ID

    def getName(self):
        """
        Getter for name
        :return: Name
        """
        return self.__name

    def setName(self, name):
        """
        Setter for name
        :param name: String name
        :return: None
        """
        self.__name = name

    def __str__(self):
        """
        Returns string conversion of Student object
        :return: String of Student object
        """
        return str(self.__ID) + "    " + self.__name

    def __cmp__(self, other):
        if int(self.__ID) < int(other.__ID):
            return -1
        elif int(self.__ID) > int(other.__ID):
            return 1
        else:
            return 0

    def __lt__(self, other):
        """
        Overloads '<' operation
        :param other: Student ID number
        :return: Whether self ID is less than other ID
        """
        if self.__cmp__(other) == -1:
            return True
        else:
            return False

    def __le__(self, other):
        """
        Overloads '<=' operation
        :param other: Student ID number
        :return: Whether self ID is less than or equal to other ID
        """
        if self.__cmp__(other) == -1 or self.__cmp__(other) == 0:
            return True
        else:
            return False

    def __gt__(self, other):
        """
        Overloads '>' operation
        :param other: Student ID number
        :return: Whether self ID is greater than other ID
        """
        if self.__cmp__(other) == 1:
            return True
        else:
            return False

    def __ge__(self, other):
        """
        Overloads '>=' operation
        :param other: Student ID number
        :return: Whether self ID is greater than or equal to other ID
        """
        if self.__cmp__(other) == 1 or self.__cmp__(other) == 0:
            return True
        else:
            return False

    def __eq__(self, other):
        """
        Overloads '=' operation
        :param other: Student ID number
        :return: Whether self ID is equal to other ID
        """
        if self.__cmp__(other) == 0:
            return True
        else:
            return False

    def __ne__(self, other):
        """
        Overloads '!=' operation
        :param other: Student ID number
        :return: Whether self ID is not equal to other ID
        """
        if self.__cmp__(other) != 0:
            return True
        else:
            return False

    def __mod__(self, other):
        if isinstance(other, int):
            return int(self.__ID) % other
        else:
            return int(self.__ID) % int(other.__id)


def binarySearch(alist, item):
    """
    Performs a binary search and outputs the correct match
    :param alist: list to search
    :param item: value to find in alist
    :return: The value at the current index of alist
    """
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
            return alist[midpoint].getName()
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    if not found:
        return "The ID: " + str(item) + " cannot be found."


def main():
    """
    Reads a text file of student IDs and names to create a list of Student objects. Then reads a second text file of
        student IDs and performs a brute force method of searching for the name associated with the ID. Then searches
        the same file using a binary search method instead and outputs the correct name. If no name is associated with
        an ID, a message is output saying an ID is invalid.
    :return: None
    """
    std_lst = []
    new_file = open('listOfNames_short.txt', 'r')
    for line in new_file:
        x = line.strip()
        y = x.split('\t')
        current = Student(y[0], y[1])
        std_lst.append(current)
    new_file.close()
    std_lst.sort()
    second_file = open('searchIds_short.txt', 'r')
    shrt_lst = []
    for line in second_file:
        x = line.strip()
        current = Student(x)
        shrt_lst.append(current)
    second_file.close()
    print()
    print("Search using brute force method")
    print("-------------------------------")
    i = 0
    j = 0
    while i < len(shrt_lst):
        while j < len(std_lst):
            if shrt_lst[i] == std_lst[j]:
                print(i + 1, ".", "The ID:", shrt_lst[i], "belongs to", std_lst[j].getName())
                i = i + 1
                j = 0
            else:
                j = j + 1
            if j == len(std_lst):
                print(i + 1, ".", "The ID: " + str(shrt_lst[i]) + " cannot be found.")
                i = i + 1
                j = 0
            if i > len(shrt_lst) - 1:
                break
    print()
    print()
    print("Search using binary search")
    print("--------------------------")
    shrt_lst.sort()
    s = 0
    while s < len(shrt_lst):
        if binarySearch(std_lst, shrt_lst[s]) != "The ID: " + str(shrt_lst[s]) + " cannot be found.":
            print(s + 1, '.', "The ID:", shrt_lst[s], "belongs to", binarySearch(std_lst, shrt_lst[s]))
            s = s + 1
        else:
            print(s + 1, '.', binarySearch(std_lst, shrt_lst[s]))
            s = s + 1


if __name__ == "__main__":
    main()
