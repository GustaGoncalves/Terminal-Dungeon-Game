from .shop_display import item_info_display

def relic_player_stat_changes(
  selected_relic:dict,
  player_stats_in_shop:dict,
 ):
 """
 The process of increasing/changing the player stats upon buying a relic

 selected_relic: Dict containing the relic stats and info

 player_stats_in_shop: Dict containing all the player stats
 """

 for key in selected_relic.keys():

  try:
   if type(selected_relic[key])==list:

    #> Some stat bonuses are based on a list
    #> As such It is necessary to treat it like this
    for stat in selected_relic[key]:
     player_stats_in_shop[key].append(stat)

   else: #| Regular stat buffs

    #> Because life steal is the only float that actually adds instead
    #> of subtracting I believe this is not too bad
    if type(selected_relic[key])==float:
     if key=='hp_max':
      selected_relic['hp_gain_loss']=int(selected_relic[key]*player_stats_in_shop[key])+((selected_relic[key]*player_stats_in_shop[key])%1>0)
      player_stats_in_shop[key]+=selected_relic['hp_gain_loss']
      if player_stats_in_shop['hp_max']<1:
       player_stats_in_shop['hp_max']=1
      
      if player_stats_in_shop['hp_current']>player_stats_in_shop['hp_max']:
       player_stats_in_shop['hp_current']=player_stats_in_shop['hp_max']

     #//elif key=='attack_current':
      #//player_stats_in_shop[key]+=int(selected_relic[key]*player_stats_in_shop[key])+((selected_relic[key]*player_stats_in_shop[key])%1>0)

     else:
      player_stats_in_shop[key]+=selected_relic[key]

    elif type(selected_relic[key])==int:
     player_stats_in_shop[key]+=selected_relic[key]

    elif type(selected_relic[key])==bool and key!='bought':
     player_stats_in_shop[key]=selected_relic[key]

  except KeyError: #| Creates the new stat if it doesn't exist
   pass

  except Exception as erro:
   print('What did I do wrong')
   print(erro.__class__)

    #//else:    
     #//continue

  finally:
   continue

 return None


def relic_player_stat_changes_removing_relic(
  selected_relic:dict,
  player_stats_in_shop:dict,
 ):
 """
 The process of increasing/changing the player stats upon buying a relic

 selected_relic: Dict containing the relic stats and info

 player_stats_in_shop: Dict containing all the player stats
 """

 for key in selected_relic.keys():

  try:
   if type(selected_relic[key])==list:

    #> Some stat bonuses are based on a list
    #> As such It is necessary to treat it like this
    for stat in selected_relic[key]:
     player_stats_in_shop[key].remove(stat)

   else: #| Regular stat buffs

    #> Because life steal is the only float that actually adds instead
    #> of subtracting I believe this is not too bad
    if type(selected_relic[key])==float:
     if key=='hp_max':
      player_stats_in_shop[key]-=selected_relic['hp_gain_loss']
      if player_stats_in_shop['hp_max']<1:
       player_stats_in_shop['hp_max']=1
      
      if player_stats_in_shop['hp_current']>player_stats_in_shop['hp_max']:
       player_stats_in_shop['hp_current']=player_stats_in_shop['hp_max']

     #//elif key=='attack_current':
      #//player_stats_in_shop[key]+=int(selected_relic[key]*player_stats_in_shop[key])+((selected_relic[key]*player_stats_in_shop[key])%1>0)

     else:
      player_stats_in_shop[key]-=selected_relic[key]

    elif type(selected_relic[key])==int:
     player_stats_in_shop[key]-=selected_relic[key]

    elif type(selected_relic[key])==bool and key!='bought':
     player_stats_in_shop[key]=not(selected_relic[key])

  except KeyError:
   pass

  except Exception as erro:
   print('What did I do wrong')
   print(erro.__class__)

    #//else:    
     #//continue

  finally:
   continue

 return None


