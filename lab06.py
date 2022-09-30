########################################################################
##
## CS 101 Lab
## Program #5
## Name     Kevin Yu
## Email    ky3fh@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


# import statements

# functions
def get_school(card):
    if card[5] == '1':
        return 'School of Computing and Engineering SCE'
    elif card[5] == '2':
        return 'School of Law'
    elif card[5] == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'

def get_grade(card):
    if card[6] == '1':
        return 'Freshman'
    elif card[6] == '2':
        return 'Sophomore'
    elif card[6] == '3':
        return 'Junior'
    elif card[6] == '4':
        return 'Senior'
    else:
        return 'Invalid Grade'

def character_value(character):
    return ord(character.lower())-97

def get_check_digit(card):
    total = 0
    for pos,i in enumerate(card):
        if i.isalpha():
            total += character_value(i) * (pos+1)
        elif i.isdigit():
            total += int(i) * (pos+1)
    return total%10

def verify_check_digit(card):
    if len(card) != 10:
        return (False, 'The length of the number given must be 10')
    elif card[:5].isalpha() != True:
        invalid_index = 0
        for pos,i in enumerate(card[:5]):
            if i.isalpha() != True:
                print(i)
                invalid_index = pos
        return (False, f'The first 5 characters must be A-Z, the invalid character is at {invalid_index} is {card[invalid_index]}')
    elif card[-4:-1].isdigit() != True:
        invalid_index = 0
        for pos,i in enumerate(card[-4:-1]):
            if i.isdigit() != True:
                invalid_index = pos
        return (False, f'The last 3 characters must be 0-9, the invalid character is at {invalid_index} is {card[invalid_index]}')
    elif card[5] != '1' and card[5] != '2' and card[5] != '3':
        return (False, 'The sixth character must be 1 2 or 3')
    elif card[6] != '1' and card[6] != '2' and card[6] != '3' and card[6] != '4':
        return (False, 'The seventh character must be 1 2 3 or 4')
    elif card[9] != str(get_check_digit(card)):
        return (False, f'Check Digit {card[9]} does not match calculated value {get_check_digit(card)}.')
    else:
        return (True, '')

if __name__ == "__main__":

    # main program
    print(f"{'Linda Hall':^60}")
    print(f"{'Library Card Check':^60}")
    print('='*60)
    lib_card = input('Enter Library Card. Hit Enter to Exit ==> ')
    if verify_check_digit(lib_card)[0] == False:
        print('Library card is invalid.')
        print(verify_check_digit(lib_card)[1])
    else:
        print(f'Library card is valid.\n{get_school(lib_card)}\n{get_grade(lib_card)}')
    
