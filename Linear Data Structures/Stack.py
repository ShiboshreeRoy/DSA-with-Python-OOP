class  Stack:
    def __init__(self) :
      self.Stack = []

    #add signle item in stack 
    def Push(self,item):
       self.Stack.append(item)
       #print("Stack : ",self.Stack)

    #remove single item  in stack
    def Pop(self,item):
       self.Stack.remove(item)
       #print("Stack :", self.Stack)
    
     # Push a single item onto the stack
    def push(self, item):
        self.stack.append(item)
        print("Stack:", self.stack)

    
    # Update items
    def update_item(self, old_item, new_item):
        if old_item in self.Stack:
            index = self.Stack.index(old_item)  # Find the index of the old item
            self.Stack[index] = new_item  # Replace the old item with the new one
            print("Updated Stack:", self.Stack)
        else:
            raise ValueError("Item not found in stack")


    #Add multiple items  in Stack
    def  Stack_All(self,item):
      if isinstance(item,list):
          self.Stack.extend(item)
          #print("Add multiple  items in Stack : ",self.Stack)
      else:
         raise ValueError("Input  Must be a  List ..")
      
    #check if  stack   

    def is_empty(self):
      return len(self.Stack) == 0
    
    #stack size
    def  size(self):
       return  len(self.Stack)
   

    #show  all item  in stack
    def  Display(self):
       return self.Stack
    

my_stack = Stack()

my_stack.Push("A")
my_stack.Push("B")
my_stack.Push("c")
my_stack.Pop('B')

my_stack.Stack_All(["cpoznek@gmail.com",
    "ealuger@gmail.com",
    "a.r._consulting@outlook.com",
    "1610mgnt@gmail.com",
    "www.diamondfoodenterprises@gmail.com",
    "field+-+markwfield@gmail.com",
    "parrish@gmail.com",
    "emily@gograndplan.com",
    "7y29re57@duck.com",
    "Bangladesh",
    "India",
    "China",
    "USA"
    ])



print("If Stack has  no items : ",my_stack.is_empty())
print("Stack :",my_stack.Display())
print("Stack Size :",my_stack.size())

try:
   my_stack.update_item("Bangladesh", 50)
except ValueError as e:
   print(e)
