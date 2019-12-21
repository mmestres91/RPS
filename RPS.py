import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = their_move
        self.their_move = their_move
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
            return self.move()


class ReflectPlayer(Player):
    def move(self):
        return random.choice(moves)

    def reflectmove(self):
        return self.my_move


class CyclePlayer(Player):
    def move(self):
        return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    player1score = 0
    player2score = 0

    def __init__(self, p1, p4):
        self.HumanPlayer = p1
        #self.Player = p2
        #self.RandomPlayer = p3
        self.ReflectPlayer = p4
        #self.CyclePlayer = p5

    def play_round(self, HumanPlayer, ReflectPlayer):
        move1 = self.HumanPlayer.move()
        #move2 = self.RandomPlayer.move()
        if self.play_round.has_been_Called is False:
            move2 = self.ReflectPlayer.move()
        else:
            move2 = self.ReflectPlayer.reflectmove()
        print(f"Player One: {move1}  Player Two: {move2}")
        if beats(move1, move2) is True:
            self.player1score += 1
        elif beats(move2, move1) is True:
            self.player2score += 1
        else:
            print("TIE! No points awarded")
        print(f"Score: Player One: {self.player1score}")
        print(f"Score: Player Two: {self.player2score}")
        #self.RandomPlayer.learn(move1, move2)
        self.ReflectPlayer.learn(move1, move2)
        self.ReflectPlayer.learn(move2, move1)
        Game.play_round.has_been_Called = True

    play_round.has_been_Called = False

    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round(HumanPlayer, ReflectPlayer)
        if self.player1score > self.player2score:
            print("You Won!")
        elif self.player1score == self.player2score:
            print("It's a Final Tie!")
        else:
            print("You Lost!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
    
