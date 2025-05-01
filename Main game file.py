# This looks ugly, but at this point I have
# used functions from all of these here so best leave it be
# but God I should have used my brain a bit better - 30/07/2024
# There is hope for improvement...I think - 02/09/2024

# It is done. Aparently I just didn't fully understand modules
# But a true G in college gave my a massive help on it
# Thanks Guilherme, it was a nightmare, but we did it

import sys
from main_game_lib import *
from time import sleep
import random  #| Will be used on the future

#*DONE Need to start using seeds
#*DONE Remove a bunch of returns that are not needed
#*DONE Add a enemy generator
#TODO Spell check the whole game, cuz my english sucks

#TODO Write all enemy names with proper captalization to use on attack messages
#TODO and use .upper() to put all on caps for displaying in combat
#TODO Trim out the repeated functions
#TODO Add lists containing all the in-game debuffs and buffs for relics, skills and items

#*DONE Make luck actually meaningful by including it in a bunch of random checks
#*DONE Include debuff damage modifiers and duration modifiers in the calculations for debuffs all over
#*DONE Change dodge buff name to Speed+
#*DONE Change crit buff name to Precision+
#TODO Check through documentation and if any is missing add it

# Main program

game_seed=random.getrandbits(50)
game_seed=3146169615354 #*debug
random.seed(game_seed)

size=40 # For lines, centering and such
class_list=['The Knight','The Thief','The Beast']
main_menu_options=['Start Game','Options','Credits','Exit Game']
persistent_itens_main=persistent_item_sheet()
enemy_table_load=level_1_enemy_list()
mini_boss_table_load=level_1_miniboss_list()
acquirable_skills_load=skill_data_sheet()
basic_item_list=item_sheet()
special_relic_list=event_relics_sheet()
cursed_relics_list=cursed_relics()
shop_contents={}
event_itens={}
enemies_to_be_fought={}

(
 shop_contents,
 event_itens
)=get_random_itens(
 basic_item_list,
 persistent_itens_main,
 acquirable_skills_load,
 shop_contents,
 event_itens,
 special_relic_list,
 cursed_relics_list
)

(
 enemies_to_be_fought
)=get_random_enemies(
 enemy_table_load,
 mini_boss_table_load,
 enemies_to_be_fought,
 #//basic_item_list
)

'''(
 shop_contents
)=get_random_itens( #*Debug
 basic_item_list,
 persistent_itens_main,
 acquirable_skills_load,
 shop_contents
)'''

# Game starts here
os.system('cls')
main_file_menu_displays.start_up_screen()

main_file_menu_displays.display('TERMINAL DUNGEON',size)
press_enter_to('Continue',size)


while True:
 os.system('cls')
 main_file_menu_displays.display('MAIN MENU',size)
 main_file_menu_displays.option_generator(main_menu_options)

 while True:
  player_option_main_menu=integer_check('Your input: ',size)
  if player_option_main_menu>=1 and player_option_main_menu<=len(main_menu_options):
   break
  print('Choose a Valid Option')

 if player_option_main_menu==1:
  break

 elif player_option_main_menu==2:
  # This will be fun to figure out in the future - 03/07/2024
  main_file_menu_displays.display('WORK IN PROGRESS',size)
  press_enter_to('Return',size)

 elif player_option_main_menu==3:
  main_file_menu_displays.display_credits(size)
  press_enter_to('Return',size)

 elif player_option_main_menu==4:
  os.system('cls')
  display('Exiting Game',size)
  sleep(2)
  os.system('cls')
  sys.exit()

os.system('cls')

while True:
 main_file_menu_displays.display('WHO ARE YOU?',size)
 main_file_menu_displays.option_generator(class_list)

 while True:
  player_option_caracter=integer_check('Your choice: ',size)
  if player_option_caracter>=1 and player_option_caracter<=len(class_list):
   break
  print('Choose a Valid Option')

 # Loads the stats of The Knight
 if player_option_caracter==1:
  main_file_menu_displays.display('CARACTER 1',size)

 elif player_option_caracter==2:
  main_file_menu_displays.display('YOU ARE A THIEF',size)
  current_stats=thief_base_load()

 # Loads the stats of The Beast 
 elif player_option_caracter==3:
  main_file_menu_displays.display('CARACTER 3',size)


 #? Should this be debug only?
 '''current_stats['inventory'].append(basic_item_list[4])   #* Debug, all 4
 current_stats['inventory'].append(basic_item_list[5])
 current_stats['inventory'].append(basic_item_list[1])
 current_stats['inventory'].append(basic_item_list[2])
 current_stats['skill_list'].append(acquirable_skills_load[0])'''  #* Debug
 #current_stats['skill_list'].append(acquirable_skills_load[1])
 #current_stats['skill_list'].append(acquirable_skills_load[2])

 current_level=1 # Used as base modifier for events and prices

 while True: #* Debug
  main_file_menu_displays.display("SELECT EVENT TO TEST...\n!DON'T FORGET IT STARTS AT ZERO\nCHECK RANDOM EVENT FUNCTION FOR REFERENCE",size)
  print(f'CURRENT SEED: {game_seed}')
  player_room_choice=integer_check('Which way should you go? ',size)

  
   #current_stats,
   #persistent_itens_main,
   #acquirable_skills_load
  event_pool(
             player_stats=current_stats,
             random_event_choice=player_room_choice,
             format_size=size,
             level_modifier=current_level,
             enemy_table=enemies_to_be_fought,
             shop_contents=shop_contents,
             event_itens=event_itens
             )

  '''(
   shop_contents,
   event_itens
  )=get_random_itens( #* Debug
   basic_item_list,
   persistent_itens_main,
   acquirable_skills_load,
   shop_contents,
   event_itens,
   special_relic_list,
   cursed_relics_list,
   True
  )'''
  
  #for relic in range(len(shop_contents['shop_relics'])-1,-1,-1): #* debug
   #shop_contents['shop_relics'].pop(relic)
  
  if current_stats['player_is_alive'] is False:
   break

 print('You ded boi')
