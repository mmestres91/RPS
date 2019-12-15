import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class HumanPlayer(Player):
    def move(self):
      input("Please enter your move!")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))



class Game:
    def __init__(self, p1, p2):
        self.HumanPlayer = p1
        self.RandomPlayer = p2

    def play_round(self, HumanPlayer, RandomPlayer, player1score, player2score):
        move1 = self.HumanPlayer()
        move2 = self.RandomPlayer.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) is True:
            player1score += 1
            print("Player 1 is the winner!")
        elif beats(move2, move1) is True: 
            player2score += 1
            print("Player 2 is the winner!")
        else:
            print("We have a tie!")
        print(f"Score: Player 1: {player1score} Player 2: {player2score}")
        self.RandomPlayer.learn(move1, move2)
        self.RandomPlayer.learn(move2, move1)     

    def play_game(self):
        player1score = 0 
        player2score = 0
        print("Game start!")
        for round in range(6):
            print(f"Round {round}:")
            self.play_round(HumanPlayer, RandomPlayer, player1score, player2score)
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
    