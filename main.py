import random

def play():
  player = input("What's your choice? Pick R, P, or S: ")
  player = player.lower()

  cpu = random.choice(['r', 'p', 's'])

  if player == cpu:
    return "That was a tie. You have both chosen {}.", format(cpu)

  if win(player, cpu):
    return "You win. You have chosen {}, and the computer has chosen {}.",format(user, computer)
  return "You lose. You chose {}, and your opponent chose {}.", format(user, computer)

def win(player, opponent):
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
    return True
  return False

play()
