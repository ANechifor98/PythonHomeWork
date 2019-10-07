from Node import Node
from string import ascii_lowercase

class WordGameNode(Node):
   def __init__(self, name, parent = None):
      # Ensure lowercase letters (no digits or special chars)
      for letter in name:
         assert letter in ascii_lowercase
      self.name = name
      self.parent = parent

   def __str__(self):
      return self.name

   def get_children(self):
      # all one letter mutations of the word
      child_words = []
      for i in range(len(self.name)):
          for c in ascii_lowercase:
              if c != self.name[i]:
                  word = self.name[:i] + c + self.name[i+1:]
                  child_words.append(word)
      
      new_list = []
      for word in child_words:
          k = WordGameNode(word)
          new_list.append(k)
          
      return new_list# Need to return a list of WordGameNode objects.

   def get_path(node):
      path = []
      #Node = self.get_parent()
      
      while node != None:
          path.append(node)
          node = node.get_parent()
          
      return path
      