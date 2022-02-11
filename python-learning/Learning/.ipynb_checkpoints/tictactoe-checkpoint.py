import sys

game = [[0, 0, 0], 
        [0, 0, 0],
        [0, 0, 0]]


def game_board(row, column, player):
  try:
    if game[row][column] != 0:
      print('That number is already taken')
    else:
      if player % 2 == 0: iplayer = 1
      else: iplayer = 2
      print(f'Player {iplayer} take your turn!')
      game[row][column] = player
      print("   0  1  2")
      for count, row in enumerate(game):
        print(count, row)
      return game_map
  except:
    print('Something went wrong! --> Something Went Wrong!')
    return False


def main():
  game_board(0, 0, 0)
  p = 0
  while True:
    try:
      r = int(input('Enter Row: '))
      c = int(input('Enter Column: '))
    except TypeError:
     print ('You did not type and int!, very stupid')
     p -= 3
    if p % 2 == 0:
      player = 1
    else:
      player = 2
    print(p)
    p += 3
    try:
      check_draw()
      game_board(r, c, player)
    except:
      print('You Typed something wrong')
      p -= 3


def check_draw():
  p = 0
  for row in game:
    for column in row:
      if column == 0:
        p += 1
      else:
        p += 0
    if p == 9:
      print('Game is draw')
      break


def check_win():
  check = []
  #Horizontal Algo
  for row in game:
    check_win2(row)
  #Vertical algo
  for col in range(len(game[0])):
      check = []
      for row in game:
          check.append(row[col])
      check_win2(check)
  #Diagonal Algo
  rev_diags = []
  diags = []
  cols = list(reversed(range(len(game))))
  rows = range(len(game))
  for col, row in zip(cols, rows):
    rev_diags.append(game[col][row])
    diags.append(game[row][row])
    check_win2(rev_diags)
    check_win2(diags)

def check_win2(lists):
  if lists.count(lists[0]) == len(lists) and lists[0] != 0:
    print(f'Player {lists[0]} won the game')
    exit()


  '''diags = []
  for ix in range(len(game)): 
    diags.append(game[ix][ix])
  diags_rev = []
  for p in list(reversed(range(len(game)))):
    diags_rev.append(game[p][p]) '''

if __name__ == "__main__":
  main()