from time import sleep

# Same functions used in the menu
# Copied them in here to not move the interface objects too down the ladder
# Should not be imported anywhere else
# Nvm ended up using it somewhere else, although not in the main file - 15/08/2024
def print_line(line_sizing):
 
 print('-'*line_sizing)



# Same as previous, copied from a module higher up the chain
# As to not move it down excessively
def display(message,size_formatting):

 print_line(size_formatting)
 print(message.center(size_formatting))
 print_line(size_formatting)



# Same as previous two
# This is all done to avoid circular imports...I think
def integer_check(message_for_user='',size_check=40):

 while True:
  try:
   user_input=int(input(message_for_user))


  except ValueError:
   print('Input MUST be a number AND integer. Ex: 1,2,3...')



  except KeyboardInterrupt:     # Y'know, just in case it happens, somehow. In hindsight, might remove it
   print('User stopped the process')
   break
   


  except Exception as error:    # Since I'm still learning, I have no clue what other problems could happen here so just in case
   print('Something unexpected happened')
   display('ERROR LOG',size_check)
   print(error)
   print_line(size_check)

  else:
   return user_input
  


#*DONE Add Rage and Rush buffs unicode icons
#TODO Update documentation

def combat_screen(
  player_stats: dict,
  enemy_stats: dict,
  format_size: int,
  current_status_player: list,
  current_status_enemy: list,
  player_attack_bonus: int,
  player_defense_bonus: int,
  player_dodge_bonus: int,
  enemy_attack_bonus: int,
  enemy_defense_bonus: int,
  turn_count_display: int,
  player_has_rage: bool,
  player_has_rush: bool,
  enemy_dodge_bonus: int,
  player_crit_bonus: int,
  enemy_has_rush: bool,
  enemy_crit_bonus: int
):
 """
 This generates the combat screen containing player and enemy health along with the options available for dealing with the encounter

 player_stats: Self explanatory, it's the player's current stats

 enemy_stats: random enemy_stats pulled from the sheet acording to the encounter

 format_size: size for formatting spaces and lines

 current_status_player: current player status, changes if afflicted by a debuff

 current_status_enemy: current enemy status, changes if afflicted by a debuff

 player_attack_bonus: current buffs/modifiers applied to player attack

 player_defense_bonus: current buffs/modifiers applied to player attack

 enemy_attack_bonus: current buffs/modifiers applied to enemy attack

 enemy_defense_bonus: current buffs/modifiers applied to enemy defense

 turn_count_display: used to display the current turn count to the player

 player_has_rage: Flag for rage buff

 player_has_rush: Flag for rush buff
 """

 # This is just barely readable for anyone besides me
 # As insane as it looks I actually can confortably say what this does
 # I made it, so I should know - 05/07/2024
 # Code has overall improved and is considerably more readable now. Yay :D - 15/08/2024

 #| ANSI coloring for text
 colors={
  'red':'\033[31m',
  'green':'\033[32m',
  'cyan':'\033[36m',
  'white':'\033[37m',
  'end':'\033[m'
 }
 color_value_hp_player='white'
 color_value_hp_enemy='white'

 if player_stats['hp_current']<=(player_stats['hp_max']*(30/100)):
  color_value_hp_player='red'

 print(f'{f'TURN {turn_count_display}':^{format_size}}')
 print_line(format_size)

 # Making the display put the menu on the middle with player and enemy status on the corners
 # Is nothing short of a stroke of genius
 # It looks ludicrously(?) good
 # Thank you so much for the suggestion Dan, you rock - 14/08/2024

 #*DONE Add icon for slow debuff

 # Player display
 #TODO Add character icon to the display
 print('YOU')
 print('STATUS:',end=' ')

 if len(current_status_player)<=0:
  print('Ø',end='')

 else:

  if 'BURN' in current_status_player:
   print('♨',end=' ')

  if 'WOUNDED' in current_status_player:
   print('🗡',end=' ')

  if 'POISON' in current_status_player:
   print('☠',end=' ')

  if 'WEAK' in current_status_player:
   print('☹',end=' ')

  if 'FROSTBITE' in current_status_player:
   print('❄',end=' ')

  if 'SILENCE' in current_status_player:
   print('🤫',end=' ')

  if 'SLOW' in current_status_player:
   print('🐌',end=' ')

 print(f'\n{f'HP:{colors[color_value_hp_player]} {player_stats['hp_current']}{colors['end']} / {player_stats['hp_max']}'}')

 # Display for player buff/debuff on stats
 # Dan you genius, using UNICODE symbols is an awesome idea - 15/08/2024

 #*DONE refactor the 'print('|')'
 #*DONE It should be in the icon print

 if player_attack_bonus>0:
  print(f'|{colors['green']}⚔ ↑{colors['end']}',end='')

 elif player_attack_bonus<0:
  print(f'|{colors['red']}⚔ ↓{colors['end']}',end='')

 #//if player_attack_bonus>0 or player_attack_bonus<0:  #| Prints the bar only if player has been buffed or debuffed
  #//print('|',end='')

 if player_defense_bonus>0:
  #print('|',end='')
  print(f'{colors['green']}⛨ ↑{colors['end']}',end='')

 elif player_defense_bonus<0:
  #print('|',end='')
  print(f'{colors['red']}⛨ ↓{colors['end']}',end='')


 if player_dodge_bonus>0:
  #print('|',end='')
  print(f'{colors['green']}🦶 ↑{colors['end']}',end='')

 elif player_dodge_bonus<0:
  #print('|',end='')
  print(f'{colors['red']}🦶 ↓{colors['end']}',end='')


 if player_crit_bonus>0:
  #print('|',end='')
  print(f'{colors['green']}◎ ↑{colors['end']}',end='')

 if player_crit_bonus<0:
  #print('|',end='')
  print(f'{colors['red']}◎ ↓{colors['end']}',end='')


 if player_has_rage:
  #print('|',end='')

  #*DONE Emoji is placeholder, replace with better one
  print(f'{colors['red']}✦{colors['end']}',end='')

 if player_has_rush:
  #print('|',end='')

  #*DONE Emoji is placeholder, replace with better one
  #*DONE New one did not translate well to terminal, needs replacing
  print(f'{colors['cyan']}💨{colors['end']}',end='')


 if player_crit_bonus!=0 or player_attack_bonus!=0 or player_defense_bonus!=0 or player_has_rage or player_has_rush or player_dodge_bonus!=0: 
  print() #* debug
 #//if player_attack_bonus!=0 or player_defense_bonus!=0:  # Skips line if a buff/debuff is active
  #//print()

 print(f'ATK BONUS: {player_attack_bonus}')  #* Debug
 print(f'DEF BONUS: {player_defense_bonus}') #* Debug

 option_set=['Attack', 'Block', 'Items','Skills']
 for i in range(0,len(option_set)):
  print(f'{f'[{i+1}] {option_set[i]}':^{(format_size)}}')


 #| Enemy display starts here
 print(f'{enemy_stats['enemy_name']:>{format_size}}')

 if len(current_status_enemy)<=0:
  print(f'{f'STATUS: ':>{format_size-1}}',end='')

 #! Due to how text aligning with print commands work
 #! It is necessary to do this rather weird UI solution
 #! It subtracts from the value used, the number of caracters in the commands (i.e. two)
 #! Multiplied by the amount of debuffs - 21/08/2024
 elif len(current_status_enemy)>0:
  print(f'{f'STATUS: ':>{format_size-(len(current_status_enemy)*2)}}',end='')

 if len(current_status_enemy)<=0:
  print(f'{f'Ø'}',end='')

 else:
  if 'BURN' in current_status_enemy:
   print(f'♨',end=' ')

  if 'WOUNDED' in current_status_enemy:
   print('🗡',end=' ')

  if 'POISON' in current_status_enemy:
   print('☠',end=' ')

  if 'WEAK' in current_status_enemy:
   print('☹',end=' ')

  if 'FROSTBITE' in current_status_enemy:
   print('❄',end=' ')

  if 'SILENCE' in current_status_enemy:
   print('🤫',end=' ')

  if 'SLOW' in current_status_enemy:
   print('🐌',end=' ')


 if enemy_stats['hp_current']<=(enemy_stats['hp_max']*(30/100)):
  color_value_hp_enemy='red'

 #! The ANSI codes add 8 chars to the string
 #! So just add 8 to format value, JUST for this  
 print(f'\n{f'HP: {colors[color_value_hp_enemy]}{enemy_stats['hp_current']}{colors['end']} / {enemy_stats['hp_max']}':>{format_size+8}}')

 #! One of the, if not the most bizarre UI adjust solutions
 #! I just don't know yet a better way to do this
 screen_adjust=0

 if enemy_attack_bonus!=0:   #|// Increment by 4 here to acount for the bar print
  screen_adjust+=3

 if enemy_defense_bonus!=0:
  screen_adjust+=3

 if enemy_dodge_bonus!=0:
  screen_adjust+=3

 if enemy_crit_bonus!=0:
  screen_adjust+=3

 if enemy_has_rush:
  screen_adjust+=2

 if enemy_attack_bonus!=0 or enemy_defense_bonus!=0 or enemy_dodge_bonus!=0 or enemy_crit_bonus!=0 or enemy_has_rush:
  print(f'{'':>{format_size-screen_adjust}}',end='')

 if enemy_attack_bonus>0:
  print(f'{colors['green']}{'⚔ ↑'}{colors['end']}',end='')

 elif enemy_attack_bonus<0:
  print(f'{colors['red']}⚔ ↓{colors['end']}',end='')


 #//if enemy_attack_bonus>0 or enemy_attack_bonus<0:  # Prints bar only if enemy has an applied attack buff or debuff
  #//print('|',end='')

 if enemy_defense_bonus>0:  # Defense buff
  print(f'{colors['green']}{f'⛨ ↑'}{colors['end']}',end='')

 elif enemy_defense_bonus<0:  # Defense debuff
  print(f'{colors['red']}{f'⛨ ↓'}{colors['end']}',end='')


 if enemy_dodge_bonus>0:
  #//print('|',end='')
  print(f'{colors['green']}{f'🦶 ↑'}{colors['end']}',end='')

 elif enemy_dodge_bonus<0:
  #//print('|',end='')
  print(f'{colors['red']}{f'🦶 ↓'}{colors['end']}',end='')


 if enemy_crit_bonus>0:
  #//print('|',end='')
  print(f'{colors['green']}◎ ↑{colors['end']}',end='')

 if enemy_crit_bonus<0:
  #//print('|',end='')
  print(f'{colors['red']}◎ ↓{colors['end']}',end='')


 if enemy_has_rush:
  print(f'{colors['cyan']}💨{colors['end']}',end='')

 if enemy_attack_bonus!=0 or enemy_defense_bonus!=0 or enemy_dodge_bonus!=0 or enemy_crit_bonus!=0 or enemy_has_rush:  #! Skip line if there is a stat buff/debuff active due to 'end' command
  print()


 #* Debug
 print(f'{f'ATK BONUS: {enemy_attack_bonus}':>{format_size}}')
 print(f'{f'DEF BONUS: {enemy_defense_bonus}':>{format_size}}')
 print_line(format_size)


def item_and_skill_display(
  player_skill_item_for_display,
  #size_format No clue why I added, was never used
):
 """
 Generates a display of the currently available items for the player to use

 player_combat_stats: Current player stats, containing the inventory
 """

 menu_number_display=1

 for item in player_skill_item_for_display:
  print(f'[{menu_number_display}] {item['name']}')
  menu_number_display+=1

  sleep(0.2)
