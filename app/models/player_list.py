from app.models.player import *

player_1 = Player("Martin", ["Rock" "Paper", "Scissors"])
player_2 = Player("Uthred", ["Paper", "Paper", "Scissors"])
players = [player_1, player_2]

if ((player1 == "rock" or player1 == "paper" or player1 == "scissors") and (player2 == "rock" or player2 == "paper" or player2 == "scissors")):
    if (player1 == 'rock' and player2 == 'rock'):
        return "Draw"
    elif (player1 == 'paper' and player2 == 'paper'):
        return "Draw"
    elif (player1 == 'scissors' and player2 == 'scissors'):
        return "Draw"
    elif (player1 == 'paper' and player2 == 'rock'):
        return "Player 1 wins!"
    elif (player1 == 'rock' and player2 == 'scissors'):
        return "Player 1 wins!"
    elif (player1 == 'scissors' and player2 == 'paper'):
        return "Player 1 wins!"
    elif (player1 == 'rock' and player2 == 'paper'):
        return "Player 2 wins!"
    elif (player1 == 'scissors' and player2 == 'rock'):
        return "Player 2 wins!"
    elif (player1 == 'paper' and player2 == 'scissors'):
        return "Player 2 wins!"
else:
    print("Restart Game")