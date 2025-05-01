from .item_list import *
from .shop_display import *
from .acquirable_skills import *
from .player_buy_functions import *
from ...menu_interface import integer_check
import os

#*DONE Fix the my lack of code reading skills and improve readability of this whole module
#*DONE Separate all buy functions in a different file for maintainability
#*DONE Need to start using random.choice() later because it's better
#TODO Make the shop man (it's actually a mouse guy who sells junk🐭👍)

def shop(size_format: int,
         player_stats_in_shop: dict,
         shop_contents: dict,
         price_modifier: int,
         ):
 """
 Shop internal workings, such as adding itens to player inventory, charge money and so on

 size_format: Integer value used for lines and centering

 player_stats_in_shop: Current player stats that will be altered

 #//persistent_itens_list: Persistent itens set. The ones currently loaded on the shop will be removed from this set

 shop_contents: Current itens available on the shop

 price_modifier: Current price modifier that will change how much is charged from the player

 #//acquirable_skills_list: List containing the available skills. Currently loaded ones in shop will be removed from this

 return: return updated player stats and persistent itens with the ones seen/bought removed from the list
 """

 # I need to get better variable names - 09/07/2024

 #//item_list=item_sheet()
 #//loaded_shop_check=False
 #//loaded_shop_data=[]
 insufficient_gold=False
 inventory_full=False
 heal_cost=20
 #//player_shopkeeper_interact=0
 dialogue_level=[]
 player_shopkeeper_interact=0

 while True:

  if player_stats_in_shop['first_time_on_shop']:
   while True:
    #//if len(dialogue_level)==0:

    (
     options_minimum,
     options_maximum,
     #//dialogue_level
    )=shopkeeper_display(
     size_format,
     player_stats_in_shop['first_time_on_shop'],
     #//player_shopkeeper_interact,
     player_stats_in_shop['character_icon'],
     player_stats_in_shop['action_available'],
     dialogue_level
    )

    if options_minimum==options_maximum==0 or (options_maximum==player_shopkeeper_interact==4):
     player_stats_in_shop['first_time_on_shop']=False
     system('cls')
     break

    while True:
     player_shopkeeper_interact=integer_check('Your Response: ',size_format)
     if options_minimum<=player_shopkeeper_interact<=options_maximum:
      dialogue_level.append(player_shopkeeper_interact)
      break    

      #//if player_shopkeeper_interact==1:
       #//dialogue_level.append(player_shopkeeper_interact)

      #//elif player_shopkeeper_interact==2:
       #//dialogue_level.append('B')

      #//elif player_shopkeeper_interact==3:
       #//dialogue_level.append('C')



  shop_display(size_format,
               shop_contents,
               player_stats_in_shop,
               price_modifier,
               heal_cost
              )

  if insufficient_gold:
   print('NOT ENOUGH GOLD!\n')

  if inventory_full:
   print('INVENTORY IS FULL\n')
  
  while True:

   try:
    player_shop_choice=int(input('Your Choice: '))

   except ValueError:
    print('Input only the numbers on the options!')

   except :
    print('There has been an unexpected error')
    print('Please try again')

   else:
    break


  match player_shop_choice:

   # I wish I was a better programmer because this doesn't feel right - 25/07/2024
   # In hindsight, this might actually be fairly okay. Could be improved - 03/09/2024

   case 1:    #| Cases for normal itens
    
    (
     insufficient_gold,
     inventory_full
    )=buy_item_common(
     shop_contents['shop_itens'][0], #> The number indicates which item is being bought
     size_format,
     player_stats_in_shop,
     price_modifier
     )
    os.system('cls')

   case 2:

    (
     insufficient_gold,
     inventory_full
    )=buy_item_common(
     shop_contents['shop_itens'][1],
     size_format,
     player_stats_in_shop,
     price_modifier
     )
    os.system('cls')

   case 3:
    (
     insufficient_gold,
     inventory_full
    )=buy_item_common(
     shop_contents['shop_itens'][2],
     size_format,
     player_stats_in_shop,
     price_modifier
     )
    os.system('cls')



   case 4:   #| Cases for relics

    if shop_contents['shop_relics'][0]['bought'] is False:

     (
      insufficient_gold,
      inventory_full
     )=buy_relic(
      shop_contents['shop_relics'][0],
      player_stats_in_shop,
      size_format,
      price_modifier
      )
    
    else:
     #//os.system('cls')
     pass

    os.system('cls')

   case 5:
    
    if shop_contents['shop_relics'][1]['bought'] is False:

     (
      insufficient_gold,
      inventory_full
     )=buy_relic(
      shop_contents['shop_relics'][1],
      player_stats_in_shop,
      size_format,
      price_modifier
      )

    else:
     #//os.system('cls')
     pass

    os.system('cls')


   case 6:   #| Cases player buys a skill

    if shop_contents['shop_skills'][0]['has_been_bought'] is False:

     (
      insufficient_gold,
      inventory_full
     )=buy_skill(
      player_stats_in_shop,
      shop_contents['shop_skills'][0],
      price_modifier,
      size_format
     )

    else:
     pass

    os.system('cls')

   case 7:

    if shop_contents['shop_skills'][1]['has_been_bought'] is False:

     (
      insufficient_gold,
      inventory_full
     )=buy_skill(
      player_stats_in_shop,
      shop_contents['shop_skills'][1],
      price_modifier,
      size_format
     )

    else:
     pass

    os.system('cls')


   case 8:   #| Case for heal 
    
    (
     insufficient_gold,
     inventory_full
    )=buy_healing(
                  player_stats_in_shop,
                  size_format,
                  price_modifier,
                  heal_cost,
                  insufficient_gold
                 )

   case 9:  #| Case to leave 
    break


   case _:  #| Case player has stupid
    print('Input a valid option!')

 #! This method is faulty and removes the wrong itens
 #! May sometimes raise an index error - 15/08/2024
 #//Removes relics seen in this shop from the pool
 #//for i in range(0,len(loaded_shop_data['shop_relics'])):
 #// del persistent_itens_list[loaded_shop_data['shop_relics'][i]]
 #! Being relocated to the 'get_random_itens' file
 '''if loaded_shop_data['shop_relics'][1]>loaded_shop_data['shop_relics'][0]:  #| Checks which index is higher and deletes them in order of higher to lower
  del persistent_itens_list[loaded_shop_data['shop_relics'][1]]
  del persistent_itens_list[loaded_shop_data['shop_relics'][0]]

 elif loaded_shop_data['shop_relics'][1]<loaded_shop_data['shop_relics'][0]:
  del persistent_itens_list[loaded_shop_data['shop_relics'][0]]
  del persistent_itens_list[loaded_shop_data['shop_relics'][1]]


 if loaded_shop_data['shop_skills'][1]>loaded_shop_data['shop_skills'][0]:
  del acquirable_skills_list[loaded_shop_data['shop_skills'][1]]
  del acquirable_skills_list[loaded_shop_data['shop_skills'][0]]

 elif loaded_shop_data['shop_skills'][1]<loaded_shop_data['shop_skills'][0]:
  del acquirable_skills_list[loaded_shop_data['shop_skills'][0]]
  del acquirable_skills_list[loaded_shop_data['shop_skills'][1]]'''

 # Holy this madness somehow actually works, let's gooo! \(T U T)/ - 11/07/2024

 return None
