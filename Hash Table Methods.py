# Connor Smith
# CSC231 Dr. Ferner
# 6-18-20
# Creates hash tables of student records and finds records from IDs. Records
# the time it takes to complete the inserting and searching


from Student import Student
from LinkedList import LinkedList
from HashTable import HashTableProbing
from HashTable import HashTableChaining
import time


def part1():
    record_names = ['listOfNames_short.txt', 'listOfNames_med.txt', 'listOfNames_long.txt']
    search_names = ['searchIds_short.txt', 'searchIds_med.txt', 'searchIds_long.txt']
    print("Hash Table Chaining")
    print("-------------------")
    for i in range(len(record_names)):
        if i == 0:
            print("Short Data")
            print("----------")
        elif i == 1:
            print()
            print("Medium Data")
            print("-----------")
        else:
            print()
            print("Long Data")
            print("---------")
        std_lst = HashTableChaining()
        new_file = open('txt_files/' + record_names[i], 'r')
        for line in new_file:
            x = line.strip()
            y = x.split('\t')
            current = Student(int(y[0]), y[1])
            std_lst.insert(current)
        new_file.close()
        second_file = open('txt_files/' + search_names[i], 'r')
        for line in second_file:
            x = line.strip()
            current = Student(int(x))
            if std_lst.find(current) is not None:
                print("Looking for: " + str(current) + "  Found Student record:", std_lst.find(current))
            else:
                print("Student ID", current, "is not found.")
        second_file.close()


def part2():
    record_names = ['listOfNames_short.txt', 'listOfNames_med.txt', 'listOfNames_long.txt']
    search_names = ['searchIds_short.txt', 'searchIds_med.txt', 'searchIds_long.txt']
    primeNumbers = (750019, 740011, 730003, 720007, 710009, 700001, 690037, 680003, 670001, 660001, 650011, 640007,
                    630017, 620003)
    print("Hash Table Probing")
    print("-------------------")
    for i in range(len(record_names)):
        if i == 0:
            print("Short Data")
            print("----------")
        elif i == 1:
            print()
            print("Medium Data")
            print("-----------")
        else:
            print()
            print("Long Data")
            print("---------")
        std_lst = HashTableProbing(750019)
        new_file = open('txt_files/' + record_names[i], 'r')
        for line in new_file:
            x = line.strip()
            y = x.split('\t')
            current = Student(int(y[0]), y[1])
            std_lst.insert(current)
        new_file.close()
        second_file = open('txt_files/' + search_names[i], 'r')
        for line in second_file:
            x = line.strip()
            current = Student(int(x))
            if std_lst.find(current) is not None:
                print("Looking for: " + str(current) + "  Found Student record:", std_lst.find(current))
            else:
                print("Student ID", current, "is not found.")
        second_file.close()


def part3():
    record_names = ['listOfNames_short.txt', 'listOfNames_med.txt', 'listOfNames_long.txt']
    search_names = ['searchIds_short.txt', 'searchIds_med.txt', 'searchIds_long.txt']
    primeNumbers = (750019, 740011, 730003, 720007, 710009, 700001, 690037, 680003, 670001, 660001, 650011, 640007,
                    630017, 620003, 100003, 90001, 80021, 70001, 60013, 50021, 40009, 30011, 20011, 10007)
    print("Hash Table Chaining")
    print("-------------------")
    print()
    print("Long Data")
    print("---------")
    for tableSize in primeNumbers:
        std_lst = HashTableChaining(tableSize)
        new_file = open('txt_files/' + record_names[2], 'r')
        count1 = 0
        count2 = 0
        startTime = time.time()
        for line in new_file:
            x = line.strip()
            y = x.split('\t')
            current = Student(int(y[0]), y[1])
            std_lst.insert(current)
            count1 += 1
        new_file.close()
        endTime = time.time()
        second_file = open('txt_files/' + search_names[2], 'r')
        startTime2 = time.time()
        for line in second_file:
            x = line.strip()
            current = Student(int(x))
            std_lst.find(current)
            count2 += 1
        second_file.close()
        endTime2 = time.time()
        print("Using Chaining with tableSize " + str(tableSize) + " it took " + str(format(endTime - startTime, "6.4f"))
              + " to insert " + str(count1) + " students.")
        print("Using Chaining with tableSize " + str(tableSize) + " it took " +
              str(format(endTime2 - startTime2, "6.4f")) + " to search through " + str(count2) + " students.")
        print()


def part4():
    record_names = ['listOfNames_short.txt', 'listOfNames_med.txt', 'listOfNames_long.txt']
    search_names = ['searchIds_short.txt', 'searchIds_med.txt', 'searchIds_long.txt']
    primeNumbers = (750019, 740011, 730003, 720007, 710009, 700001, 690037, 680003, 670001, 660001, 650011, 640007,
                    630017, 620003)
    print("Hash Table Probing")
    print("-------------------")
    print()
    print("Long Data")
    print("---------")
    for tableSize in primeNumbers:
        std_lst = HashTableProbing(tableSize)
        new_file = open('txt_files/' + record_names[2], 'r')
        count1 = 0
        count2 = 0
        startTime = time.time()
        for line in new_file:
            x = line.strip()
            y = x.split('\t')
            current = Student(int(y[0]), y[1])
            std_lst.insert(current)
            count1 += 1
        new_file.close()
        endTime = time.time()
        second_file = open('txt_files/' + search_names[2], 'r')
        startTime2 = time.time()
        for line in second_file:
            x = line.strip()
            current = Student(int(x))
            std_lst.find(current)
            count2 += 1
        second_file.close()
        endTime2 = time.time()
        print("Using Probing with tableSize " + str(tableSize) + " it took " + str(format(endTime - startTime, "6.4f"))
              + " to insert " + str(count1) + " students.")
        print("Using Probing with tableSize " + str(tableSize) + " it took " +
              str(format(endTime2 - startTime2, "6.4f")) + " to search through " + str(count2) + " students.")
        print()


def printing():
    """
    Executes printing functions
    :return: None
    """
    part1()
    print()
    print()
    part2()


def timing():
    """
    Executes timing functions.
    :return: None
    """
    part3()
    print()
    print()
    part4()


def main():
    # printing()
    timing()


if __name__ == "__main__":
    main()
