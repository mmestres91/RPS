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


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.RandomPlayer = p1
        self.RandomPlayer = p2

    def play_round(self, RandomPlayer):
        move1 = self.RandomPlayer.move()
        move2 = self.RandomPlayer.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.RandomPlayer.learn(move1, move2)
        self.RandomPlayer.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round(RandomPlayer)
        print("Game over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()