class node:
   def __init__(self,data=None):
      self.data=data
      self.next=None

class linked_list:
   def __init__(self):
      self.head = node() # acts as placeholder for first element in linked list 

   def append(self,data): # append new node at end of linked list 
      new_node = node(data)
      current_node = self.head # pointer to head node
      while current_node.next!=None:
         current_node = current_node.next
      current_node.next = new_node

   def length(self):
      current_node = self.head
      total = 0
      while current_node.next!=None:
         total+=1
         current_node = current_node.next
      return total

   def display(self):
      elements = []
      current_node = self.head
      while current_node.next!=None:
         current_node = current_node.next
         elements.append(current_node.data)
      print(elements)

   def get(self,index):
      if index>=self.length():
         print("Bad!")
      current_index = 0
      current_node = self.head
      while current_node.next!=None:
         current_node = current_node.next
         if current_index == index: return current_node.data
         current_index+=1

   def erase(self,index):
      if index>=self.length():
         print("Bad!")
      current_index = 0
      current_node = self.head
    
      while current_node.next!=None:
         last_node = current_node
         current_node = current_node.next
         if current_index==index:
            last_node.next = current_node.next
            return
         current_index+=1 

   def reverse_iterative(self):
      prev = None
      cur = self.head
      while cur: # while cur is not None
         nxt = cur.next
         cur.next = prev
         prev = cur
         cur = nxt
      self.head = prev

my_list = linked_list()

# my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

print(my_list.get(2))

my_list.erase(2)

my_list.display()

my_list.reverse_iterative()

my_list.display()
