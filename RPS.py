import random

moves = ['rock', 'paper', 'scissors']


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
        move = input("Please enter your move!")
        if move in moves:
            return move
        else: 
            self.move()
        
'''class ReflectPlayer(HumanPlayer):
    def move(self):
        return HumanPlayer.move(self)

class CyclePlayer(Player):
    def move(self):
        return "rock"'''


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    player1score = 0 
    player2score = 0
    def __init__(self, p1, p2):
        self.HumanPlayer = p1
        self.RandomPlayer = p2

    def play_round(self, HumanPlayer, RandomPlayer):
        move1 = self.HumanPlayer.move()
        move2 = self.RandomPlayer.move()
        print(f"Player One: {move1}  Player Two: {move2}")
        if beats(move1, move2) is True:
            self.player1score += 1
        elif beats(move2, move1) is True: 
            self.player2score += 1
        else:
            print("TIE! No points awarded")
        print(f"Score: Player One: {self.player1score} Player Two: {self.player2score}")
        self.RandomPlayer.learn(move1, move2)    

    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round(HumanPlayer, RandomPlayer)
        if self.player1score > self.player2score:
            print("You Won!")
        elif self.player1score == self.player2score:
            print("It's a Final Tie!")
        else:
            print("You Lost!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
    