class Node :
  def __init__(self, message):
    self.message = message
    self.yes_node = None
    self.no_node = None

  def add_message(self, new_message, yes_or_no, old_message ):
    if self.message == old_message :
      if yes_or_no == "oui":
        self.yes_node = Node(new_message)
      else:
        self.no_node = Node(new_message)
    else:
      if self.yes_node != None:
        self.yes_node.add_message(new_message, yes_or_no, old_message )
      if self.no_node != None:
        self.no_node.add_message(new_message, yes_or_no, old_message )

class Discusion_tree:
  def __init__(self):
    self.first_node = None
    self.current_conversation_node = None

  def next_message(self, yes_or_no):
      if self.current_conversation_node == None:
        self.current_conversation_node = self.first_node
        if yes_or_no == "oui":
          if self.current_conversation_node != None:
            self.current_conversation_node = self.first_node.yes_node
        else:
          if self.current_conversation_node != None:
            self.current_conversation_node = self.first_node.no_node
      else:
        if yes_or_no == "oui":
          if self.current_conversation_node != None:
            self.current_conversation_node = self.current_conversation_node.yes_node
        else:
          if self.current_conversation_node != None:
            self.current_conversation_node = self.current_conversation_node.no_node

  def check_yes_or_no(self,yes_or_no):

    if yes_or_no == "oui" or yes_or_no == "non":
      return True
    else:
      return False
  

  def add_message(self, new_message, yes_or_no, old_message ):
    self.first_node.add_message(new_message, yes_or_no, old_message)


