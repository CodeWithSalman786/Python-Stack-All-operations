# CREATING STACK CLASS.
class Stack:
    def __init__(self):
        self.items = []
    # CHECKING IF STACK IS EMPTY OR NOT.
    def is_Empty(self):
        return len(self.items) == 0
    # PUSH FUNCTION TO ADD ELEMENT IN THE STACK.
    def push(self, item):
        self.items.append(item)
    # POP FUNCTION TO REMOVE ELEMENT FROM THE STACK.
    def pop(self):
        if not self.is_Empty():
            self.items.pop()
        else:
            print("Error! Stack is Empty")
    # PEEP FUNCTION TO FETCH LAST ELEMENT WITHOUT EMPTYING STACK.
    def peep(self):
        if not self.is_Empty():
            return self.items[-1]
        else:
            print("Error! Stack is Empty")
    # CHECKING THE SIZE OF THE STACK.
    def size(self):
        return len(self.items)

# MAIN CODE OR DRIVER CODE.
# The below first line is optional.
if __name__ == '__main__':
    # CREATING THE OBJECT FOR THE STACK CLASS.
    # U CAN GIVE ANY NAME TO THE OBJECT.
    obj = Stack()
    while True:
        print("OPERATIONS ON STACK:")
        print("1 = Push")
        print("2 = Pop")
        print("3 = Peek")
        print("4 = Size")
        print("5 = Display Stack")
        # GOING TO TAKE INPUT FROM THE USER.
        selection = int(input("Make any One selection from above: "))
        if selection == 1:
            element = int(input("Enter the Element: "))
            obj.push(element)
        elif selection == 2:
            obj.pop()
        elif selection == 3:
            obj.peep()
        elif selection == 4:
            obj.size()
        elif selection == 5:
            print(obj.items)
