from time import sleep

#>NOTE Whenever a new uniquely treated debuff is added,
#>don't forget to properly treat in the panacea, if 
#>it's supposed to be curable

def usable_item_effects(
    item_currently_being_used: dict,
    enemy_stats: dict,
    enemy_status: list,
    player_stats: dict,
    player_status: list,
    format_size: int,
    player_attack_bonus: int,
    player_defense_bonus: int,
    enemy_attack_bonus: int,
    enemy_defense_bonus: int,
    turn_count: int,
    enemy_is_debuffed_damage: bool,
    damage_overtime: dict,
    debuff_ends_at: dict,
    turn_debuff_was_applied: dict,
    stat_debuff_data: dict,
    stat_debuff_power: dict,
    enemy_is_debuffed_stat: bool,
    rage_buff: bool,
    rush_buff: bool,
    player_is_debuffed_damage: bool,
    player_is_stat_debuffed: bool,
    turn_count_enemy_debuffs: dict,
    damage_per_turn_enemy: dict,
    enemy_debuff_ends_at: dict,
    enemy_stat_debuff_power: dict,
    enemy_stat_decreased: dict,
    player_stat_buff_data: dict,
    player_stat_buff_power: dict,
    player_stat_buff_duration: dict,
    player_stat_buff_was_applied_at: dict,
    player_dodge_bonus: int,
    player_is_stat_buffed: bool,
    item_used_breaks: bool
):
 """
 sheet containing the effects of each usable/consumable item, made to be applicable in a universal way

 item_being_currently_used: The item the player has currently elected to use

 enemy_stats: stats of the current enemy the player is facing

 enemy_status: current status effect of the enemy

 player_stats: current player stats

 player_status: current player status effect

 format_size: Integer bla bla bla you know the thing, makes lines and centers things and is a number

 player_attack_bonus: current player attack buffs/modifiers

 player_defense_bonus: current player defense buffs/modifiers

 enemy_attack_bonus: current enemy attack buffs/modifiers

 enemy_defense_bonus: current enemy defense buffs/modifiers

 damage_overtime: Dict containing damage values of all debuffs

 debuff_ends_at: Dict containing when the debuffs should run out

 turn_debuff_was_applied: Dict containing when each debuff was applied

 stat_debuff_data: Contains the stats reduced by a stat debuff

 stat_debuff_power: Stores how much enemy stats were lowered by the debuff

 enemy_is_debuffed_stat: Bool value to check if enemy has stats lowered

 rage_buff: Player rage buff flag

 rush_buff: Player rush buff flag

 player_is_debuffed_damage: Flag for when the player has a damage debuff
 
 player_is_stat_debuffed: Flag for when the player has a stat debuff
 
 turn_count_enemy_debuffs: Dict containing turn count of all enemy debuffs
 
 damage_per_turn_enemy: Dict containing damage of all enemy debuffs
 
 enemy_debuff_ends_at: Dict containing when all enemy debuffs end
 
 enemy_stat_debuff_power: Dict containing the power value of all enemy stat debuffs
 
 enemy_stat_decreased: Dict containing which stats each enemy debuff has reduced

 player_stat_buff_data: Dict with the stats the buff increased

 player_stat_buff_power: Dict with how much the player stat was buffed

 player_stat_buff_duration: Dict containing the duration of the buff

 player_stat_buff_was_applied_at: Dict containing the turn stat buffs were applied

 player_dodge_bonus: Current player dodge chance bonus

 player_is_stat_buffed: Flag for player having a temporary stat buff

 item_used_breaks: Flag for item being deleted from the player inventory

 return: This returns way to much stuff to simply add here.
         In summary returns how long a debuff might last, damage dealt by a consumable,
         damage caused by debuff and all stats and status from the player and enemy.
         In theory it should be possible to figure out most of it through comments
         and variable names alone.

         UPDATE 22/08/2024 - It returns even more stuff now
                             Someone help me please I am going insane

         The return has significantly reduced.
         Now it returns only the debuff flags related
         to the player and the enemy and returns their current stat bonuses.
 """

 # Managed to figure a way to deal with consumable item effects that isn't total garbage
 # Since these are attached to each item, they can be used universaly and repeatedly with other itens
 # Further more I'm already cooking some ideas on how to make multiple effects happen on a single item using this - 31/07/2024 UPDATE: Multiple effects can take place at once now

 #damage_overtime={}
 #debuff_ends_at={}
 #turn_debuff_was_applied={}

 sleep_timer=0.5


 sleep(sleep_timer)

 try:
  item_currently_being_used['item_charges']-=1
  print(item_currently_being_used['usage_messages'][item_currently_being_used['item_charges']])

  if item_currently_being_used['item_charges']<=0:
   item_used_breaks=True
  else:
   item_used_breaks=False

 except KeyError:
  item_used_breaks=True
  print(item_currently_being_used['usage_message'])

 if 'DAMAGE' in item_currently_being_used['effect_types']:   #| Item just causes damage
  item_damage=item_currently_being_used['power_damage']

  if item_currently_being_used['elemental'] in player_stats['elemental_damage_bonus']: #| Elemental bonus
   item_damage+=int((item_damage*0.5))+(item_damage%2)

  try:
   if item_currently_being_used['elemental'] in enemy_stats['elemental_weakness']:
    item_damage=(item_damage//2)+(item_damage%2)

  except KeyError: #>Expected. If enemy doesnt have any weakness
   pass

  if item_currently_being_used['elemental'] in enemy_stats['elemental_resistance']: #| Enemy elemental resistance
   item_damage=(item_damage//2)+(item_damage%2)

  try:
   if player_stats['player_has_glass_dagger']:
    item_damage*=2
  except KeyError:
   pass

  #// if item_currently_being_used['elemental'] not in enemy_stats['elemental_resistance']:   #| If enemy is not resistant to element
  enemy_stats['hp_current']-=item_damage
  print(f'The {enemy_stats['enemy_name']} takes {item_damage} damage')


  #//elif item_currently_being_used['elemental'] in enemy_stats['elemental_resistance']:  # If enemy is resistant to element
   #//enemy_stats['hp_current']-=item_currently_being_used['power_damage']//2

   #//print(f'The {enemy_stats['enemy_name']} takes {item_currently_being_used['power_damage']//2} damage')

  sleep(sleep_timer)


 if 'DEBUFF_DAMAGE' in item_currently_being_used['effect_types']:  # Item causes a debuff that does damage overtime

  if item_currently_being_used['debuff_type'] not in enemy_status:  # If enemy has not been debuffed

   if (item_currently_being_used['debuff_type'] not in enemy_stats['debuff_immunity']):    # Enemy is not immune to the debuff

    enemy_status.append(item_currently_being_used['debuff_type'])
    damage_overtime[item_currently_being_used['debuff_type']]=item_currently_being_used['power_debuff_damage']+player_stats['debuff_power_modifier']
    debuff_ends_at[item_currently_being_used['debuff_type']]=item_currently_being_used['debuff_turn_duration']+player_stats['debuff_duration_modifier']
    turn_debuff_was_applied[item_currently_being_used['debuff_type']]=turn_count
    enemy_is_debuffed_damage=True

    print(f'The enemy is now suffering from a {item_currently_being_used['debuff_type']}!')

   elif (item_currently_being_used['debuff_type'] in enemy_stats['debuff_immunity']):    # Enemy is immune to the debuff
    print(f'The enemy is immune to the {item_currently_being_used['debuff_type']}!')

  elif item_currently_being_used['debuff_type'] in enemy_status:   # If enemy has the same debuff type as the current item

   damage_overtime[item_currently_being_used['debuff_type']]+=((item_currently_being_used['power_debuff_damage']+player_stats['debuff_power_modifier'])//2)
   print(f'The power of the {item_currently_being_used['debuff_type']} has increased!')

  sleep(sleep_timer)


 if 'HEAL' in item_currently_being_used['effect_types']:   # Used item heals
  hp_healed=item_currently_being_used['heal_power']+player_stats['bonus_healing']
  try:
   if player_stats['player_has_blood_talisman']:
    enemy_stats['hp_current']-=hp_healed
    print('The blood talisman converts all your healing to damage!')
    print(f'The enemy took {hp_healed} damage!')

  except KeyError:
   player_stats['hp_current']+=hp_healed
   print(f'You healed {hp_healed} HP!')

  if player_stats['hp_current']>player_stats['hp_max']:   # If player heals more than max hp
   player_stats['hp_current']=player_stats['hp_max']

  sleep(sleep_timer)

 #! If any new stat debuffs, outside 'DODGE',''CRIT','ATK' and 'DEF' are added
 #! Make sure you account for them in the instensity stone section
 #! So when it is used it affects the new stat too
 if 'DEBUFF_STAT' in item_currently_being_used['effect_types']:   # Item lowers enemy stats

  if item_currently_being_used['debuff_type'] not in enemy_stats['debuff_immunity']:    # Enemy immunity check

   if item_currently_being_used['debuff_type'] not in enemy_status:     # Checks if had the debuff previously
    debuff_power=item_currently_being_used['power_debuff_stat']+player_stats['debuff_power_modifier']

    if 'ATK' in item_currently_being_used['stat_decreased']:    
     enemy_attack_bonus-=debuff_power

    if 'DEF' in item_currently_being_used['stat_decreased']:
     enemy_defense_bonus-=debuff_power

    enemy_status.append(item_currently_being_used['debuff_type'])
    turn_debuff_was_applied[item_currently_being_used['debuff_type']]=turn_count    
    stat_debuff_data[item_currently_being_used['debuff_type']]=item_currently_being_used['stat_decreased']
    stat_debuff_power[item_currently_being_used['debuff_type']]=debuff_power
    debuff_ends_at[item_currently_being_used['debuff_type']]=item_currently_being_used['debuff_turn_duration']+player_stats['debuff_duration_modifier']
    enemy_is_debuffed_stat=True

    print(f'The enemy is now afflicted with {item_currently_being_used['debuff_type']}')

   elif item_currently_being_used['debuff_type'] in enemy_status:
    turn_debuff_was_applied[item_currently_being_used['debuff_type']]+=((item_currently_being_used['debuff_turn_duration']+player_stats['debuff_duration_modifier'])//2)+((item_currently_being_used['debuff_turn_duration']+player_stats['debuff_duration_modifier'])%2)

    print(f'The enemy {item_currently_being_used['debuff_type']} now lasts longer!')

  elif item_currently_being_used['debuff_type'] in enemy_stats['debuff_immunity']:
   print(f'The enemy is immune to {item_currently_being_used['debuff_type']}!')

  sleep(sleep_timer)


 if 'BUFF' in item_currently_being_used['effect_types']:

  try:
   buff_power=item_currently_being_used['buff_power']

  except KeyError:
   pass

  if 'RAGE' in item_currently_being_used['buff_types']:
   rage_buff=True

   print('Your next attack will be a critical hit!')

  if 'RUSH' in item_currently_being_used['buff_types']:
   rush_buff=True

   print('You will dodge the next enemy attack!')

  if 'ATK' in item_currently_being_used['buff_types']:
   player_attack_bonus+=buff_power
   print('Your attack has increased!')
  
  if 'DEF' in item_currently_being_used['buff_types']:
   player_defense_bonus+=buff_power
   print('Your defense has increased!')

  if 'DODGE' in item_currently_being_used['buff_types']:

   if item_currently_being_used['buff_name'] not in player_stat_buff_data.keys():

    player_dodge_bonus+=buff_power
    player_stat_buff_data[item_currently_being_used['buff_name']]=item_currently_being_used['buff_types']
    player_stat_buff_power[item_currently_being_used['buff_name']]=buff_power
    player_stat_buff_duration[item_currently_being_used['buff_name']]=item_currently_being_used['buff_duration']
    player_stat_buff_was_applied_at[item_currently_being_used['buff_name']]=turn_count
    player_is_stat_buffed=True

    print('Your dodge chance increases!')

   elif item_currently_being_used['buff_name'] in player_stat_buff_data.keys():
    player_stat_buff_duration[item_currently_being_used['buff_name']]+=(item_currently_being_used['buff_duration']//2)
    print('Your dodge bonus now last longer!')


  sleep(sleep_timer)


 if 'HEAL_DEBUFF' in item_currently_being_used['effect_types']:

  if 'ALL' in item_currently_being_used['debuff_healed']:
   player_status.clear()
   turn_count_enemy_debuffs.clear()
   damage_per_turn_enemy.clear()
   enemy_debuff_ends_at.clear()

   for debuff in enemy_stat_debuff_power.keys():
    if 'ATK' in enemy_stat_decreased[debuff]:
     player_attack_bonus+=enemy_stat_debuff_power[debuff]

    if 'DEF' in enemy_stat_decreased[debuff]:
     player_defense_bonus+=enemy_stat_debuff_power[debuff]

   enemy_stat_debuff_power.clear()
   enemy_stat_decreased.clear()
   player_is_debuffed_damage=False
   player_is_stat_debuffed=False

   print('All your debuffs wore off!')

  sleep(sleep_timer)


 if 'UNIQUE_BUFF' in item_currently_being_used['effect_types']:

  if 'DAMAGE_DEBUFF_DAMAGE' in item_currently_being_used['buff_types']: #|Increase damage off all damage debuffs

   for debuff in damage_overtime.keys():
    damage_overtime[debuff]+=int(((damage_overtime[debuff]*item_currently_being_used['buff_power'])+((damage_overtime[debuff]*item_currently_being_used['buff_power'])%1>0)))

   print('The damage of the enemy current ailments has increased!')

  if 'STRENGTH_STAT_DEBUFF' in item_currently_being_used['buff_types']: #|Increase power of all stat debuffs

   for debuff in stat_debuff_power.keys():
    debuff_power_increase=int(((stat_debuff_power[debuff]*item_currently_being_used['buff_power'])+((stat_debuff_power[debuff]*item_currently_being_used['buff_power'])%1>0)))
    stat_debuff_power[debuff]+=debuff_power_increase

    if 'ATK' in stat_debuff_data[debuff]:
     enemy_attack_bonus-=debuff_power_increase

    if 'DEF' in stat_debuff_data[debuff]:
     enemy_defense_bonus-=debuff_power_increase

    if 'DODGE' in stat_debuff_data[debuff]:
     enemy_dodge_bonus-=debuff_power_increase

    if 'CRIT' in stat_debuff_data[debuff]:
     enemy_crit_bonus-=debuff_power_increase

   print('The strength of the enemy current stat ailments has increased!')

  if 'DEBUFF_DURATION' in item_currently_being_used['buff_types']:

   for debuff in debuff_ends_at.keys():
    debuff_ends_at[debuff]*=item_currently_being_used['duration_increase_multiplier']
   
   print('The duration of all debuffs has increased!')

  sleep(sleep_timer)

 print()
 input('Press Enter to Continue'.center(format_size))


 return (
  #//enemy_stats,
  #//damage_overtime,
  #//debuff_ends_at,
  #//enemy_status,
  player_attack_bonus,
  player_defense_bonus,
  enemy_attack_bonus,
  enemy_defense_bonus,
  #//turn_debuff_was_applied,
  enemy_is_debuffed_damage,
  #//stat_debuff_data,
  #//stat_debuff_power,
  enemy_is_debuffed_stat,
  rage_buff,
  rush_buff,
  player_is_debuffed_damage,
  player_is_stat_debuffed,
  player_dodge_bonus,
  player_is_stat_buffed,
  item_used_breaks
 )
