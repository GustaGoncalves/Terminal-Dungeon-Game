#//from random import randint
from os import system
from time import sleep
from random import choice

def print_line(line_size=40):
 """
 prints a line on the screen
 
 line_size:\n
   Integer value for the size of the line
 """
 
 print('-'*line_size)


def dialogue_box(
 lines: list,
 #//format_size: int,
 size_format :int,
 character_icon: str='',
 player_icon_in_dialogue: str=None,
 typing_speed: float=0.024,
 ):
 '''
 Prints messages smoothly character by character

 lines:\n
   lines of the message contained in a list

 size_format:\n
   Value for generating lines

 character_icon: (optional)\n
   Icon of the character speaking if there's any

 typing_speed: (optional)\n
   Rate in which characters are typed.\n
   Higher value means slower.\n
   Default value is 0.04

 player_icon_in_dialogue: (optional)\n
   If the player also speaks in the dialogue,\n
   It is necessary to treat the whole thing a little different\n
   If he does, add his icon to string message\n
   pass the player icon through in this parameter\n
   otherwise you can ignore this
 '''

 print_line(size_format)
 for message in lines:

  if message!=None:
   if player_icon_in_dialogue!=None and player_icon_in_dialogue in message:
    pass

   else:
    print(character_icon,end='')

   for letter in message:
    print(letter,end='')
    sleep(typing_speed)
   print()
 print_line(size_format)

 return None


def press_enter_to_continue(
 player_message: str,
 clear_screen: bool=True
 ):
 '''
 Generates the input command for the player to proceed

 player_message:\n
   Message the will be displayed for the player

 clear_screen:\n
   Flag that dictates if the screen should or not be cleared after
 '''

 print()
 input(player_message)
 if clear_screen:
  system('cls')

 return None


def shop_display(
 shop_format:int,
 loaded_shop:dict,
 player_stats_for_display:dict,
 price_modifier_display:int,
 heal_cost:int
 ):
 """
 generates and shows on the screen the current shop itens

 shop_format:\n
   Integer value for centering and line generation

 loaded_shop:\n
   Contains all the current contents of the shop

 player_stats_for_display:\n
   Current player stats that will be displayed

 heal_cost:\n
   Base healing cost

 price_modifier_display:\n
   Current price modifier of which the item prices will be multiplied by
 """
 
 #TODO I need to figure something better to the item price, as of now is not very sustainable
 #*DONE Should separate the whole item generation thing, or just put it in 'main_shop_routine', also should use choice instead of randint
 #*DONE Need to adjust how the code is being displayed for a better reading experience

 #//heal_cost=20

 if price_modifier_display>1:
  heal_cost+=(20*price_modifier_display)//2

 dialogue_box(
  shopkeeper_display(
   shop_format,
   player_stats_for_display['first_time_on_shop']
  ),
  shop_format,
  '🐭',
  None,
  0
 )

 print('YOU')
 print(f'HP: {player_stats_for_display['hp_current']} / {player_stats_for_display['hp_max']}')
 print(f'GOLD: {player_stats_for_display['money']}')
 print_line(shop_format)

 #! Obsolete do not use
 '''if shop_loaded is False:
  shop_item_1=randint(0,len(itens_for_display)-1) #! Must be -1 or else it may raise a KeyError

  while True: # Ensure item won't repeat
   shop_item_2=randint(0,len(itens_for_display)-1)

   if shop_item_2!=shop_item_1:
    break

  while True:
   shop_item_3=randint(0,len(itens_for_display)-1)

   if shop_item_3!=shop_item_2 and shop_item_3!=shop_item_1:
    break


  shop_relic_1=randint(0,len(persistent_itens_for_display)-1)

  while True:
   shop_relic_2=randint(0,len(persistent_itens_for_display)-1)
   if shop_relic_1!=shop_relic_2:
    break

  shop_relic_2=4  # * Debug

  shop_skill_1=randint(0,len(acquirable_skills_for_display)-1)
  shop_skill_1=1

  while True:
   shop_skill_2=randint(0,len(acquirable_skills_for_display)-1)
   
   if shop_skill_1!=shop_skill_2:
    break


  shop_item_index_list={
   'shop_itens':[shop_item_1,shop_item_2,shop_item_3],
   'shop_relics':[shop_relic_1,shop_relic_2],
   'shop_skills':[shop_skill_1,shop_skill_2]
  }

 else:
  shop_item_index_list=currently_loaded_shop  # Uses already loaded shop'''

 for i in range(0,len(loaded_shop['shop_itens'])):  # The display is setup this way due to how price if modyfied
  if price_modifier_display<=2:

   print(f'[{i+1}] {loaded_shop['shop_itens'][i]['name']}',end=' ')
   print(f'$ {loaded_shop['shop_itens'][i]['price']*price_modifier_display}',end=' | ')

  elif price_modifier_display>=3:

   print(f'[{i+1}] {loaded_shop['shop_itens'][i]['name']}',end=' ')
   print(f'$ {loaded_shop['shop_itens'][i]['price']+(int(loaded_shop['shop_itens'][i]['price']*1.5))}',end=' | ')

 print('')


 for i in range(0,len(loaded_shop['shop_relics'])):

  if loaded_shop['shop_relics'][i]['bought']:
   print('SOLD OUT',end='   ')

  else:

   if price_modifier_display<=2:
    print(f'[{i+4}] {loaded_shop['shop_relics'][i]['name']}',end=' ')
    print(f'$ {loaded_shop['shop_relics'][i]['price']*price_modifier_display}',end=' | ')

   elif price_modifier_display>=3:
    print(f'[{i+4}] {loaded_shop['shop_relics'][i]['name']}',end=' ')
    print(f'$ {loaded_shop['shop_relics'][i]['price']+(int(loaded_shop['shop_relics'][i]['price']*1.5))}',end=' | ')

 print('')  # Poor man's \n *sad_emoji*


 for i in range(0,len(loaded_shop['shop_skills'])):

  if loaded_shop['shop_skills'][i]['has_been_bought']:
   print('SOLD OUT',end='   ')

  else:

   if price_modifier_display<=2:
    print(f'[{i+6}] {loaded_shop['shop_skills'][i]['name']}',end=' ')
    print(f'$ {loaded_shop['shop_skills'][i]['price']*price_modifier_display}',end=' | ')

   elif price_modifier_display>=3:
    print(f'[{i+6}] {loaded_shop['shop_skills'][i]['name']}',end=' ')
    print(f'$ {loaded_shop['shop_skills'][i]['price']+(int(loaded_shop['shop_skills'][i]['price'])*1.2)}',end=' | ')

 print(f'\n[8] Heal $ {heal_cost}')
 print('[9] Leave')

 return None


