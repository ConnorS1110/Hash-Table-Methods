# Connor Smith
# CSC231 Dr. Ferner
# 6-3-20
# Creates a linked list ADT and allows the user to insert new nodes into
# the list and display the length of the list and the payloads in each of
# the nodes.


import random


class listNode:
    def __init__(self, __payload=None, __nextListNode=None):
        """
        Constructor.
        :param __payload: Payload
        :param __nextListNode: Next node to look at
        """
        self.__payload = __payload
        self.__nextListNode = __nextListNode

    def getPayload(self):
        """
        Gets the payload.
        :return: Payload
        """
        return self.__payload

    def setPayload(self, __payload):
        """
        Sets the payload
        :param __payload: current payload
        :return: None.
        """
        self.__payload = __payload

    def getNextListNode(self):
        """
        Gets the next list node.
        :return: Next list node
        """
        return self.__nextListNode

    def setNextListNode(self, __nextListNode):
        """
        Sets the next list node.
        :param __nextListNode: Next list node.
        :return: None
        """
        self.__nextListNode = __nextListNode


class LinkedList:
    def __init__(self, __head=None, __tail=None, __size=0):
        """
        Constructor.
        :param __head: Start of the list.
        :param __tail: Back of the list.
        :param __size: Length of the list.
        """
        self.__head = __head
        self.__tail = __tail
        self.__size = __size

    def __getIthNode(self, i):
        """
        Gets the Ith node.
        :param i: Current position
        :return: Node at current position, i.
        """
        if i < 0:
            i = len(self) - i
        elif i >= len(self):
            raise IndexError('list index out of range')
        current = self.__head
        count = 0
        while current is not None and count < i:
            count += 1
            current = current.getNextListNode()
        return current

    def insert(self, i, x):
        """
        Adds new node to list and increases size of the list by one.
        :param x: Payload to be added to inserted list node.
        :param i: Position
        :return: None
        """
        if self.isEmpty():
            self.__head = listNode(x)
            self.__tail = self.__head
        elif i <= 0:
            self.__head = listNode(x, self.__head)
        elif i >= self.__size:
            self.__tail.setNextListNode(listNode(x))
            self.__tail = self.__tail.getNextListNode()
        else:
            previous = self.__getIthNode(i - 1)
            previous.setNextListNode(listNode(x, previous.getNextListNode()))
            if self.__tail == previous:
                self.__tail = self.__tail.getNextListNode()
        self.__size += 1

    def __str__(self):
        """
        Coverts list nodes to string.
        :return: String conversion of list nodes.
        """
        result = ""
        current = self.__head
        while current is not None:
            result = result + " " + str(current.getPayload())
            current = current.getNextListNode()
        return result

    def __len__(self):
        """
        Finds the length of the list
        :return: Length of list
        """
        return self.__size

    def isEmpty(self):
        """
        Determines when there are list nodes or not
        :return: Boolean of whether there is a list node or not
        """
        return self.__head is None

    def front(self):
        """
        Returns the front of the list
        :return: The payload at the front of the list
        """
        if self.isEmpty():
            return None
        else:
            return self.__head.getPayload()

    def back(self):
        """
        Returns the back of the list
        :return: The payload at the back of the list
        """
        if self.isEmpty():
            return None
        else:
            return self.__tail.getPayload()

    def prepend(self, x):
        """
        Adds a payload to the front of the list
        :param x: Payload to be inserted
        :return: None
        """
        self.insert(0, x)

    def append(self, x):
        """
        Adds a payload to the back of the list
        :param x: Payload to be inserted
        :return: None
        """
        self.insert(len(self), x)

    def pop(self, i=None):
        """
        Pops a list node from the linked list.
        :param i:Position to pop
        :return:Payload popped.
        """
        if self.isEmpty():
            return None
        else:
            if i is None:
                i = self.__size - 1
            if i == 0:
                x = self.__head.getPayload()
                self.__head = self.__head.getNextListNode()
                self.__size -= 1
                if self.__head is None:
                    self.__tail = None
                return x
            else:
                previous = self.__getIthNode(i - 1)
                x = previous.getNextListNode().getPayload()
                if self.__tail == previous.getNextListNode():
                    self.__tail = previous
                previous.setNextListNode(previous.getNextListNode().getNextListNode())
                self.__size -= 1
                return x

    def find(self, x):
        """
        Finds a given value in the linked list.
        :return: The matched value or none if not found.
        """
        result = None
        current = self.__head
        while current is not None:
            if current.getPayload() == x:
                result = current.getPayload()
                current = None
            else:
                current = current.getNextListNode()
        return result

    def __getitem__(self, i):
        """
        Gets the payload
        :param i: Location to get payload from.
        :return: The payload at location i
        """
        return self.__getIthNode(i).getPayload()

    def __setitem__(self, i, value):
        """
        Sets value for a given position in the linked list.
        :param i: Position to set value for.
        :param value: Value to set
        :return: None
        """
        self.__getIthNode(i).setPayload(value)


def main():
    """
    Creates an empty linked list and adds 20 random integers from -100 to
        100, printing each number. Then adds a value to the middle and
        beginning of the list, printing information about the list at each
        step.
    :return: None
    """
    test = LinkedList()
    print("The list is empty ==", test.isEmpty())
    print("The front of the list is", test.front())
    print("The back of the list is", test.back())
    print("The size of the list is", len(test))
    print("The list is [", test, " ]")
    print()

    for i in range(20):
        x = random.randint(-100, 100)
        print(x)
        test.insert(i, x)

    print()
    print("The list is empty ==", test.isEmpty())
    print("The front of the list is", test.front())
    print("The back of the list is", test.back())
    print("The size of the list is", len(test))
    print("The list is [", test, " ]")
    print()

    test.insert(0, 1000)
    print("The list is empty ==", test.isEmpty())
    print("The front of the list is", test.front())
    print("The back of the list is", test.back())
    print("The size of the list is", len(test))
    print("The list is [", test, " ]")
    print()

    test.insert(5, 2000)
    print("The list is empty ==", test.isEmpty())
    print("The front of the list is", test.front())
    print("The back of the list is", test.back())
    print("The size of the list is", len(test))
    print("The list is [", test, " ]")
    print()

    test.insert(len(test), 4000)
    print("The list is empty ==", test.isEmpty())
    print("The front of the list is", test.front())
    print("The back of the list is", test.back())
    print("The size of the list is", len(test))
    print("The list is [", test, " ]")
    print()

    print(test[0])
    print(test[22])
    print(test[10])
    print()

    test[0] = 1
    print(test[0])
    test[22] = 2
    print(test[22])
    test[10] = 3
    print(test[10])
    print()

    test.prepend(24)
    print(test)
    test.append(60)
    print(test)
    print(test.find(60))


if __name__ == "__main__":
    main()
