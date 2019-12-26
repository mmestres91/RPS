import random

moves = ['rock', 'paper', 'scissors']
players = ["1", "2", "3", "4"]


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
        if Game.play_round.has_been_Called is False:
            return random.choice(moves)
        else:
            return self.my_move


class CyclePlayer(Player):
    def move(self):
        if Game.play_round.has_been_Called is False:
            return random.choice(moves)
        elif self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    player1score = 0
    player2score = 0

    def __init__(self, p1, p2):
        self.HumanPlayer = p1
        self.Player = p2

    def play_round(self, HumanPlayer, Player):
        move1 = self.HumanPlayer.move()
        move2 = self.Player.move()
        print(f"Player One: {move1}  Player Two: {move2}")
        if beats(move1, move2) is True:
            self.player1score += 1
        elif beats(move2, move1) is True:
            self.player2score += 1
        else:
            print("TIE! No points awarded")
        print(f"Score: Player One: {self.player1score}")
        print(f"Score: Player Two: {self.player2score}")
        self.Player.learn(move1, move2)
        self.Player.learn(move2, move1)
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


def game_start():
    # Create input and ask Human Player what CPU they want to play against
    print("Welcome to Rock Paper Scissors!")
    print("Choose your Competition:")
    print("Press 1 for Dummy Player")
    print("Press 2 for Random Player")
    print("Press 3 for Reflect Player")
    print("Press 4 for Cycle Player")
    game_input()


def game_input():
    playerselect = input("Selection:")
    if playerselect == "1":
        game = Game(HumanPlayer(), Player())
    elif playerselect == "2":
        game = Game(HumanPlayer(), RandomPlayer())
    elif playerselect == "3":
        game = Game(HumanPlayer(), ReflectPlayer())
    elif playerselect == "4":
        game = Game(HumanPlayer(), CyclePlayer())
    else:
        game_input()
    game.play_game()


if __name__ == '__main__':
    game_start()
