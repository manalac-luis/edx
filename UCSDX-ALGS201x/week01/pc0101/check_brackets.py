# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

class Stack:
    def __init__(self,size):
        self.StackArray = []
        self.StackIndex = []
        self.top = 0
        for i in range(size):
            self.StackArray.append("")
            self.StackIndex.append(0)

    def push(self,c,i):
        self.StackArray[self.top]=c
        self.StackIndex[self.top]=i
        self.top = self.top+1

    def pop(self):
        c = self.StackArray[self.top-1]
        self.top = self.top - 1
        if (self.top <0):
            c="-1"
        return c

    def topOfStack(self):
        c = self.StackArray[self.top-1]
        return self.StackArray[self.top-1], self.StackIndex[self.top-1]

    def isempty(self):
        if self.top == 0:
            return True
        else:
            return False

def IsBalanced(str):
    stack = Stack(1000000)

    lastpushed =""
    lastpopped =""

    index = 0
    #print("IsBalanced:",str)
    for char in text:
        if char == '(' or char == '[' or char == '{':
            stack.push(char,index)
        if char == ')' or char == ']' or char == '}':
            lastpopped=stack.pop()
            if (char == ')') and (lastpopped!='('):
                return index
            if (char == ']') and (lastpopped!='['):
                return index
            if (char == '}') and (lastpopped!='{'):
                return index
        index = index+1

    if (stack.isempty()):
        return -1
    else:
        char,index = stack.topOfStack()
        #print("c,i",lastpopped,",",index)
        return index





if __name__ == "__main__":
    text = sys.stdin.read()


#  test stack


    #for i in range(10):
    #    print("*",i)
    #    stack.push(str(i))
    #for i in range(10):
    #    print(stack.pop())
    #print("text:",text)
    valid = IsBalanced(text)
    if (valid<0):
        print("Success")
    else:
        print(valid+1)
    #print(IsBalanced(text))

    opening_brackets_stack = []
    #for i, next in enumerate(text):
    #    if next == '(' or next == '[' or next == '{':
    #        # Process opening bracket, write your code here
    #        stack.push(next)

    #    if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
    #        stack.pop()

    # Printing answer, write your code here
