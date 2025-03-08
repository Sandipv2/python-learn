import random

def game():
    moves = ['rock','paper','scissor']
    
    while True:
        game_over = False
        user_move = input("Enter your move : ")
        if user_move not in 'rps':
            print("Invalid move!!")
            continue
            
        comp_move = random.choice(moves)
        print(f"Computer choose : {comp_move}")
        
        if user_move == 'p' and comp_move == moves[2]:
            print("Computer Won!")
            game_over = True
            
        elif user_move == 'p' and comp_move == moves[0]:
            print('User Won!')
            game_over = True
            
        elif user_move == 'r' and comp_move == moves[1]:
            print("Computer Won!")
            game_over = True
            
        elif user_move == 'r' and comp_move == moves[2]:
            print("User Won!")
            game_over = True
            
        elif user_move == 's' and comp_move == moves[0]:
            print("Computer Won!")
            game_over = True
            
        elif user_move == 's' and comp_move == moves[1]:
            print("User Won!")
            game_over = True
        print("--------------------")
        
        if game_over:
            play_again = input("Continue playing (y/n) : ").lower().strip()
            if play_again == 'n':
                break
            


if __name__ == '__main__':
    game()