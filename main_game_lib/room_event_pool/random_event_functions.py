from random import randint
from .combat_routines import *
from .shop_routine import *
from random import randint

# This is a bad solution, but after looking around in the internet
# What seems to happen is that apparently, modules can't import from one another when nested a certain way
# Not the one I need anyway, so I'm just going to improvise it - 04/07/2024

#*DONE add a check to see if player is dead in the miniboss event

def answer_check():
 """
 Checks the response and catches exceptions

 return: returns the player input

 """
 # Checks player response is within expected
 while True:
  try:
   player_input=int(input('What will you do? '))

  except ValueError:
   print('Type only non-decimal numbers!')
  #//return player_input

  except Exception as error:
   print('An error has ocurred!')
   print(error)

 #//return player_input

  else:
   return player_input


#! Obsolete, do not use
'''
def print_line_event(line_sizing):
 print('-'*line_sizing)


def display_event(message,size_formatting):
 print_line_event(size_formatting)
 print(message.center(size_formatting))
 print_line_event(size_formatting)
'''

# After some deliberation, I decided to create a small interface module
# It's the same functionality of the one used on the menus on the main
# It's just more convinient at the moment and easier then going around trying
# To circumvent bad imports while offering what I need - 04/07/2024

 #TODO Redo documentation here
def event_pool(
  random_event_choice: int,
  player_stats: dict,
  format_size: int,
  level_modifier: int,
  enemy_table: list,
  shop_contents: dict,
  event_itens: dict
  ):
 """
 Contains a pool of different events to be used

 random_event_choice: Dictates the random event that is supposed to happen

 player_stats: The current stats of the player

 format_size: Interger value for formating lines and centering on latter funcitons

 persistent_itens_list: List of itens that are persistent and are removed from the pool once bought

 level_modifier: Modifier used to allow certain events to trigger and improves event rewards

 enemy_table: List containing all the loaded enemy data

 mini_boss_table: List containing all the loaded mini-boss data

 acquirable_skills_list: List containing all the available skills data

 return: returns the updated player stats and the updated list of current relics available
 """

