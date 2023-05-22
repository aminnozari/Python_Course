import random
class Game:
    def __init__(self):
        self.game_items = ['rock', 'paper', 'scissors']
        self.score_board = {'user': 0, 'computer': 0}

    def get_user_choice(self):
        while True:
            user_choice = input('Please enter your choice (rock/paper/scissors), or "q" to quit: ').lower()
            if user_choice == 'q':
                return None
            elif user_choice not in self.game_items:
                print('Invalid input, please try again.')
            else:
                return user_choice

    def play_round(self, user_choice):
        computer_choice = random.choice(self.game_items)
        print(f"User choice: {user_choice.title()}, Computer choice: {computer_choice.title()}")
        if computer_choice == user_choice:
            print('Draw!')
        elif (computer_choice == 'rock' and user_choice == 'scissors') or \
             (computer_choice == 'paper' and user_choice == 'rock') or \
             (computer_choice == 'scissors' and user_choice == 'paper'):
            self.score_board['computer'] += 1
            print('Computer wins!')
        else:
            self.score_board['user'] += 1
            print('Congratulations, You win!')

    def play_game(self):
        while True:
            print(f"\nScore: User {self.score_board['user']} - Computer {self.score_board['computer']}")
            user_choice = self.get_user_choice()
            if user_choice is None:
                break
            self.play_round(user_choice)

        print(f"\nFinal Score: User {self.score_board['user']} - Computer {self.score_board['computer']}")
        if self.score_board['computer'] > self.score_board['user']:
            print('Computer wins the game.')
        elif self.score_board['computer'] < self.score_board['user']:
            print('Congratulations, You win the game!')
        else:
            print('The game is a draw.')

game = Game()
game.play_game()