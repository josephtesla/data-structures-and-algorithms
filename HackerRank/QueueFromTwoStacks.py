# Enter your code here. Read input from STDIN. Print output to STDOUT

class Queue:
    def __init__(self):
        self.__newStack = []
        self.__oldStack = []

    def is_empty(self):
        return len(self.__newStack) == len(self.__oldStack) == 0

    def get_front(self):
        self.check_and_shift()
        return None if self.is_empty() else self.__oldStack[-1]

    def enqueue(self, element):
        self.__newStack.append(element)

    def dequeue(self):
        self.check_and_shift()
        return None if self.is_empty() else self.__oldStack.pop()

    def check_and_shift(self):
        if not self.__oldStack:
            while self.__newStack:
                top = self.__newStack.pop()
                self.__oldStack.append(top)

#
# def main():
#     queue = Queue()
#     queries_no = input("")
#     for i in range(int(queries_no)):
#         t = input("").split(" ")
#         if t[0] == "1":
#             queue.enqueue(t[1])
#         elif t[0] == "2":
#             queue.dequeue()
#         else:
#             print(queue.get_front())
#
#
# main()