#*DONE Start using the 'event_itens' dict for stuff
#? This method for random events doesn't seem good
#? nor correct, there could be a different way to do it
#? but I don't know how
 match random_event_choice:

  case 0:     #| Coin on ground event

   while True:
    os.system('cls')
    dialogue_box(
     [
      '''Within the dark corridors of the maze''',
      '''A glimmer catches your attention'''
     ],
     format_size
    )
    print('[1] Approach it')
    print('[2] Ignore it')

    player_interact_choice=answer_check()

    if player_interact_choice>0 and player_interact_choice<=2:
     break

    else:
     continue

   print_line(format_size)

   if player_interact_choice==1:    #| If player decides to interact with the event

    event=randint(0-player_stats['luck'],1)     #| Decides if event is positive or negative

    if event<=0:      #| Positive outcome

     coins_in_pouch=20+((20*level_modifier)//2)

     dialogue_box(
      [
       '''The glimmer turned out to be a small pouch!''',
       '''Inside there are a couple coins''',
       'You hastly claim them as yours'
      ],
      format_size
     )
     print(f'You gained {coins_in_pouch} gold')
     player_stats['money']+=coins_in_pouch

     press_enter_to_continue('Press Enter to Continue')

    elif event>=1:         #| Negative outcome
     damage_taken=5+((5*level_modifier)//2)
     coins_in_pouch=(((20*level_modifier)//2)+20)

     dialogue_box(
      [
       'You realize the glimmer is coming from coins on the ground',
       'On your rush to grab them, you trigger a trap!',
       'You are attacked by a barrage of arrows!'
      ],
      format_size
     )
     press_enter_to_continue('Press Enter to Advance')
     system('cls')

     dialogue_box(
      [
       'You manage to dodge them, although not unscathed',
       'You quickly scoop up the coins before anything else happens'
      ],
      format_size
     )
     sleep(0.5)
     print(f'You have taken {damage_taken} damage')
     sleep(0.5)
     print(f'You grabbed {coins_in_pouch} gold')

     player_stats['hp_current']-=damage_taken
     player_stats['money']+=coins_in_pouch

     press_enter_to_continue('Press Enter to Continue')


   elif player_interact_choice==2:        #| If player chooses NOT to interact with event
    dialogue_box(
     [
      'You deliberate for a moment',
      'And chose to ignore the glimmer',
      'Not everything that shines is gold after all'
     ],
     format_size
    )
    press_enter_to_continue('Press Enter to Continue')

  case 1:      #| Case Combat

   #//enemy_to_load=randint(0,len(enemy_table)-1)
   #//enemy_to_load=0   #* NOTE: Debug

   combat_base(
    size_format_combat_screen=format_size,
    player_combat_stats=player_stats,
    current_enemy_stats=enemy_table['normal_enemy'].copy()
    )

  case 2:      #| Case Shop

   shop(
        format_size,
        player_stats,
        shop_contents,
        level_modifier
       )

  case 3:       #| Case special mini-boss event

   #*DONE There is a issue where, even if the player dies
   #*DONE they still get rewards after the fact
   #*DONE Gotta add a condition to prevent such
   #*DONE Add the punisher miniboss and create a function
   #*DONE That randomly chooses which miniboss will be used
   #// Improve the whole way the chance to trigger a miniboss and find
   #// the relic here works so the seeding matters here too
   while True:        # Ensures player input to be within expected

    os.system('cls')
    dialogue_box(
     enemy_table['miniboss']['encounter_message'],
     format_size
     )
    print('[1] Search the body')
    print('[2] Leave it alone')

    player_interact_choice=answer_check()

    if player_interact_choice>0 and player_interact_choice<=2:
     break

    else:
     continue

   #//print_line(format_size)

   search_attempts=5    # How many times player searched body
   times_searched=0        # Just for dialogue generation

   relic_found=event_itens['mini_boss_event_relic']       # Loads rewards from the event
   money_found=40*level_modifier
   #//mini_boss_to_be_loaded=randint(0,len(mini_boss_table)-1)         # Mini Boss Load

   if player_interact_choice==1:        # If player chooses to search

    while True:      # Search loop
     encounter_trigger=randint(0,(4+player_stats['luck']))  # Chance of finding the mini-boss

     encounter_trigger=2    #* Debug
     #//relic_found_index=1    #* Debug

     if search_attempts>0:
      item_found=randint((0-player_stats['luck']),search_attempts)

     elif search_attempts<=0:
      item_found=0

     if item_found<=0:     # If player finds something
      dialogue_box(
       [
        'With the body you find a trinket and a few coins',
        'You quickly leave before finding out what happened here'
       ],
       format_size
      )
      sleep(0.5)
      print(f'You found {money_found} gold')
      sleep(0.5)
      print(f'You found a {relic_found['name']}')

      money_found=40*level_modifier
      player_stats['relics'].append(relic_found)
      player_stats['money']+=money_found

      '''for key in relic_found.keys():
       try:

        player_stats[key]+=relic_found[key]

       except KeyError:
        pass

       finally:
        continue'''

      relic_player_stat_changes(
       relic_found,
       player_stats
      )

      press_enter_to_continue('Press Enter to Continue')

      break

     elif encounter_trigger==2:    #| If the mini-boss is triggered

      combat_base(
       size_format_combat_screen=format_size,
       player_combat_stats=player_stats,
       current_enemy_stats=enemy_table['miniboss'].copy(),
       mini_boss=True
       )

      if player_stats['player_is_alive']:
       sleep(0.5)
       print(f'You have obtained the {relic_found['name']}')
       player_stats['relics'].append(relic_found)

       #*DONE Update this to account for spark plug, should separate in its own function really
       '''for key in relic_found.keys():
        try:
         player_stats[key]+=relic_found[key]

        except KeyError:
         pass

        finally:
         continue'''

       relic_player_stat_changes(
       relic_found,
       player_stats
       )

       press_enter_to_continue('Press Enter to Continue')
       #//del persistent_itens_list[relic_found_index]    
      break

     else:     #| If player doens't find anything

      while True:   
       times_searched+=1

       if times_searched==1:     #| First failed search message
        os.system('cls')
        dialogue_box(
         [
          'You search him, but find nothing'
         ],
         format_size
        )

        print('[1] Keep searching')
        print('[2] Leave the body')

       elif times_searched>=2 and times_searched<4:     #| Message for following attempts
        os.system('cls')
        dialogue_box(
         [
          'You search him some more, but nothing still'
         ],
         format_size
        )

        print('[1] Search further')
        print('[2] Leave the body')

       elif times_searched>=4:  #| How did the minboss not happen yet?
        os.system('cls')
        dialogue_box(
         [
          'You are running out of spots to check'
         ],
         format_size
        )

        print('[1] Just a bit more')
        print('[2] Leave the body')

       player_interact_choice=answer_check()

       if player_interact_choice>0 and player_interact_choice<=2:
        break

       else:
        continue

      if player_interact_choice==1:
       search_attempts-=1
       continue

      elif player_interact_choice==2:
       dialogue_box(
        [
         'You decide is best not to push your luck'
        ],
        format_size
       )

       press_enter_to_continue('Press Enter to Continue')

       break

   elif player_interact_choice==2:
    dialogue_box(
     [
      'You decide is best not to risk',
      'learning what happened to him'
     ],
     format_size
    )

    press_enter_to_continue('Press Enter to Continue')

  case 4:     #| Max Health Idol event
   dialogue_box(
    [
     'On the corner of the room, you found an idol',
     'It has an ominous aura surrounding it',
     "You feel as if it's calling you..."
    ],
    format_size
   )
   print('[1] Pray at it')
   print('[2] Desecrate')
   print('[3] Touch the Idol')

   while True:
    player_interact_choice=answer_check()

    if player_interact_choice>=1 and player_interact_choice<=3:
     break

    print('Invalid Option')
   
   system('cls')

   if player_interact_choice==1:     #| Player prays at the idol
    gold_gained=10*level_modifier
    dialogue_box(
     [
      'You decide to pray at the idol',
      'You feel your pockets fill a little...'
     ],
     format_size
    )

    sleep(0.5)
    print(f'You gained {gold_gained} gold')
    player_stats['money']+=gold_gained

    press_enter_to_continue('Press Enter to Continue')

   elif player_interact_choice==2:     #| Player is atheist
    gold_gained=30+((level_modifier*60)//2)
    hp_lost=10+((level_modifier*20)//2)

    dialogue_box(
     [
      'You smash the idol to bits!',
      'It contained gold inside!',
      'You quickly pick it up',
      'Although you feel a deep pain within your body'
     ],
     format_size
    )
    sleep(0.5)
    print(f'You gained {gold_gained} gold')
    sleep(0.5)
    print(f'You took {hp_lost} damage')

    player_stats['money']+=gold_gained
    player_stats['hp_current']-=hp_lost

    press_enter_to_continue('Press Enter to Continue')

   elif player_interact_choice==3:    #| Hmm, me touch suspicious thing
    dialogue_box(
     [
      'You carefully touch the idol...',
      'Suddenly you feel as if your',
      'Life force is being drained!',
      'However your body feels sturdier too!'
     ],
     format_size
    )

    sleep(0.5)
    print(f'You took {10*level_modifier} damage')
    sleep(0.5)
    print(f'Your max health has increased by {5*level_modifier}')

    player_stats['hp_current']-=10*level_modifier
    player_stats['hp_max']+=5*level_modifier

    press_enter_to_continue('Press Enter to Continue')


  case 5: #| Midas chicken dinner event
   dialogue_box(
    [
     'You find a pristine table',
     'There are two plates on top of it',
     'One with a drumstick on it',
     'And the other with a whole chicken'
    ],
    format_size
   )
   print('[1] Eat the Drumstick')
   print('[2] Go for the whole chicken')
   
   while True:
    player_interact_choice=answer_check()

    if 0<player_interact_choice<3:
     break
    print('Enter a valid option!')


   if player_interact_choice==1:
    dialogue_box(
     [
      'You ate the single drumstick to the bone',
      'Although small, it gave you a satisfying meal'
     ],
     format_size
    )

    player_stats['hp_current']=player_stats['hp_max']

    sleep(0.5)
    print('You have been completely healed!')
    press_enter_to_continue('Press Enter to Continue')

   elif player_interact_choice==2:
    dialogue_box(
     [
      'You decide to get the whole chicken',
      'You pull a drumstick for yourself',
      'However as you bite it, the drumstick turns into gold!',
      'The bite hurt quite a bit, but the stick is surely valuable'
     ],
     format_size
    )

    relic_player_stat_changes(
     event_itens['midas_chicken_event'],
     player_stats
    )

    sleep(0.5)
    print(f'You obtained the {event_itens["midas_chicken_event"]['name']}')

    press_enter_to_continue('Press Enter to Continue')


  case 6: #| Cursed relic event

   dialogue_box(
    [
     'On the corner of the hallway',
     'You spot a figure covered in robes',
     'It seems to be calling you'
    ],
    format_size
   )
   press_enter_to_continue('Press Enter to Advance')

   os.system('cls')
   dialogue_box(
    [
     'As you approach the figure',
     'It offers you a weird trinket saying with a raspy voice',
     '''🎭 Take this! It's a gift from me to you'''
    ],
    format_size
   )

   print('[1] Take the relic')
   print('[2] Refuse it and leave')

   while True:
    player_interact_choice=answer_check()

    if 0<player_interact_choice<3:
     break
    print('Choose a valid option!')

   if player_interact_choice==1:
    dialogue_box(
     [
      'As soon as you pick the relic up',
      'The figure disappears with a cackling laugh',
      '🎭 I hope you enjoy my gift!'
     ]
    )

    player_stats['relics'].append(event_itens['cursed_relic'])
    relic_player_stat_changes(
     event_itens['cursed_relic'],
     player_stats
    )

    print(f'You have acquired the {event_itens['cursed_relic']['name']}')

    press_enter_to_continue('Press Enter to Continue')

   elif player_interact_choice==2:
    dialogue_box(
     [
      f'{player_stats['character_icon']} I rather not take it',
      "🎭 You're the one missing out",
      'The figure vanishes walking along the corridor'
     ],
     format_size
    )

    press_enter_to_continue('Press Enter to Continue')


  #TODO Add press to continue empty inputs to improve player experience
  case 7: #| Trader event
   dialogue_box(
    [
    'You find a small somewhat dark side room along the way',
    'Inside there is a pair of yellowish eyes',
    'They look directly into you, You have been noticed',
    'A voice calls you from inside'
    ],
    format_size
   )
   press_enter_to_continue('Press Enter to Advance')
   system('cls')

   dialogue_box(
    [
     ''' Hey you, come here!''',
     f'''{player_stats['character_icon']} ...''',
     ''' I'm not planning to hurt you''',
     ''' Now come here already'''
    ],
    format_size,
    '🐺',
    player_stats['character_icon']
   )

   print('[1] Approach the figure')
   print('[2] Continue on your path')

   while True:
    player_interact_choice=answer_check()

    if 0<player_interact_choice<3:
     break
    print('Invalid option')

   if player_interact_choice==2:
    os.system('cls')
    dialogue_box(
     [
      f"{player_stats['character_icon']} I don't have time for this",
      "🐺 You're the one who's missing out",
      'The figure says it as you proceed through the maze'
     ],
     format_size
    )
    press_enter_to_continue('Press Enter to Continue')

   elif player_interact_choice==1:
    items_choosen={}

    if len(player_stats['inventory'])>0:
     consumable_index=randint(0,(len(player_stats['inventory'])-1))
     items_choosen['consumable']=player_stats['inventory'][consumable_index]['name']

    #TODO Make so cursed relics are not included as possible candidates for trade
    if len(player_stats['relics'])>0:
     relic_index=randint(0,(len(player_stats['relics'])-1))
     items_choosen['relic']=player_stats['relics'][relic_index]['name']

    if (len(player_stats['skill_list'])-1)>0:
     while True:
      skill_index=randint(0,(len(player_stats['skill_list'])-1))
      if not player_stats['skill_list'][skill_index]['name']==player_stats['skill_list'][0]['name']:
       items_choosen['skill']=player_stats['skill_list'][skill_index]['name']
       break

    total_items=len(items_choosen)
    os.system('cls')

    if total_items>0:
     while True:
      if total_items==3:
       dialogue_box(
        [
         " I see you have quite the collection of treasures with you",
         " Ya'see, I'm a collector much like yourself",
         " So let's make a deal, gimme somethin' you have",
         " And I will give you somethin' I have in return"
        ],
        format_size,
        '🐺'
       )
      
      elif total_items==2:
       dialogue_box(
        [
         " You seem to have been scavengin' around a bit",
         " I have myself too, so why not share",
         " A bit of what we found with one another eh?"
        ],
        format_size,
        '🐺'
       )

      elif total_items==1:
       dialogue_box(
        [
         " Not unlike me, you've been through some hard times",
         " Don't be to worried 'bout it frien'",
         " I can assure you we can benefit one another!"
        ],
        format_size,
        '🐺'
       )

      for item_type in items_choosen.keys():
       print(f'[{item_type.capitalize()}] {items_choosen[item_type]}')
      print('Which item will you trade?')
      
      while True:
       player_choosen_item=str(input()).upper()

       if player_choosen_item[0] in 'CRS':
        break

       print('Input a valid item type!')

      system('cls')

      match player_choosen_item[0].upper():

       case 'C':

        try:
         sleep(0.5)
         print(f'You gave up the {items_choosen['consumable']}!')
         player_stats['inventory'].pop(consumable_index)

         dialogue_box(
          [
           " Ah, thank you, thank you",
           " Now here's my part of the deal!"
          ],
          format_size,
          '🐺'
         )

         player_stats['inventory'].append(event_itens['consumable_trader_item'])
         sleep(0.5)
         print(f'The merchant gave you a {event_itens['consumable_trader_item']['name']}')

         press_enter_to_continue('Press Enter to Continue')

         break

        except KeyError:
         pass

       case 'R':
        try:
         print(f'You gave up the {items_choosen['relic']}')
         relic_player_stat_changes_removing_relic(
          player_stats['relics'][relic_index],
          player_stats
         )
         player_stats['relics'].pop(relic_index)

         dialogue_box(
          [
           " Oh that's quite an interesting find",
           " Here, have this for you!"
          ],
          format_size,
          '🐺'
         )

         relic_player_stat_changes(
          event_itens['relic_trader_item'],
          player_stats
         )

         sleep(0.5)
         print(f'The merchant gave you the {event_itens['relic_trader_item']['name']}')
         player_stats['relics'].append(event_itens['relic_trader_item'])

         press_enter_to_continue('Press Enter to Continue')

         break

        except KeyError:
         pass

       case 'S':
        try:
         print(f'You gave up the {items_choosen['skill']}')
         player_stats['skill_list'].pop(skill_index)

         dialogue_box(
          [
           " Now that's something quite special",
           " Such generosity will not go unrewarded!",
           " Take this! I'm sure you'll like it"
          ],
          format_size,
          '🐺'
         )

         player_stats['skill_list'].append(event_itens['skill_trader_item'])
         print(f'The merchant gave you the {event_itens['skill_trader_item']['name']}')

         press_enter_to_continue('Press Enter to Continue')

         break

        except KeyError:
         pass

    else:
     dialogue_box(
      [
       " It seems you've been strugglin' frien'",
       " Here, this should help you a little"
      ],
      format_size,
      '🐺'
     )
     player_stats['money']+=25*level_modifier
     print(f'You gained {25*level_modifier}')
     press_enter_to_continue('Press Enter to Continue')

  case 8:
   display('EVENT 9',format_size)

  case 9:
   display('EVENT 10',format_size)

  case 10:
   display('EVENT 11',format_size)
   
 return None
   #player_stats,
   #persistent_itens_list,
   #acquirable_skills_list
 

# For Debug, remove later - 04/07/2024
# event_pool(random_event_choice=1)