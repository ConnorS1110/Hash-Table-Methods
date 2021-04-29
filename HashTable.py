# Connor Smith
# CSC231 Dr. Ferner
# 6-15-20
# Creates hash tables using chaining and probing methods


from LinkedList import LinkedList
import random


class HashTableChaining:
    def __init__(self, size=67):
        """
        Constructor
        :param size: Size of hash table. Default is size 67.
        """
        self.__buckets = []
        for i in range(size):
            self.__buckets.append(LinkedList())

    def __hash(self, value):
        """
        Hash function
        :param value: Value to hash
        :return: The bucket number for the value
        """
        return value % len(self.__buckets)

    def insert(self, value):
        """
        Inserts a value to hash table
        :param value: Value to be inserted
        :return: None
        """
        bucketNum = self.__hash(value)
        self.__buckets[bucketNum].append(value)

    def find(self, value):
        """
        Finds a value in a hash table
        :param value: Value to be found
        :return: Bucket containing value
        """
        bucketNum = self.__hash(value)
        result = self.__buckets[bucketNum].find(value)
        return result

    def __str__(self):
        """
        Converts hash table to string
        :return: String conversion of hash table
        """
        result = ""
        for i in range(len(self.__buckets)):
            result += "Bucket " + str(i) + ":  " + str(len(self.__buckets[i])) + ":"
            result += str(self.__buckets[i]) + "\n"
        return result


class HashTableProbing:
    def __init__(self, size=67):
        """
        Constructor.
        :param size: Size of hash table
        """
        self.__buckets = [None] * size
        self.__skip = 3

    def __hash(self, value):
        """
        Hash function
        :param value: Value to hash
        :return: Bucket number for the value
        """
        return value % len(self.__buckets)

    def __rehash(self, bucketNum):
        """
        Rehash function
        :param bucketNum: Old bucket number to hash
        :return: New bucket number to hash
        """
        return (bucketNum + self.__skip) % len(self.__buckets)

    def insert(self, value):
        """
        Inserts a value into the hash table
        :param value: Value to be inserted
        :return: None
        """
        bucketNum = self.__hash(value)
        originalBucketNum = bucketNum
        if self.__buckets[bucketNum] is not None:
            bucketNum = self.__rehash(bucketNum)
        while self.__buckets[bucketNum] is not None and bucketNum != originalBucketNum:
            bucketNum = self.__rehash(bucketNum)
        if self.__buckets[bucketNum] is None:
            self.__buckets[bucketNum] = value
        else:
            raise Exception("Table Full")

    def find(self, value):
        """
        Finds a value in the hash table
        :param value: Value to find
        :return: The value if found and none if not found
        """
        bucketNum = self.__hash(value)
        originalBucketNum = bucketNum
        if self.__buckets[bucketNum] is not None and self.__buckets[bucketNum] == value:
            return self.__buckets[bucketNum]
        else:
            bucketNum = self.__rehash(bucketNum)
        while self.__buckets[bucketNum] is not None and self.__buckets[bucketNum] != value and \
                bucketNum != originalBucketNum:
            bucketNum = self.__rehash(bucketNum)
        if self.__buckets[bucketNum] is not None and self.__buckets[bucketNum] == value:
            return self.__buckets[bucketNum]
        else:
            return None

    def __str__(self):
        """
        Converts hash table to string
        :return: String conversion of hash table
        """
        result = ""
        for i in range(len(self.__buckets)):
            result += "Bucket " + str(i) + ":  " + str(self.__buckets[i]) + "\n"
        return result


def main():
    test1 = HashTableChaining()
    randInts = []

    for i in range(20):
        x = random.randint(0, 100)
        randInts.append(x)
        test1.insert(x)

    print("Chaining")
    print("--------")
    print(randInts)
    print(test1)
    test1.insert(101)
    print(test1)
    print(test1.find(101))
    print()
    print()

    test2 = HashTableProbing()
    randInts2 = []

    for i in range(20):
        x = random.randint(0, 100)
        randInts2.append(x)
        test2.insert(x)

    print("Probing")
    print("-------")
    print(randInts2)
    print(test2)
    test2.insert(102)
    print(test2)
    print(test2.find(102))


if __name__ == "__main__":
    main()
