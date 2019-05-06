#board = [
#  ["_","_","_"],
#  ["_","_","_"],
#  ["_","_","_"]
#]

#print(board)

#print the board in a single line using list comprehension
#def print_board(board):
#  [print(row) for row in board]

def print_board(board):
  for row in board:
   print(row)

#No such thing as int('a')
#code placed in try block so that we handle the errors that get raised without crashing the 
#program.

def convert_selection(selection):
  selection -= 1
  return (selection // 3, selection % 3)

def place_piece(selection, board, player):
  board[selection[0]][selection[1]] = player

#chained comparisons are faster because the middle value only needs to be evaluated once
# raising an error rather than returning None from a function
def select_square():
  selection = int(input("select a sqaure: "))
  if not 1 <= selection <= 9:
    raise ValueError
  return selection

def main():
  board = [["_" for _ in range(3)] for _ in range(3)]
  is_x = True
  while True:
    player = "X" if is_x else "0"
    print_board(board)
    try:
      selection = convert_selection(select_square())
      place_piece(selection, board, player)
    except ValueError:
      print("Sorry, please select a number 1-9")
    is_x = not is_x
    #print_board(board)

#Examples:
#1 => 0,0
#4 => 1,0
#8 => 2,1

#Think floor division + modulo


if __name__ == "__main__":
  main()



#try:
 # selection = int(input("select a sqaure: "))
  #if selection > 9 or selection < 1:
   # print("Sorry, please select a number 1-9")
  #else:
   # print(selection)
#except ValueError:
 # print("Sorry, that's not a number")
