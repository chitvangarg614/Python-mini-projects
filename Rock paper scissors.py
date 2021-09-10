import random

def play():
    user=input("\'r\' for rock,\'p\' for paper, '\s\' for scissors ")
    computer= random.choice(['r','s','p'])

    if user== computer:
        print('It\'s a tie between computer and user')

    if is_win(user,computer) :
        print("You won! Computer loses.")   

    else:
        print("Computer wins! You lose") 
 
def is_win(player,opponent):
      if (player=='r'and opponent=='s')or (player=='s' and opponent=='p' )or(player=='p' and opponent=='r'):
          return True
    
play()    