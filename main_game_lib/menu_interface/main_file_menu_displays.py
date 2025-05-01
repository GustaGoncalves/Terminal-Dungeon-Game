from time import sleep
import os

def print_line(line_size: int):
 """
 A simple print for lines based on size

 line_size: Size of the line
 """

 print('-'*line_size)


def display(message: str,size_formatting: int):
 """
 Prints on screen the main menu.

 message: Message used on the menu

 size_formatting: Size of lines, centering and other formating aspects
 """
 
 print_line(size_formatting)
 print(message.center(size_formatting))
 print_line(size_formatting)


def option_generator(option_list: list):
 """
 For generating the options of a menu

 option_list: the list of options that will be used, must be a list
 """

 for i in range(0,len(option_list)):
  print(f'[{i+1}] {option_list[i]}')


def start_up_screen():
 """
 This is the first thing that should appear once game is "booted"
 """

 size=40
 delay=0.3

 print_line(size)
 sleep(delay)
 print('WELCOME'.center(size))
 sleep(delay)
 print_line(size)
 sleep(delay)

 sleep(2-delay)

 os.system('cls')


def display_credits(size_credits: int):
 """
 Shows the credits of the game when prompted
 by the player on the main menu

 size_credits: Size for lines, centering and other formating aspects
 """

 display('CREDITS',size_credits)
 sleep(0.5)
 print('   A game by')
 sleep(1)
 print(f'{'Kryon':>37}')
 print_line(size_credits)
 sleep(1)
 print('From my terminal'.center(size_credits))
 sleep(1)
 print('To yours'.center(size_credits))
 sleep(1)
 print_line(size_credits)


def integer_check(message_for_user,size_check: int):
 """
 Puts a player input through a check to ensure it's a integer
 message_for_user: the message for the user
 size: Size used for formating and line generation
 """
 while True:
  try:
   user_input=int(input(message_for_user))

  except ValueError:
   print('Input MUST be a number AND integer. Ex: 1,2,3...')



   # Y'know, just in case it happens, somehow
  except KeyboardInterrupt:
   print('User stopped the process')
   break
  


  #Since I'm still learning, I have no clue what other problems could happen here so
  except Exception as error:
   print('Something unexpected happened')
   display('ERROR LOG',size_check)
   print(error)
   print_line(size_check)

  else:
   return user_input


def press_enter_to(message_to,size):
 """
 Prompts the user to press the 'Enter' key to move on to the next screen
 Size: the size used to center the message
 Message_to: Informs the user the effect of pressing enter
 """
 print()
 print(f'Press Enter to {message_to}'.center(size))
 input()