def item_info_display(item_name,item_description,size):
 """
 Displays item info to player when buying any especific item

 item_name: Name of the item selected

 item_description: Description of the selected item

 size: Integer value for centering and formating lines
 """

 print_line(size)
 print(item_name.center(size))
 print(item_description.center(size))
 print_line(size)


#*DONE Use a For structure to develop a smooth typer
def shopkeeper_display(
  format_size: int,
  first_time_on_shop: bool,
  #//player_response: int,
  player_icon: str=None,
  player_class: dict=None,
  dialogue_tree: list=None,
  shopkeeper_icon: str='🐭',
  sleep_timer: float=0.5
 ):
 '''
 Generates both the first time dialogue trees
 the player can have with the shopkeeper
 and generates random flavour dialogue
 when the player already is on the shop

 format_size:
   Integer value used to generate lines and align text

 first_time_on_shop:
   Flag that indicates if player has or not been in the shop before

 player_icon (optional):
   Icon of the current player character

 player_class (optional):
   Dict containing the flags that indicate the current player character

 dialogue_tree (optional):
   List containing integere values equating to player answers\n
   This is only applicable in case it's the player's first time in the shop\n
   The idea is for it to follow a standard tree structure of sorts\n
   Each number inside it indicates the "dialogue branch" the player is on\n
    Ex.: [1,3,2] (left to right)\n
    This one indicates the player chose the first option on first dialogue\n
    Chose the third one in the second\n
    And the second one in the third\n

 shopkeeper_icon (optional):
   The icon used for the shopkeeper

 sleep_timer (optional):
   Float value used to delay line generation in the options
   Doing so gives out a somewhat smoother experience

 return (optional):
  If it's the first time the player has entered the shop\n
  It will return the number of available options on current dialogue\n
  Otherwise returns a list of random dialogues for the shop
 '''

 options_min=options_max=0

 if first_time_on_shop:
  total_responses=len(dialogue_tree)
  if total_responses==0: #| First Interaction

   dialogue_box(
    [
     'As you approach the room, you spot someone',
     "There's a myriad of different items scattered about"
    ],
    format_size
   )
   press_enter_to_continue('Press Enter to Continue')

   dialogue_box(
    [
     "A large travelling pack sits on comfortably at a corner",
     "Seems to be some kind of shop",
     "The person on the corner takes note of your presence and waves"
    ],
    format_size
   )
   press_enter_to_continue('Press Enter to Continue')

   dialogue_box(
    [
     ''' Oh hello there friend! You seem new around here''',
     ''' Pretty sure we haven't met before'''
    ],
    format_size,
    shopkeeper_icon
   )

   print('[1] Who are you?')
   sleep(sleep_timer)
   print('[2] What do you mean with new around here?')
   sleep(sleep_timer)
   print('''[3] I've been around before''')
   sleep(sleep_timer)
   print('[4] Skip Interaction')
   print_line(format_size)

   options_min=1
   options_max=4

  else:
   if dialogue_tree[0]==1: #| Branch [1]
    system('cls')
    #//print_line(format_size)

    if total_responses>=2:
     if dialogue_tree[1]==1: #| Branch [1,1]

      dialogue_box(
       [
        f'''{player_icon} A shop you say?''',
        ''' Why yes! You see, while exploring I've found quite a few things''',
        ''' Not all of them are useful for me however''',
        ''' So I'm giving them away...For a price of course''',
        f'''{player_icon} ...'''
       ],
       format_size,
       shopkeeper_icon,
       player_icon
      )
      press_enter_to_continue('Press Enter to Continue')

      dialogue_box(
       [
        ''' Oh don't give me that look, life isn't free nor cheap''',
        ''' You know that better than most''' if player_class['parry'] else None,
        f'''{player_icon}💢 Hmpf''' if player_class['parry'] else None,
        ''' Hard to not know who you are bud''' if player_class['parry'] else None,
        ''' Anyhow, I guarantee my prices will impress you''' if player_class['parry'] else ''' But my prices are some of the best you'll find''',
        ''' Not like there is any competition really'''
       ],
       format_size,
       shopkeeper_icon,
       player_icon
      )
      press_enter_to_continue('Press Enter to Continue')

      options_max=options_min=0


     elif dialogue_tree[1]==2: #| Branch [1,2]
      #*DONE Fix this shit too
      dialogue_box(
       [
        f'''{player_icon} What are you selling?''',
        ''' -Straight to the point no? I like that!'''
       ],
       format_size,
       shopkeeper_icon,
       player_icon
      )
      press_enter_to_continue('Press Enter to Advance')

      if player_class['berserk']:
       dialogue_box(
        [
         f'''{player_icon} Really?''',
         ''' Of course, much better than those smooth talking thiefs''',
         ''' No excessive talks that never go anywhere''',
         ''' Just directly saying what you're interested in''',
         f'''{player_icon} That's...an interesting way of looking at it''',
         ''' I say we keep this trend and do some business. Sounds good?''',
         f'''{player_icon} Sounds good to me'''
        ],
        format_size,
        shopkeeper_icon,
        player_icon
       )

      elif player_class['parry']:
       dialogue_box(
        [
         f'''{player_icon} Glad you like it, I prefer it this way too''',
         ''' Not surprising coming from you, but I'm not complaining''',
         f'''{player_icon} How about doing some business?''',
         ''' Took the words out of my mouth'''
        ],
        format_size,
        shopkeeper_icon,
        player_icon
       )

      elif player_class['steal']:
       dialogue_box(
        [
         ''' Here, have a look at this''',
         ''' Just don't get any funny ideas''',
         ''' I'm neither a charity nor merciful with shoplifters''',
         f'''{player_icon}💢 I'm not planning anything!''',
         ''' Oh don't be so insulted, y'know how it goes''',
         ''' Better to be safe than sorry'''
        ],
        format_size,
        shopkeeper_icon,
        player_icon
       )

      options_max=options_min=0


     elif dialogue_tree[1]==3: #| Branch [1,3]

      dialogue_box(
       [
        f'''{player_icon} Why set up shop here of all places''',
        ''' Anyone passing through this old labyrinth will need resources''',
        ''' So I have guarantee sales all around''',
        ''' Moreover, people will always end up finding me''',
        ''' So I don't ever really need move and redo the whole shop''',
        ''' And, with all of that said, why not take a look at my stuff?''',
        ''' I mean you're already here so might as well do it''',
        ''' And don't worry, whatever you buy WILL be useful'''
       ],
       format_size,
       shopkeeper_icon,
       player_icon
      )
      press_enter_to_continue('Press Enter to Continue')

     options_min=options_max=0

    else: #| Branch [1]

     dialogue_box(
      [
       f'''{player_icon} Who are you?''',
       ''' Well aren't you a feisty one? The name is Aiden''',
       ''' I'm just like you, an adventurer on, well...an adventure''',
       #//''' Though you seem to be more of a destination type guy''' if player_class['steal'] else None,
       ''' For now though, I've decided to setup a small shop'''
      ],
      format_size,
      shopkeeper_icon,
      player_icon
     )

     print('[1] A shop you say?')
     sleep(sleep_timer)
     print("[2] What is it that you're selling?")
     sleep(sleep_timer)
     print('[3] Why set up shop here of all places?')
     sleep(sleep_timer)

     options_min=1
     options_max=3

   elif dialogue_tree[0]==2: #| Branch [2]
    system('cls')

    if total_responses>=2:
     if dialogue_tree[1]==1: #| Branch [2,1]

      if total_responses>=3:

       if dialogue_tree[2]==1: #| Branch [2,1,1]

        dialogue_box(
         [
          f'''{player_icon} What about you then?''',
          ''' I'm just a simple merchant really, not much else to it''',
          ''' People go exploring and I sell them useful stuff''',
          ''' And since we're on the topic...''',
          ''' Why don't you take a look around?''',
          ''' I guarantee you'll find something useful!'''
         ],
         format_size,
         shopkeeper_icon,
         player_icon
        )
        press_enter_to_continue('Press Enter to Continue')

        options_max=options_min=0

       elif dialogue_tree[2]==2: #| Branch [2,1,2]

        dialogue_box(
         [
          f'''{player_icon} It really doesn't look that out of the ordinary though''',
          ''' I'm pretty damn confident this isn't no ordinary maze''',
          ''' You don't get so many people swarming a place like this for nothing''',
          ''' I mean everyone knows the tales about what can happen here''',
          ''' Yet they just keep flocking around here like moths on fire''',
          ''' Moreover, you're not gonna be the last one I see either'''
         ],
         format_size,
         shopkeeper_icon,
         player_icon
        )
        press_enter_to_continue('Press Enter to Advance')

        dialogue_box(
         [
          f'''{player_icon} Why did you come here then?''',
          ''' I'm...not quite sure the reason''',
          f'''{player_icon} What do you mean?''',
          ''' You probably won't believe what I'll tell you but...''',
          ''' It's almost as if something was calling me here''',
          ''' And I'm not sure I want to find out what it is''',
          ''' There's... just something about this place that pulls you in''',
         ],
         format_size,
         shopkeeper_icon,
         player_icon
        )
        press_enter_to_continue('Press Enter to Continue')

        options_min=options_max=0

      else: #| Branch [2,1]

       #*DONE Fix this shit, just make the conditions playout outside
       dialogue_box(
        [
         f'''{player_icon} Why would anyone come to this place?''',
         ''' There's many reasons for people to come here'''
        ],
        format_size,
        shopkeeper_icon,
        player_icon
       )
       press_enter_to_continue('Press Enter to Advance')

       if player_class['steal']:
        dialogue_box(
         [
          ''' Robbing the fabled hidden treasures is a fairly common one''',
          ''' I mean that's why you're here right?''',
          ''' Not that I'm judging you''',
          ''' Likely would do the same in your position''',
          ''' Either way, that's just one example''',
          ''' There's a lot more to the alure of this place...'''
         ],
         format_size,
         shopkeeper_icon,
         player_icon
        )
       
       elif player_class['parry']:
        dialogue_box(
         [
          '''Some dream of the glory they might obtain by conquering the maze''',
          ''' That's, in part at least, why you're here no?''',
          f'''{player_icon} You know nothing of me''',
          ''' Your name is already out there, and know as much as I need about it''',
          f'''{player_icon} ...''',
          ''' Either way, that's just an example''',
          ''' There's much more to the alure of this place...'''
         ],
         format_size,
         shopkeeper_icon,
         player_icon
        )

       elif player_class['berserk']:
        dialogue_box(
         [
          ''' They say there's a relic with tremendous power hidden somewhere''',
          ''' Supposedly, it's powerful enough to cure any ailment, including dispelling curses''',
          f'''{player_icon} ...''',
          ''' I take it this is a touchy subject for you''',
          ''' Well, this is just an example really''',
          ''' There's a lot more to the alure of this place...'''
         ],
         format_size,
         shopkeeper_icon,
         player_icon
        )

       print('[1] What about you then?')
       sleep(sleep_timer)
       print("[2] It doesn't really look that out of the ordinary though")
       sleep(sleep_timer)
       print_line(format_size)

       options_min=1
       options_max=2

     elif dialogue_tree[1]==2: #| Branch [2,2] 

      dialogue_box(
       [
        f'''{player_icon} How long have you been here?''',
        ''' I've been doing business for sometime now''',
        ''' From what it seems, I'm the only merchant around''',
        ''' Don't worry about it if you're thinking of buying something''',
        ''' I don't usually charge much'''
       ],
       format_size,
       shopkeeper_icon,
       player_icon
      )
      press_enter_to_continue('Press Enter to Advance')

      dialogue_box(
       [
        f'''{player_icon} Usually?''',
        ''' Supply and demand friend, more costumers equals lower prices''',
        ''' Don't be worried about that either''',
        ''' Movement seems to be always consistently high''',
        ''' With that said, why don't you take a look around?''',
        ''' I mean, you're already here so might as well make the most of it no?''',
        ''' And I'm sure you'll find something useful'''
       ],
       format_size,
       shopkeeper_icon,
       player_icon
      )
      press_enter_to_continue('Press Enter to Continue')

      options_max=options_min=0

    else: #| Branch [2]
     dialogue_box(
      [
       f'''{player_icon} What do you mean with new around here?''',
       ''' You're not the first one around here y'know''',
       ''' You probably noticed this by now, but I'm a merchant of sorts''',
       ''' So I've seen quite a few people go by''',
      ],
      format_size,
      shopkeeper_icon,
      player_icon
     )

     print('[1] Why would anyone come to this place?')
     sleep(sleep_timer)
     print('[2] How long have you been here?')
     sleep(sleep_timer)

     options_min=1
     options_max=2


   elif dialogue_tree[0]==3: #| Branch [3]
    system('cls')
    if total_responses>=2:

     if dialogue_tree[1]==1: #| Branch [3,1]
      if total_responses>=3:

       if dialogue_tree[2]==1: # |Branch [3,1,1]
        if total_responses>=4:

         if dialogue_tree[3]==1: #| Branch [3,1,1,1]
          dialogue_box(
           [
            f'''{player_icon} There's people besides us in here?''',
            ''' You probably know this, but this labyrinht is quite famous''',
            ''' All sorts of legends are tied around this place'''
           ],
           format_size,
           shopkeeper_icon,
           player_icon
          )
          press_enter_to_continue('Press Enter to Advance')

          if player_class['steal']:
           dialogue_box(
            [
             ''' Like the tales about a treasure hidden somewhere''',
             ''' No doubt you heard your fair share of those''',
             f'''{player_icon} Just a handful, but all seem unbelievable''',
             ''' Not enough to stop people from looking for it though'''
            ],
            format_size,
            shopkeeper_icon,
            player_icon
           )
           press_enter_to_continue('Press Enter to Advance')
           

          elif player_class['parry']:
           dialogue_box(
            [
             ''' Because of that, the place garnered quite a bit of fame''',
             ''' Many come here thinking they'll make it big by conquering the place''',
             ''' Most come in and out with no sucess, some just never leave''',
             f'''{player_icon} Hmpf, don't think silly folk tales scare me'''
            ],
            format_size,
            shopkeeper_icon,
            player_icon
           )
           press_enter_to_continue('Press Enter to Advance')

          elif player_class['berserk']:
           dialogue_box(
            [
             ''' There's that one tale about some sort of artifact''',
             ''' It is said to be on the deeper ends of the maze''',
             ''' They say it has all kinds of miraculous powers''',
             ''' Like curing any disease''',
             ''' Supposedly it can dispel magic of any kind''',
             f'''{player_icon} ...'''
            ],
            format_size,
            shopkeeper_icon,
            player_icon
           )
           press_enter_to_continue('Press Enter to Advance')

          dialogue_box(
           [
            ''' Either way, one thing is certain''',
            ''' You're not planning to leave this place empty handed''',
            ''' And, for a small fee, I'll be able to help you with that'''
           ],
           format_size,
           shopkeeper_icon
          )
          press_enter_to_continue('Press Enter to Continue')

          options_max=options_min=0


         elif dialogue_tree[3]==2: #| Branch [3,1,1,2]
          dialogue_box(
           [
            f'''{player_icon} Why are you staying here?''',
            ''' You really like prying on others no?'''
           ],
           format_size,
           shopkeeper_icon,
           player_icon
          )
          press_enter_to_continue('Press Enter to Advance')

          if player_class['steal']:
           dialogue_box(
            [
             f'''{player_icon} That's just what I do''',
             ''' And what I do is point out nosy people''',
             ''' Specially your type'''
            ],
            format_size,
            shopkeeper_icon,
            player_icon
           )
           press_enter_to_continue('Press Enter to Advance')

          elif player_class['berserk']:
           dialogue_box(
            [
             f'''{player_icon} Sorry, I didn't mean t--''',
             ''' Don't worry about that. I'd do the same in your position''',
             ''' But I appreciate your concern''',
             ''' It's rare to find someone who does'''
            ],
            format_size,
            shopkeeper_icon,
            player_icon
           )
           press_enter_to_continue('Press Enter to Advance')

          elif player_class['parry']:
           dialogue_box(
            [
             f'''{player_icon} So what? Planning on doing something about it?''',
             ''' You really are just like people say huh?''',
             f'''{player_icon} You give rumors too much credit''',
             ''' And you live up to them too much'''
            ],
            format_size,
            shopkeeper_icon,
            player_icon
           )
           press_enter_to_continue('Press Enter to Advance')

          dialogue_box(
           [
            ''' Anyhow, my reasoning is rather simple''',
            ''' These halls have lots of stuff just laying about''',
            ''' Weird relics, antique weapons and so on''',
            ''' There's even books teaching some fighting techniques''',
            ''' So I've amassed quite the collection here'''
           ],
           format_size,
           shopkeeper_icon
          ),
          press_enter_to_continue('Press Enter to Advance')

          dialogue_box(
           [
            ''' Since there's still people venturing down the maze''',
            ''' Why not give them a hand by doing some good business?''',
            ''' They get a useful doodad for a good price''',
            ''' It's a mutually beneficial afair really'''
           ],
           format_size,
           shopkeeper_icon
          )
          press_enter_to_continue('Press Enter to Advance')

          dialogue_box(
           [
            ''' Also, like I mentioned before, the maze constantly shifts''',
            ''' So I don't need to move myself as often''',
            ''' With that said, why don't take a look at my collection?''',
            ''' Maybe you'll find something useful''',
            ''' I know there is no competition, but I'm not a scalper''',
            ''' My prices are always fair and square'''
           ],
           format_size,
           shopkeeper_icon
          )
          press_enter_to_continue('Press Enter to Continue')

          options_min=options_max=0

        else: #| Branch [3,1,1]
         dialogue_box(
          [
           f'''{player_icon} How long have you been here?''',
           ''' After a while you start losing track of time inside these halls''',
           ''' So I'm not sure how long I've been here''',
           ''' I've met quite a few people by now''',
           ''' And like I said, stick around long enough in a place''',
           ''' And you start noticing the halls shifting''',
           ''' So I'd say I've been around for a while now'''
          ],
          format_size,
          shopkeeper_icon,
          player_icon
         )

         print('''[1] There's people besides us in here?''')
         sleep(sleep_timer)
         print('''[2] Why are you staying here?''')
         sleep(sleep_timer)

         options_min=1
         options_max=2

       elif dialogue_tree[2]==2: # |Branch [3,1,2]
        if total_responses>=4:

         if dialogue_tree[3]==1: #| Branch [3,1,2,1]

          dialogue_box(
           [
            f'''{player_icon} I take it you don't live far then''',
            ''' Pretty much. Before setting up my little business here''',
            ''' I would run a small shop on a nearby town''',
            ''' And while I do miss being at home''',
            ''' There's somethin refreshing about being on the move again'''
           ],
           format_size,
           shopkeeper_icon,
           player_icon
          )
          press_enter_to_continue('Press Enter to Advance')

          dialogue_box(
           [
            f'''{player_icon} Again?''',
            ''' Again Indeed. I used to be a merchant in Hawkwel''',
            ''' Pretty far town from here'''
            ''' But I was never one to stay in one place too much''',
            ''' So soon enough I found myself travelling through the continent''',
           ],
           format_size,
           shopkeeper_icon,
           player_icon
          )
          press_enter_to_continue('Press Enter to Advance')

          dialogue_box(
           [
            ''' Going around the world is pretty rewarding and fun''',
            ''' But even a free spirit has to settle down eventually''',
            ''' Once I heard about these ruins here though''',
            ''' I just couldn't resist checking them out''',
            ''' It was almost as if they were calling for me''',
            ''' So back on the on the road I am'''
           ],
           format_size,
           shopkeeper_icon
          )
          press_enter_to_continue('Press Enter to Advance')

          dialogue_box(
           [
            ''' Oh look at me rambling about myself again''',
            ''' Thanks for hearing all of it though''',
            ''' It's been a while since someone bothered hearing me''',
            f'''{player_icon} Does that mean I get a discount?''',
            ''' Now, now, let's not get ahead of ourselves okay?''',
            ''' I will try saving the best stuff for you as thanks though''',
           ],
           format_size,
           shopkeeper_icon,
           player_icon
          )
          press_enter_to_continue('Press Enter to Continue')

          options_min=options_max=0

         if dialogue_tree[3]==2: #| Branch [3,1,2,2]
          dialogue_box(
           [
            f'''{player_icon} Why stay here then?''',
            ''' Convenience of course! No need to move all that much''',
            ''' When the maze itself moves for you''',
           ],
           format_size,
           shopkeeper_icon,
           player_icon
          )
          press_enter_to_continue('Press Enter to Advance')

          dialogue_box(
           [
            ''' So hey, if nothing I have now interests you''',
            ''' You'll likely cross me again in the future''',
            ''' With a completely new inventory for you'''
           ],
           format_size,
           shopkeeper_icon
          )
          press_enter_to_continue('Press Enter to Continue')

          options_min=options_max=0


        else: #| Branch [3,1,2]
         dialogue_box(
          [
           f'''{player_icon} How do you know the entrance ramins?''',
           ''' What? Are you assuming I'm some gremlin who lives here?''',
           ''' Every now then and I will leave the place a bit''',
           ''' Well, when the maze shifts favours me of course''',
          ],
          format_size,
          shopkeeper_icon,
          player_icon
         )

         print("[1] I take it you don't live far then")
         sleep(sleep_timer)
         print("[2] Why stay here then?")
         sleep(sleep_timer)

         options_min=1
         options_max=2

      else: #| Branch [3,1]
       dialogue_box(
        [
         f'''{player_icon} Everchanging?''',
         ''' You seem quite unaware of your surroundings''',
         ''' Really surprising for your type but I digress''' if player_class['steal'] else ''' Not surprising considering your fame y'know''' if player_class['parry'] else None,
         ''' But yes, everchanging. This place changes it's structure from time to time'''
        ],
        format_size,
        shopkeeper_icon,
        player_icon
       )
       press_enter_to_continue('Press Enter to Advance')

       dialogue_box(
        [
         ''' It's a silent undertaking, so much that many, like you, don't notice it''',
         ''' But stay long enough in one place and before y'know it''',
         ''' You'll be somewhere completely different''',
         ''' Funny thing is, the entrance remains mostly the same...'''
        ],
        format_size,
        shopkeeper_icon,
        player_icon
       )

       print('''[1] How long have been here?''')
       sleep(sleep_timer)
       print('''[2] How do you know the entrance remains?''')
       sleep(sleep_timer)

       options_min=1
       options_max=2


     elif dialogue_tree[1]==2: #| Branch [3,2]
      if total_responses>=3:

       if dialogue_tree[2]==1: #| Branch [3,2,1]
        dialogue_box(
         [
          f'''{player_icon} Who's this trader?''',
          ''' He's this guy on these dark robes''',
          ''' His face is completely obscured because of it''',
          ''' With the exception of his glowing yellowish eyes'''
         ],
         format_size,
         shopkeeper_icon,
         player_icon
        )
        press_enter_to_continue('Press Enter to Advance')

        dialogue_box(
         [
          ''' As I've implied, he trades stuff''',
          ''' You give him one of your possessions''',
          ''' And he will give you one of his''',
          ''' The catch is that you won't know what you're getting'''
         ],
         format_size,
         shopkeeper_icon
        )
        press_enter_to_continue('Press Enter to Advance')

        dialogue_box(
         [
          ''' If that kind of stuff interests you''',
          ''' You should buy something here''',
          f'''{player_icon} Seriously? I'm already at your shop''',
          ''' And you haven't bought anything...Yet''',
          ''' So how about we change that?'''
         ],
         format_size,
         shopkeeper_icon,
         player_icon
        )
        press_enter_to_continue('Press Enter to Continue')

        options_min=options_max=0

       elif dialogue_tree[2]==2: #| Branch [3,2,2]
        dialogue_box(
         [
          f'''{player_icon} Blacksmith lady?''',
          ''' You heard it, there's this room in the labyrinth''',
          ''' Inside there's a small forge with an anvil''',
          ''' And the blacksmith is this one lady'''
         ],
         format_size,
         shopkeeper_icon,
         player_icon
        )
        press_enter_to_continue('Press Enter to Advance')

        dialogue_box(
         [
          ''' She usually offers a sharpening service''',
          ''' But with a few extra coins''',
          ''' She'll will help you improve your own skills''',
          ''' Who would have thought that a blacksmith knows martial arts'''
         ],
         format_size,
         shopkeeper_icon
        )
        press_enter_to_continue('Press Enter to Advance')

        dialogue_box(
         [
          ''' So if you're interested in learning something from her''',
          ''' You may want to consider buying a thing or two from me''',
          f'''{player_icon} You really want me to buy something huh?''',
          ''' That's just part of the business really''',
          ''' Anyways, Just ring me if you want to buy something'''
         ],
         format_size,
         shopkeeper_icon,
         player_icon
        )

        press_enter_to_continue('Press Enter to Continue')

        options_max=options_min=0

      else: #| Branch [3,2]
       dialogue_box(
        [
         f'''{player_icon} I take it you've been here before''',
         ''' Oh I've been around for quite a while now''',
         ''' As you can see, I am a merchant of sorts''',
         ''' Your trusty, one and only merchant!'''
        ],
        format_size,
        shopkeeper_icon,
        player_icon
       )
       press_enter_to_continue('Press Enter to Advance')

       dialogue_box(
        [
         f'''{player_icon} You're the only merchant around?''',
         ''' Pretty much. I mean, There's that one trader too''',
         ''' But I wouldn't call him much of a merchant''',
         ''' There's also that blacksmith lady''',
         ''' But she's giving out a service rather than goods''',
        ],
        format_size,
        shopkeeper_icon,
        player_icon
       )

       print('''[1] Who's this trader?''')
       sleep(sleep_timer)
       print('''[2] Blacksmith lady?''')
       sleep(sleep_timer)

       options_min=1
       options_max=2

    else: #| Branch [3]
     dialogue_box(
      [
       f'''{player_icon} I've been around before''',
       ''' I see, not really surprise I haven't seen you''',
       ''' Specially since your type tends to be quite sneaky''' if player_class['steal'] else ''' Even though a figure like you is hard to miss''' if player_class['berserk'] else None,
       ''' This everchanging maze always finds a way to hide something'''
      ],
      format_size,
      shopkeeper_icon,
      player_icon
     )

     print('[1] Everchanging?')
     print("[2] I take it you've been here before")

     options_min=1
     options_max=2

  return options_min,options_max,#//dialogue_tree


 else:

  #TODO add more dialogue here later
  random_dialogue_set=[
   [
    ''' You planning on buying something?''',
    ''' Or did you just come in here to say hi?''',
    ''' Not that I'm complaining'''
   ],
   [
    ''' You know what people have been saying?''',
    ''' They say there's a griffin somewhere in the labyrinth''',
    ''' Hope neither or I have to see if discover if it's true'''
   ],
   [
    ''' Some skills may seem to not do much''',
    ''' But there's a few with additional effects''',
    ''' All you need is a little luck'''
   ],
   [
    ''' Lots of folks seem to be supersticious''',
    ''' They all carry these copper lucky coins''',
    ''' I wonder if they actually make you lucky...'''
   ],
   [
    ''' Don't know if I mentioned before''',
    ''' But somewhere in the maze there's a blacksmith''',
    ''' She's quite beautiful, not really my type though'''
   ],
   [
    ''' Have I ever told about the trader guy?''',
    ''' If you have items he will swap one with you''',
    ''' Just the more reason to buy from me no?'''
   ],
   [
    ''' There's this one spinning kick technique''',
    ''' It seems somewhat useless at first''',
    ''' But the more you use it the stronger it gets'''
   ],
   [
    ''' Y'know since I don't have any competition''',
    ''' I've been thinking of raising my prices a bit...''',
    ''' Haha! I'm just kidding...For real I AM joking'''
   ],
   [
    ''' Ever felt as if you were walking in circles?''',
    ''' Whenever I leave my spot that's how I feel''',
    ''' Sometimes the walls look so similar...'''
   ],
   [
    ''' Did y'know, there's flamming spiders in here''',
    ''' By the gods I hate spiders so much already''',
    ''' Was there any need to make immune to fire?'''
   ],
   [
    ''' Oh this sword of mine? Not for selling''',
    ''' It's an old heirloom of mine. Have it since ever''',
    ''' Despite it's age, still does a good job keeping me alive'''
   ],
   [
    ''' Oh the hat? Really good isn't it?''',
    ''' Come on! Don't make that face, it's stylish okay?''',
    ''' Bah what would YOU know of style anyways'''
   ],
   [
    ''' Honestly, staying here gets lonely sometime''',
    ''' Hopefully we'll be seeing one another often''',
    ''' Even better if you buy something while at it'''
   ],
   [
    ''' Did I tell you I'm from hawkwel? Pretty big city''',
    ''' They have lots of airships there, so business is always high''',
    ''' People from all over go by for shopping and tourism'''
   ],
   [
    ''' Ever heard of the Forsaken Lands?''',
    ''' They say that desert was witness to a nasty war''',
    ''' People turned the scrapped airships into their homes there'''
   ],
   [
    ''' Do you know Pontifex Archard Magnom from Lahvren?''',
    ''' Most people call him Archie despite'''
    ''' They say he's quite a beast fighting despite the appearances''',
   ],
   [
    ''' Y'know something funny? Despite lots of people coming here''',
    ''' You can still make the rounds and not find anyone''',
    ''' It's like as if the maze just decides when you'll see somenone else'''
   ],
   [
    ''' Hey did you know? Most relics have multiple boosts''',
    ''' Some are very clear, but others are subtle and hidden''',
    ''' All the more reason for you to buy them right?'''
   ]
  ]

  return choice(random_dialogue_set)