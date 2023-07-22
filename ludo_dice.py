'''' This is a simple ludo diice game for playing '''
import random

# this section contain user registation:

gamer_name =input('Please Enter Your name  for game registration: >>>>> ')

def roll_dice():
    return random.randint(1,6)
# validatde user guess
def validate_guess(user_choice):
    if len(user_choice) != 1:
        print('Please Enter Only Single Letter')
        return False
    elif not user_choice.isalpha():
        print('Please Enter a Letter')
        return False
    elif user_choice.lower() not in ['y','n']:
        print('please enter only "y" or "n"')
        return False
    else:
        return True

# welcome game note 
def maingame():
    print(f'<><><><><> WELCOME TO LUDO DICE GAME <> <> <> \n  -------- {gamer_name}--------')
    while True:
        user_choice = input('Do you want to roll the ludo dice? >> y/n \n Waiting for your choice: ----').lower()
        if not validate_guess(user_choice):
            continue
    
        if user_choice == 'y':
            dice_num =roll_dice()
            if dice_num == 6:
                print(f'congratulations you got {dice_num} you get two more chance to run the dice..........')
                user_choice2 = input('Do you want to roll the ludo dice? >> y/n \n Waiting for your choice: ----').lower()
                if not validate_guess(user_choice2):
                    continue
                if user_choice2 == 'y':
                    dice_num2 =roll_dice()
                    print(f'this is your second chance and you get {dice_num2}')
                        
                else:
                    print(f'Thank you for your concern {gamer_name} and you get {dice_num}')
                    break

            else:
                print(f'thank you for playing this game {gamer_name}  you got {dice_num}')
                break
        else:
            print(f'Thank you for your concern {gamer_name}')
            break
    

maingame()