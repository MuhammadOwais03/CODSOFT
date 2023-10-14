
import random
import os
class Game:
    def __init__(self):
        self.components = ["ROCK", "PAPER", "SCISSOR"]

    def ComputerTurns(self):
        return random.choice(self.components)



    def check_for_game_result(self, player, computer):

        print(f"PLAYER CHOICE IS '{player}'{' '*10}||{' '*10}COMPUTER CHOICE '{computer}'")
        if (computer == "ROCK" and player == "SCISSOR") or  (computer == "SCISSOR" and player == "PAPER") or  (computer == "PAPER" and player == "ROCK"):
            return "computer"
        elif (computer == "SCISSOR" and player == "ROCK") or  (computer == "PAPER" and player == "SCISSOR") or  (computer == "ROCK" and player == "PAPER"):
            return "player"
        else:
            return "draw"

def display():
    print("**************SCORE**************")
    print("Computer", score['computer'],end='')
    print(' '*14 ,"Player", score['player'])
    print()

if __name__ == "__main__":
    obj = Game()
    print("WELCOME TO THE GAME")
    score = {"computer": 0, "player": 0}
    continue_ = True
    while continue_:
        os.system('cls')
        display()

        print("**************ROCK PAPER AND SCISSOR**************")
        while True:
            try:
                player_turn = input("Enter Your Choice: ").upper()
                os.system('cls')
                if player_turn not in obj.components:
                    raise ValueError("Invalid choice. Available choices are: {}".format(obj.components))
                else:
                    break
            except ValueError as e:
                print(e)
                continue

        computer = obj.ComputerTurns()
        v = obj.check_for_game_result(player_turn, computer)
        print()
        if v == 'computer':
            score['computer'] += 1
            print("COMPUTER WINS")
            print()
        elif v == 'player':
            score['player'] += 1
            print("PLAYER WINS")
            print()
        else:
            print("Game Draw")
            print()
        display()
        continue_ = input("DO YOU WANT TO CONTINUE[y/N]: ").upper()
        if continue_ == 'N':
            continue_ = False