def buy_item_common(
                    selected_item: dict,
                    size_format: int,
                    player_stats_in_shop: dict,
                    price_modifier: int,
                    inventory_full:bool=False,
                    insufficient_gold:bool=False
                   ):
 """
 Internal function of the process of buying the common item

 item_list: list of items available

 loaded_shop_data: currently loaded shop itens

 size_format: integer value for centering and line generation

 player_stats_in_shop: current player stats

 selected_item_index: current index of the loaded shop item

 price_modifier: Integer value that changes item price

 return: returns updated player stats and check for insufficient gold
 """

 item_info_display(selected_item['name'],
                   selected_item['description'],
                   size_format)

 while True:
  try:
   player_item_buy_confirm=str(input(f'Buy the {selected_item['name']}? [Y/N] ')).strip().upper()

  except ValueError:
   print('Input only letters!')

  # "What could possibly go wrong" - Bubsy, 1992
  # Everything Bubsy, everything went wrong - 11/07/2024
  except Exception as erro:
   print('An unexpected error has ocurred')
   print('Please try again')
   print(erro)

  else:
   if player_item_buy_confirm not in 'YyNn':
    print('Input only Y or N!')

   else:
    break

 if player_stats_in_shop['total_item_slots']>len(player_stats_in_shop['inventory']): #| Checks if player has the inventory space

  if price_modifier<=2:
   price_for_player_to_pay=selected_item['price']*price_modifier

  elif price_modifier>=3:
   price_for_player_to_pay=selected_item['price']+(int(selected_item['price']*1.5))

  if player_item_buy_confirm in 'Yy' and player_stats_in_shop['money']>=price_for_player_to_pay:   #| Player buys the item

   player_stats_in_shop['money']-=price_for_player_to_pay
   player_stats_in_shop['inventory'].append(selected_item.copy())

   #*DONE Simplify the flag changing so it doesn't change things unnecesseraly

  elif player_item_buy_confirm in 'Yy' and player_stats_in_shop['money']<price_for_player_to_pay:  #| Player lacks money to buy
   insufficient_gold=True

  elif player_item_buy_confirm in 'Nn':  #| Player chooses to not buy the item
   pass

 elif player_stats_in_shop['total_item_slots']<=len(player_stats_in_shop['inventory']) and player_item_buy_confirm in 'Yy':  #| Player has full inventory
  inventory_full=True


 return insufficient_gold,inventory_full


def buy_relic(
  selected_relic: dict,
  player_stats_in_shop: dict,
  size_format: int,
  price_modifier: int,
  insufficient_gold:bool=False
 ):
 """
 Internal function of the process of buying a relic

 persistent_itens_list: list of all available relics in game

 loaded_shop_data: Data/indexing of the currently loaded relics in the shop

 player_stats_in_shop: current player stats

 size_format: Integer value for line generation and centering

 selected_item_index: Index of the currently selected item to buy

 return: returns updated player stats, flag for lack of gold and flag for full inventory
 """


 item_info_display(selected_relic['name'],
                   selected_relic['description'],
                   size_format)

 while True:
  try:
   player_item_buy_confirm=str(input(f'Buy the {selected_relic['name']}? [Y/N] ')).strip().upper()

  except ValueError:
   print('Input only letters')

  except Exception as erro:
   print('An unexpected error has ocurred')
   print('Try again')
   print(erro)

  else:
   if player_item_buy_confirm not in 'YyNn':
    print('Input only Y or N!')

   else:
    break

 #TODO Improve the item price storage and modification
 #! Current method is suboptimal and not maintenance friendly 
 if price_modifier<=2:
  price_for_player_to_pay=selected_relic['price']*price_modifier

 elif price_modifier>=3:
  price_for_player_to_pay=selected_relic['price']+(int(selected_relic['price']*1.5)) # Average Java command line. Not anymore!


 if player_item_buy_confirm in 'Yy':  #| Player buys the permanent item

  if player_stats_in_shop['money']>=price_for_player_to_pay:

   player_stats_in_shop['money']-=price_for_player_to_pay

   # It worked first try. Something ain't right
   # This probably isn't a good way of doing but hey it works all right
   # This adds the stats of the relic bought by the player to their stats
   #*DONE Transform this on it's own function for
   #*DONE easier debuggin and use on other places
   '''for key in selected_relic.keys():

    try:
     if key=='elemental_damage_bonus': 

      #> Since elemental damage bonus works based on a list
      #> It is necessary to treat it like this
      for element in selected_relic[key]:
       player_stats_in_shop[key].append(element)

     else: #| Regular stat buffs

      #> Because life steal is the only float that actually adds instead
      #> of subtracting I believe this is not too bad
      if type(selected_relic[key])==float:
       if key!='life_steal':
        player_stats_in_shop[key]+=int(selected_relic[key]*player_stats_in_shop[key])+((selected_relic[key]*player_stats_in_shop[key])%1>0)

       else:
        player_stats_in_shop[key]+=selected_relic[key]

      elif type(selected_relic[key])==int:
       player_stats_in_shop[key]+=selected_relic[key]

    except KeyError: #| This error is expected to happen on iteration
     pass

    except Exception as erro:
     print('What did I do wrong')
     print(erro.__class__)

    #//else:    
     #//continue

    finally:
     continue'''
   
   relic_player_stat_changes(
    selected_relic,
    player_stats_in_shop
   )
   player_stats_in_shop['relics'].append(selected_relic.copy())
   #> Relocated
   #//if player_stats_in_shop['hp_current']>player_stats_in_shop['hp_max']:
    #//player_stats_in_shop['hp_current']=player_stats_in_shop['hp_max']

   selected_relic['bought']=True

  elif player_stats_in_shop['money']<price_for_player_to_pay:
   insufficient_gold=True

 elif player_item_buy_confirm in 'Nn':  # Player does not buy the item 
  pass


 return insufficient_gold,False


