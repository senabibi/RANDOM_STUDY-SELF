import random

def game():
    user=input("'r' for rock 's' for scissors and 'p' for paper\n")
    computer=random.choice(['r','s','p'])
    if user==computer:
        return "it\'s tie"
    if is_win(user,computer):
        return "you won!"
    
    return "you lost!"
def is_win(player,across):
    if (player=='r'and across=='s') or (player=='s' and across=='p')\
        or(player=='p' and across=='r'):
        return True
    return False    

print(game())