def printBalancedParentheses(n):
    results = []

    def print_balance(left, right, curr=""):
        if left == right == 0:
            results.append(curr)
            return

        if left > 0:
            print_balance(left - 1, right, curr + "(")

        if left < right:
            print_balance(left, right - 1, curr + ")")

    print_balance(n, n)

    return results


# print(printBalancedParentheses(2))
from datetime import datetime


class MagicArray:
    def __init__(self, size):
        self.__size = size
        self.__array_content = [None] * size
        self.__array_timestamps = [None] * size
        self.__put_all_value = None
        self.__put_all_time = None

    def __len__(self):
        return self.__size

    def __get_time_stamp(self):
        return datetime.now().time()

    def get(self, index):
        if index >= self.__size:
            raise Exception("Array index out of bounds")

        value_time = self.__array_timestamps[index]
        array_value = self.__array_content[index]

        print(value_time, self.__put_all_time, index, self.__array_content)

        if value_time:
            if self.__put_all_time and self.__put_all_time > value_time:
                return self.__put_all_value
            else:
                return array_value
        else:
            return self.__put_all_value

    def put(self, index, value):
        if index >= self.__size:
            raise Exception("Array index out of bounds")

        self.__array_timestamps[index] = self.__get_time_stamp()
        self.__array_content[index] = value

    def putAll(self, value):
        for _ in range(100):
            self.do_nothing()

        self.__put_all_time = self.__get_time_stamp()
        self.__put_all_value = value

    def do_nothing(self):
        pass


myarray = MagicArray(5)
myarray.put(0, 15)
myarray.put(1, 14)
myarray.put(2, 22)
myarray.put(3, 25)
myarray.put(4, 36)

for i in range(len(myarray)):
    print(myarray.get(i))

myarray.putAll(10)
print('--------------------')
for i in range(len(myarray)):
    print(myarray.get(i))


myarray.put(2, 96)
myarray.put(4, 24)

print('--------------------')
for i in range(len(myarray)):
    print(myarray.get(i))


#myarray.put(5, 67)