def buy_healing(
                player_stats_in_shop: dict,
                size_format: int,
                price_modifier: int,
                heal_cost: int,
                insufficient_gold: bool=False
               ):
 '''
 Internal function of the player buying a heal

 player_stats_in_shop: Current player stats inside the shop

 size_format: Integer value for line generation and centering

 return: Player stats and gold flag. Inventory flag is always false for this one
 '''

 if price_modifier<=1:
  current_heal_value=player_stats_in_shop['hp_max']//2

 elif price_modifier>=2:
  current_heal_value=int(player_stats_in_shop['hp_max']*(75/100))

 item_info_display('Healing Salve',
                   'A strong balm with powerful healing properties',
                   size_format)

 while True:
  try:
   player_item_buy_confirm=str(input(f'This will heal you for {current_heal_value} HP\nBuy the salve? [Y/N]')).strip().upper()

  except ValueError:
   print('Input only letters!')

  else:
   if player_item_buy_confirm in 'YyNn':
    break

   # No clue why I used else here - 17/08/2024
   #//else:
   print('Input only Y or N!')


 if player_item_buy_confirm in 'Yy': #| Player buys the heal

  if player_stats_in_shop['money']>=heal_cost:

   player_stats_in_shop['hp_current']+=current_heal_value
   player_stats_in_shop['money']-=heal_cost

   if player_stats_in_shop['hp_current']>player_stats_in_shop['hp_max']:  #| If player overheals
    player_stats_in_shop['hp_current']=player_stats_in_shop['hp_max']

  elif player_stats_in_shop['money']<heal_cost:  #| Player is poor
   insufficient_gold=True


 return insufficient_gold,False


def buy_skill(
              player_stats_in_shop: dict,
              selected_skill: dict,
              price_modifier: int,
              format_size: int,
              insufficient_gold: bool=False
             ):
 """
 Proccess of the player buying a skill

 player_stats_in_shop: player stats

 acquirable_skills_list: All available skills

 loaded_shop_data: Item index of the currently loaded shop

 selected_item_index: Item selected by the player to buy

 price_modifier: current price modifier

 insufficient_gold:(optional) Flag for when the player lacks gold

 format_size: Value used for lines, centering etc.

 return: updated player stats and skill list, insufficient gold flag and inventory full flag which is always false here
 """

 if price_modifier<=2:
  price_for_player_to_pay=selected_skill['price']*price_modifier

 elif price_modifier>=3:
  price_for_player_to_pay=['price']+(int(selected_skill['price']*1.2))


 item_info_display(
  selected_skill['name'],
  selected_skill['description'],
  format_size
 )


 while True:
  try:
   player_item_buy_confirm=str(input(f'Buy the {selected_skill['name']}? [Y/N] ')).strip()

  except ValueError:
   print('Input only letters!')

  else:
   if player_item_buy_confirm in 'YyNn':
    break

   print('Input only Y or N!')


 if player_item_buy_confirm in 'Yy':  #| Player elects to buy the skill

  if player_stats_in_shop['money']>=price_for_player_to_pay: #| Player has enough gold

   player_stats_in_shop['money']-=price_for_player_to_pay
   player_stats_in_shop['skill_list'].append(selected_skill.copy())
   selected_skill['has_been_bought']=True

  elif player_stats_in_shop['money']<price_for_player_to_pay: #|Player lacks gold
   insufficient_gold=True

 elif player_item_buy_confirm in 'Nn':
  pass


 return insufficient_gold,False