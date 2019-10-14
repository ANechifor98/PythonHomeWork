from heuristic import h

class Node:
   def __init__(self, name, children):
      self.name = name
      self.children = children

   def __str__(self):
      return self.name
      #return "N({0}, {1})".format(self.name, self.children)

   def __repr__(self):
      return str(self)

   def get_children(self):
      return self.children

   # See https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes

   def __eq__(self, other):
      """Override the default Equals behavior"""
      if isinstance(other, self.__class__):
         return self.name == other.name
      return NotImplemented

   def __ne__(self, other):
      """Define a non-equality test"""
      if isinstance(other, self.__class__):
         return not self.__eq__(other)
      return NotImplemented

   def __hash__(self):
      """Override the default hash behavior (that returns the id or the object)"""
      return hash(tuple(sorted(self.__dict__.items())))

class Move:
   def __init__(self, row, col):
      self.row = row
      self.col = col

   def __str__(self):
      return "({0}, {1})".format(self.row, self.col)
SIZE = 3
class Puzzle8Node(Node):
   def __init__(self, position, parent = None):
      # The name will be the square
      # The name should only contain the numbers 1 to 8 and a blank
      sorted_pos = " 123456789ABCDEF" if SIZE == 4 else " 12345678"
      assert "".join(sorted(position)) == sorted_pos
      self.position = position
      self.parent = parent
      self.score = 0
      self.depth = 0

   def __eq__(self, other):
      """Override the default Equals behavior"""
      if other == None:
         return False
      return self.position == other.position

   def __ne__(self, other):
      """Define a non-equality test"""
      return not self.__eq__(other)

   def get_parent(self): return self.parent

   def get_path(self):
      # Follow the parent to create the path
      path = []
      node = self
      while node != None:
         path.append(node)
         node = node.parent
      return path


   def __str__(self):
      s = "|"
      for i in range(SIZE):
         start = i * SIZE
         s += self.position[start:start + SIZE] + "|"
      s += " ({}+{})".format(self.depth, self.score)
      return s

   def __repr__(self):
      return str(self)

   def make_board(self, this_position):
      board = [ ['-' for c in range(SIZE)] for r in range(SIZE)]
      index = 0
      for row in range(SIZE):
         for col in range(SIZE):
            board[row][col] = this_position[index]
            index += 1

      return board
   
   def __hash__(self):
      return hash(self.position)

   def make_name(self, board):
      position = ''
      for row in range(SIZE):
         for col in range(SIZE):
            position += board[row][col]

      return position

   def get_blank(self, board):
      # Find the blank
      for row in range(SIZE):
         for col in range(SIZE):
            if board[row][col] == ' ':
               return Move(row, col)

      return None # Error, this shouldn't happen. 

   def get_children(self):
      # The children are just the moves.
      children = self.get_moves()
      # Add in the parent
      # (that would be myself!)
      for child in children:
         # Record the parent and the depth.
         child.parent = self
         child.depth = child.parent.depth + 1 # Child is one deeper than parent

      return children

   def get_moves(self):
      # The moves depend on the current board position
      # Lets make the board
      board = self.make_board(self.position)
      blank = self.get_blank(board)

      # Now make the moves. There could be 4
      moves = []
      if blank.col != 0:
         # LEFT
         board[blank.row][blank.col-1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col-1]
         # Convert board to a name and append to moves
         moves.append(self.make_name(board))
         # swap back to undo the move
         board[blank.row][blank.col-1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col-1]
      if blank.row != 0: # Can't move up if already at the top
         # UP
         # swap blank and position above it
         board[blank.row-1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row-1][blank.col]
         # Convert board to a name and append to moves
         moves.append(self.make_name(board))
         board[blank.row-1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row-1][blank.col]
      if blank.col != SIZE-1:
         # RIGHT
         board[blank.row][blank.col+1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col+1]
         # Convert board to a name and append to moves
         moves.append(self.make_name(board))
         board[blank.row][blank.col+1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col+1]
      if blank.row != SIZE - 1:
         # Down
         board[blank.row+1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row+1][blank.col]
         # Convert board to a name and append to moves
         moves.append(self.make_name(board))
         board[blank.row+1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row+1][blank.col]

      return [Puzzle8Node(move) for move in moves]
   
def greedy(start, goal):
   # We will start here, so the list of nodes to do is the start
   start.score = h(start, goal)
   done = False
   num_searches = 0
   next = start
   while not done:
      # Find the next position
      num_searches += 1

      if next == goal:
         done = True
      else:
         # Keep searching.
         # What searching. This is a greedy search. Just try the best child.
         children = next.get_children()
         # Get the score for each of these children
         for child in children:
            child.score = h(child,goal)

         # Best child ...
         best = min(children, key = lambda x : x.score)
         if best.score < next.score:
            next = best # we improved, start from here.
         else:
            done = True # Our move made no progress ... hang our head in shame and give up.

   return num_searches, next

if __name__ == "__main__":
    start = Puzzle8Node("25 671483")
    goal = Puzzle8Node("625781 43")
    
    print(greedy(start, goal))
    print(h(start, goal))
