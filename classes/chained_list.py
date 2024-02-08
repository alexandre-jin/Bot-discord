class Node :
  def __init__(self, data): # un élément 
    self.data = data
    self.next_node = None

class Chained_list:
  def __init__(self):
    self.first_node = None

  def append(self,data):

    if self.first_node == None:
      self.first_node = Node(data)
      return

    current_node = self.first_node
    while current_node.next_node != None:
      current_node = current_node.next_node

    new_node = Node(data)
    current_node.next_node = new_node

  def len(self):
    i=0
    current_node = self.first_node
    while current_node!= None:
      current_node = current_node.next_node
      i+=1    
    return i

  def search(self, value):
    current_node = self.first_node
    while current_node != None:
      if current_node.data == value:
        return True
      current_node = current_node.next_node
    return False

  def get_commands_with_userId(self, id):
    current_node = self.first_node
    commands_with_userId = ""
    while current_node!= None:
      if current_node.data[0] == id:
        commands_with_userId += current_node.data[1] + " "
      current_node = current_node.next_node
    return commands_with_userId


  def last_index(self, id):
    current_node = self.first_node
    last_data = None
    while current_node!= None:
      if current_node.data[0] == id:
        last_data = current_node.data
      current_node = current_node.next_node
    return last_data
  

  def clean(self):
    self.first_node = None

  
  # def insert(self, value, id):

  #   current_node = self.first_node
  #   i = 0
  #   while i < id:
  #     current_node = current_node.next_node
  #     i+=1

  #   new_node = Node(value)
  #   new_node.next_node = current_node.next_node
  #   current_node.next_node = new_node

 

# L=Chained_list()
# L.append(5)
# L.append(6)
# L.append(8)
# L.append(10)
# L.append(1)
# L.append(10)
# L.append(1)
# print(L.get_all())
# print(L.len())
# print(L.search(10))
# print(L.get(2))
# print(L.last_index())
# L.clean()
# print(L.get_all())