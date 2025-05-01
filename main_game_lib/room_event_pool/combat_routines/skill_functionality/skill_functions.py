from random import randint
from ..combat_interface import print_line,display
from time import sleep
from ...shop_routine import relic_player_stat_changes

#*DONE eparate both random values for success of debuff opponnent
#*DONE and success value for player getting himself debuffed
#*DONE add the checks for skill on cooldown
#*DONE check which things need to be returned which not
#*DONE add sleeps in between all

def basic_character_skills(
                           current_player_character : dict,
                           format_size : int,
                           enemy_steal_chance : int,
                           skill_being_used : dict,
                           enemy_has_been_stolen : bool,
                           item_stolen_type,
                           item_to_be_stolen,
                           player_stats : dict,
                           enemy_stats : dict
                           ):
 """
 Function containing the execution of the classes basic skills

 current_player_character: Set containing bool values to check which character the player is

 format_size: Integer value used for line generation, centering and so on

 enemy_steal_chance: Integer value used for the chances of the player successfully stealing

 skill_being_used: contains info to the relevant/currently used skill

 enemy_has_been_stolen: Bool value that tracks if the enemy has or not been stolen yet

 item_stolen_type: Type of the item to be stolen

 item_to_be_stolen: Item the enemy is currently carrying

 player_stats: Current player stats
 """

 sleep_timer=0.5

 if current_player_character['steal']==True:   # Player is thief
  steal_check=randint(0,enemy_steal_chance)

  print('You sneak upon your opponent\nand try to steal something from it')

  if (skill_being_used['steal_sucess_chance']+player_stats['luck'])>=steal_check and enemy_has_been_stolen==False:   # If steal is a sucess and enemy has not been stolen yet
   display('SUCESS',format_size)
   sleep(sleep_timer)

   #TODO// Change these to check the type of the item using the 'type' method
   #! That would not actually work due to relics also being dicts, thus making this method necessary anyways
   if item_stolen_type=='GOLD':
    print(f'You have stolen {item_to_be_stolen} gold')
    sleep(sleep_timer)

    player_stats['money']+=item_to_be_stolen

   elif item_stolen_type=='ITEM':
    print(f'You have stolen a {item_to_be_stolen['name']}')

    player_stats['inventory'].append(item_to_be_stolen)
    #//del item_to_be_stolen #*debug

   elif item_stolen_type=='RELIC':
    print(f'You have stolen a {item_to_be_stolen['name']}')

    relic_player_stat_changes(
     item_to_be_stolen,
     player_stats
    )

    player_stats['relics'].append(item_to_be_stolen)

   # I am somewhat confused, but for some reason the check only changed and passed through like this
   # I really have no idea why it had to be like this, but it works I guess - 03/08/2024
   enemy_stats['enemy_has_been_stolen']=True


  elif (skill_being_used['steal_sucess_chance']+player_stats['luck'])<steal_check and enemy_has_been_stolen==False:  # If steal fails

   display('FAILURE',format_size)
   sleep(sleep_timer)
   print('The enemy noticed your sneaking!')
   sleep(sleep_timer)
   print('You quickly step away from them!')
   sleep(sleep_timer)

  elif enemy_has_been_stolen==True:  # If enemy has been stolen before
   print('This enemy has nothing of value to steal anymore')


  #//return player_stats,enemy_stats


 elif current_player_character['parry']==True:  # Player is knight

  print('is knight')


 elif current_player_character['berserk']==True:  # Player is beast

  print('is beast')


 return None#//player_stats,enemy_stats 



def acquired_skill_routine(currently_selected_skill : dict,
                           player_stats : dict,#*//debug
                           enemy_stats :dict,
                           current_player_status : list,
                           current_enemy_status : list,
                           player_attack_bonus : int,
                           player_defense_bonus : int,
                           enemy_attack_bonus : int,
                           enemy_defense_bonus : int,
                           format_size : int,
                           turn_count : int,
                           damage_per_turn_player : dict,
                           turn_count_player_debuffs : dict,
                           debuff_total_duration_player : dict,
                           enemy_is_debuffed_damage : bool,
                           player_self_inflicted_debuffs_turn_count : dict,
                           player_self_inflicted_debuffs_damage : dict,
                           player_is_debuffed_damage : bool,
                           player_self_debuff_ends_at : dict,
                           player_stat_debuff_power: dict,
                           player_stat_debuff_data: dict,
                           enemy_is_debuffed_stat: bool,
                           player_self_inflicted_debuffs_stat_power: dict,
                           player_self_debuff_stats_decreased: dict,
                           player_is_stat_debuffed: bool,
                           turn_skills_enter_cooldown: dict,
                           skip_player_turn: bool,
                           player_has_rush: bool,
                           current_enemy_buffs_power: dict,
                           enemy_buffs_total_duration: dict,
                           enemy_buffs_stat_increased: dict,
                           enemy_buff_was_applied_at: dict,
                           enemy_dodge_bonus: int,
                           enemy_is_stat_buffed: bool,
                           player_stat_buff_data: dict,
                           player_stat_buff_power: dict,
                           player_stat_buff_duration: dict,
                           player_stat_buff_was_applied_at: dict,
                           player_is_stat_buffed: bool,
                           player_crit_bonus: int,
                           player_dodge_bonus: int,
                           enemy_crit_bonus: int,
                           player_has_rage: bool
                           ):
 """
 Contains and executes the effects of skills the player uses in combat

 currently_selected_skill:
   skill the player has elected to use now

 player_stats:
   Current player stats that may be altered

 enemy_stats:
   Current enemy stats that may, and most likely will, be altered

 current_player_status:
   Current player status that may be altered

 current_enemy_status:
   Current enemy status that may be altered

 player_attack_bonus:
   active buffs/modifiers on player attack

 player_defense_bonus:
   active buffs/modifiers on player defense

 enemy_attack_bonus:
   active buffs/modifiers on enemy attack

 enemy_defense_bonus:
   active buffs/modifiers on enemy defense

 format_size:
   Integer value used for line generation and text alignment

 turn_count:
   Current turn count

 damage_per_turn_player:
   Current player active debuff damage values

 turn_count_player_debuffs:
   Contains the turn number in which each debuff was applied on the enemy by the player

 debuff_total_duration_player:
   Contains the total turn count duration

 enemy_is_debuffed_damage:
   Logic check to verify if enemy has any debuffs applied

 player_self_inflicted_debuffs_turn_count:
   Contains the turn count for any self inflicted player debuff

 player_is_debuffed_damage:
   Flag for the player being under the effect of a damage debuff

 player_self_debuff_ends_at:
   Contains the max duration for enemy debuffs

 player_self_inflicted_debuffs_stat_power:
   Stores the values a stat debuff has decreased from the player stats

 player_self_debuff_stats_decreased:
   Stores which 

 player_is_stat_debuffed:
   Flag that checks if the player is debuffed

 turn_skills_enter_cooldown:
   Dict containing which turn used skills entered cooldown

 skip_player_turn:
   Flag to skip or not the player turn

 player_has_rush:
   Flag for the rush buff on player

 current_enemy_buffs_power:
   Power of active enemy buffs

 enemy_buffs_total_duration:
   Duration of active enemy buffs

 enemy_buffs_stat_increased:
   Stats affected by current active enemy buffs

 enemy_buff_was_applied_at:
   When active enemy debuffs were applied

 enemy_dodge_bonus:
   Current enemy dodge bonus

 enemy_is_stat_buffed:
   Enemy has a stat debuff flag

 player_stat_buff_data:
   Player active buffs increased stats

 player_stat_buff_power:
   Active player buffs power

 player_stat_buff_duration:
   Active player buffs duration

 player_stat_buff_was_applied_at:
   When active player buffs were applied

 player_is_stat_buffed:
   Player has a stat buff flag

 player_crit_bonus:
   Current player critical chance bonus

 player_dodge_bonus:
   Current player dodge chance bonus

 enemy_crit_bonus:
   Current enemy critical chance bonus

 player_has_rage:
   Player has rage buff flag

 return:
   Return player and enemy stat modifiers and debuff flags
 """

 sleep_timer=0.3
 fail_message_print_flag=False #! This is a shitty way to do this, too bad!
 skill_success_check=(randint(1,100)-player_stats['luck'])
 skill_fail_check=(randint(1,100)-player_stats['luck'])

 try:
  if player_stats['frostbite_does_damage'] and currently_selected_skill['debuff_type']=='FROSTBITE':

   if 'DEBUFF_DAMAGE' not in currently_selected_skill['effect_types']:
    currently_selected_skill['effect_types'].append('DEBUFF_DAMAGE')
    currently_selected_skill['effect_types'].remove('DEBUFF_STAT')

   currently_selected_skill['debuff_power']=5
   currently_selected_skill['debuff_duration']=3
  
  elif not player_stats['frostbite_does_damage'] and currently_selected_skill['debuff_type']=='FROSTBITE':

   if 'DEBUFF_DAMAGE' in currently_selected_skill['effect_types']:
    currently_selected_skill['effect_types'].remove('DEBUFF_DAMAGE')
    currently_selected_skill['effect_types'].append('DEBUFF_STAT')
 
 except KeyError:
  pass
 #//if currently_selected_skill['skill_is_in_cooldown'] is False:

 print(currently_selected_skill['use_message'])

 print_line(format_size)

 if 'BUFF' in currently_selected_skill['effect_types']:

  try:
   if 'PLAYER_TAKEN_DAMAGE' in currently_selected_skill['activation_condition_type']:

    if player_stats['player_has_taken_damage_this_turn']:
     currently_selected_skill['buff_apply_chance']=100
    else:
     currently_selected_skill['buff_apply_chance']=0

  except KeyError:
   pass

  if currently_selected_skill['buff_apply_chance']>=skill_success_check:
   
   try: #> Treats skills that give buffs like rush that dont have any power
    buff_power=currently_selected_skill['buff_power']

   except KeyError:
    pass

   if 'ATK' in currently_selected_skill['stat_increased']:
    player_attack_bonus+=buff_power
    print(f'Your attack has increased by {buff_power}')
    #//sleep(sleep_timer)


   if 'DEF' in currently_selected_skill['stat_increased']:
    player_defense_bonus+=buff_power
    print(f'Your defense has increased by {buff_power}')
    #//sleep(sleep_timer)


   if 'RUSH' in currently_selected_skill['stat_increased']:
    player_has_rush=True
    print(f'The next enemy attack will be dodged!')
    #//sleep(sleep_timer)


   if 'RAGE' in currently_selected_skill['stat_increased']:
    player_has_rage=True
    print(f'Your next attack will be a critical hit!')


   if 'CRIT' in currently_selected_skill['stat_increased']:
    print(f'Your critical hit chance increases by {buff_power}%')
    #//sleep(sleep_timer)

    player_crit_bonus+=buff_power
    player_stat_buff_data[currently_selected_skill['buff_type']]=[]
    player_stat_buff_data[currently_selected_skill['buff_type']].append('CRIT')
    player_stat_buff_power[currently_selected_skill['buff_type']]=buff_power
    player_stat_buff_duration[currently_selected_skill['buff_type']]=currently_selected_skill['buff_duration']
    player_stat_buff_was_applied_at[currently_selected_skill['buff_type']]=turn_count
    player_is_stat_buffed=True

   
   if 'DODGE' in currently_selected_skill['stat_increased']:
    print(f'Your dodge chance increases by {buff_power}%')

    player_dodge_bonus+=buff_power
    player_stat_buff_data[currently_selected_skill['buff_type']]=[]
    player_stat_buff_data[currently_selected_skill['buff_type']].append('DODGE')
    player_stat_buff_power[currently_selected_skill['buff_type']]=buff_power
    player_stat_buff_duration[currently_selected_skill['buff_type']]=currently_selected_skill['buff_duration']
    player_stat_buff_was_applied_at[currently_selected_skill['buff_type']]=turn_count
    player_is_stat_buffed=True

   sleep(sleep_timer)

  else:
   try:
    print(currently_selected_skill['message_skill_fail'])

   except KeyError:
    pass


 if 'DAMAGE_SELF' in currently_selected_skill['effect_types']:

  if currently_selected_skill['self_damage_chance']>=skill_fail_check:
   self_damage=currently_selected_skill['self_damage_power']

   player_stats['hp_current']-=self_damage #*debug
   print(f'You have taken {self_damage} damage')
   sleep(sleep_timer)


 if 'DEBUFF_DAMAGE' in currently_selected_skill['effect_types']:

  if currently_selected_skill['debuff_apply_chance_enemy']>=skill_success_check:
   debuff_damage=currently_selected_skill['debuff_power']+player_stats['debuff_power_modifier']

   if currently_selected_skill['debuff_type'] in enemy_stats['debuff_immunity']:
    print(f'The enemy is immune to the {currently_selected_skill['debuff_type']}!')
    
   else:
    if currently_selected_skill['debuff_type'] not in current_enemy_status:

     try:
      debuff_total_duration_player[currently_selected_skill['debuff_type']]=currently_selected_skill['debuff_duration']+player_stats['debuff_duration_modifier']
      current_enemy_status.append(currently_selected_skill['debuff_type'])
      damage_per_turn_player[currently_selected_skill['debuff_type']]=debuff_damage
      turn_count_player_debuffs[currently_selected_skill['debuff_type']]=turn_count
      enemy_is_debuffed_damage=True

      print(f'The enemy now suffers from {currently_selected_skill['debuff_type']}!')

     except KeyError:
      print(currently_selected_skill['message_skill_fail'])

    elif currently_selected_skill['debuff_type'] in current_enemy_status:

     damage_per_turn_player[currently_selected_skill['debuff_type']]+=(debuff_damage//2)+(debuff_damage%2)
     print(f'The {currently_selected_skill['debuff_type']} increases in power!')

    #//elif currently_selected_skill['debuff_apply_chance_enemy']>=skill_success_check and currently_selected_skill['debuff_type'] in enemy_stats['debuff_immunity']: # Enemy is immune to the debuff
     #//print(f'The enemy is immune to the {currently_selected_skill['debuff_type']}!')

   sleep(sleep_timer)


 if 'DEBUFF_SELF' in currently_selected_skill['effect_types']:

  if currently_selected_skill['debuff_apply_chance_self']>=skill_fail_check:
   if currently_selected_skill['debuff_type'] not in player_stats['player_immunity']:
    self_debuff_damage=currently_selected_skill['self_debuff_power']
    print(currently_selected_skill['use_message_hurt_self'])
    sleep(sleep_timer)

    if currently_selected_skill['debuff_type'] not in current_player_status:

     current_player_status.append(currently_selected_skill['debuff_type'])
     player_self_inflicted_debuffs_turn_count[currently_selected_skill['debuff_type']]=turn_count
     player_self_inflicted_debuffs_damage[currently_selected_skill['debuff_type']]=self_debuff_damage
     player_self_debuff_ends_at[currently_selected_skill['debuff_type']]=currently_selected_skill['self_debuff_duration']
     player_is_debuffed_damage=True

     print(f'You now suffer from a {currently_selected_skill['debuff_type']}')

    elif currently_selected_skill['debuff_type'] in current_player_status:

     player_self_inflicted_debuffs_damage[currently_selected_skill['debuff_type']]+=(self_debuff_damage//2)+(self_debuff_damage%2)

     print(f'Your own {currently_selected_skill['debuff_type']} now hurts more!')

   else:
    print(f'You are immune to {currently_selected_skill['debuff_type']}')

   sleep(sleep_timer)


 if 'DAMAGE' in currently_selected_skill['effect_types']:

  try:
   if 'TURN_SPECIFIC' in currently_selected_skill['activation_condition_type']:

    if turn_count==currently_selected_skill['turn_for_activation']:
     currently_selected_skill['attack_success_chance']=100
    else:
     currently_selected_skill['attack_success_chance']=0

  except KeyError:
   pass

  if currently_selected_skill['attack_success_chance']>=skill_success_check:

   try:
    if (currently_selected_skill['last_turn_used']==0) or (currently_selected_skill['last_turn_used']==(turn_count-1)):
     currently_selected_skill['damage_power']+=currently_selected_skill['damage_increased']
     currently_selected_skill['last_turn_used']=turn_count

    else:
     currently_selected_skill['damage_power']=currently_selected_skill['original_damage']

   except KeyError:
    pass


   try:
    if currently_selected_skill['defense_for_damage']:
     skill_damage=player_stats['defense']+player_defense_bonus
   except KeyError:
    skill_damage=currently_selected_skill['damage_power']


   try:
    if currently_selected_skill['debuff_for_bonus_damage'] in current_enemy_status:
     skill_damage+=currently_selected_skill['bonus_damage_from_debuff']
   except KeyError:
    pass


   try:
    if turn_count%currently_selected_skill['turn_divisor']==0:
     skill_damage+=currently_selected_skill['damage_mod_for_turns']

    elif turn_count%currently_selected_skill['turn_divisor']==1:
     skill_damage-=currently_selected_skill['damage_mod_for_turns']

   except KeyError:
    pass


   if currently_selected_skill['elemental'] in player_stats['elemental_damage_bonus']:
    skill_damage+=(skill_damage//2)+(skill_damage%2)

   try:
    if currently_selected_skill['elemental'] in enemy_stats['elemental_weakness']:
     skill_damage+=(skill_damage//2)+(skill_damage%2)

   except KeyError: #>Expected. If enemy does not have elemental weakness
    pass

   if currently_selected_skill['elemental'] in enemy_stats['elemental_resistance']:
    skill_damage=(skill_damage//2)+(skill_damage%2)

   try:
    if player_stats['player_has_glass_dagger']:
     skill_damage*=2
   except KeyError:
    pass

   try:
    if player_stats['player_has_runebook_of_power']:
     skill_damage*=2
   except KeyError:
    pass

   enemy_stats['hp_current']-=skill_damage
   print(f'The enemy takes {skill_damage} damage!')
  
  else:

   try:
    if not fail_message_print_flag:
     print(currently_selected_skill['use_message_fail'])
     fail_message_print_flag=True
    
    try:
     self_damage=currently_selected_skill['damage_self']
     player_stats['hp_current']-=self_damage
     print(f'You took {self_damage} damage!')

    except KeyError:
     pass

   except KeyError:
    pass

   #//elif currently_selected_skill['elemental'] in enemy_stats['elemental_resistance']:

    #//enemy_stats['hp_current']-=currently_selected_skill['damage_power']//2

    #//print(f'The enemy takes {currently_selected_skill['damage_power']//2} damage!')

  sleep(sleep_timer)


 if 'DEBUFF_STAT' in currently_selected_skill['effect_types']:

  if currently_selected_skill['debuff_apply_chance_enemy']>=skill_success_check:

   if currently_selected_skill['debuff_type'] in enemy_stats['debuff_immunity']:
    print(f'The enemy is immune to {currently_selected_skill['debuff_type']}!')

   else:
    if currently_selected_skill['debuff_type'] not in current_enemy_status:
     stat_decrease_value=currently_selected_skill['stat_debuff_power']+player_stats['debuff_power_modifier']

     if 'ATK' in currently_selected_skill['stat_decreased']:
      enemy_attack_bonus-=stat_decrease_value

     if 'DEF' in currently_selected_skill['stat_decreased']:
      enemy_defense_bonus-=stat_decrease_value

     if 'DODGE' in currently_selected_skill['stat_decreased']:
      enemy_dodge_bonus-=stat_decrease_value

     if 'CRIT' in currently_selected_skill['stat_decreased']:
      enemy_crit_bonus-=stat_decrease_value

     current_enemy_status.append(currently_selected_skill['debuff_type'])
     player_stat_debuff_power[currently_selected_skill['debuff_type']]=stat_decrease_value
     player_stat_debuff_data[currently_selected_skill['debuff_type']]=currently_selected_skill['stat_decreased']
     turn_count_player_debuffs[currently_selected_skill['debuff_type']]=turn_count
     debuff_total_duration_player[currently_selected_skill['debuff_type']]=currently_selected_skill['stat_debuff_duration']+player_stats['debuff_duration_modifier']
     enemy_is_debuffed_stat=True

     print(f'The enemy is now afflicted with {currently_selected_skill['debuff_type']}')

    elif currently_selected_skill['debuff_type'] in current_enemy_status:
     turn_count_player_debuffs[currently_selected_skill['debuff_type']]+=((currently_selected_skill['stat_debuff_duration']+player_stats['debuff_duration_modifier'])//2)+((currently_selected_skill['stat_debuff_duration']+player_stats['debuff_duration_modifier'])%2)

     print(f'The enemy {currently_selected_skill['debuff_type']} now lasts longer!')

   sleep(sleep_timer)

  else: #| Effects that only happen IF the skill fails

   try:
    if not fail_message_print_flag:
     print(currently_selected_skill['use_message_fail'])

    if currently_selected_skill['debuff_type'] not in current_player_status:

     stat_decrease_value=currently_selected_skill['self_stat_debuff_power']

     if 'DEF' in currently_selected_skill['stat_decreased']:
      player_defense_bonus-=stat_decrease_value

     if 'DODGE' in currently_selected_skill['stat_decreased']:
      try:
       if player_stats['cant_lower_player_dodge']:
        print('You are immune to the dodge drop!')
      except KeyError:
       player_dodge_bonus-=stat_decrease_value

     current_player_status.append(currently_selected_skill['debuff_type'])
     player_self_inflicted_debuffs_stat_power[currently_selected_skill['debuff_type']]=currently_selected_skill['self_stat_debuff_power']
     player_self_inflicted_debuffs_turn_count[currently_selected_skill['debuff_type']]=turn_count
     player_self_debuff_ends_at[currently_selected_skill['debuff_type']]=currently_selected_skill['self_stat_debuff_duration']
     player_self_debuff_stats_decreased[currently_selected_skill['debuff_type']]=currently_selected_skill['stat_decreased']
     player_is_stat_debuffed=True

     print(f'You are now afflicted with {currently_selected_skill['debuff_type']}')

    elif currently_selected_skill['debuff_type'] in current_player_status:
     print(f'Your {currently_selected_skill['debuff_type']} now lasts longer!')
     player_self_inflicted_debuffs_turn_count[currently_selected_skill['debuff_type']]+=(currently_selected_skill['self_stat_debuff_duration']//2)+(currently_selected_skill['self_stat_debuff_duration']%2)

   except KeyError:
    pass


 #*DONE Add player have a stat debuff applied on itself
 #*DONE Gotta test
 if 'DEBUFF_SELF_STAT' in currently_selected_skill['effect_types']:

  if currently_selected_skill['debuff_apply_chance_self']>=skill_fail_check:
   print(currently_selected_skill['use_message_hurt_self'])
   
   try:
    if currently_selected_skill['debuff_type'] not in current_player_status:

     stat_decrease_value=currently_selected_skill['self_stat_debuff_power']

     if 'DEF' in currently_selected_skill['stat_decreased']:
      player_defense_bonus-=stat_decrease_value

     if 'DODGE' in currently_selected_skill['stat_decreased']:
      try:
       if player_stats['cant_lower_player_dodge']:
        print('You are immune to the dodge drop!')
      except KeyError:
       player_dodge_bonus-=stat_decrease_value

     current_player_status.append(currently_selected_skill['debuff_type'])
     player_self_inflicted_debuffs_stat_power[currently_selected_skill['debuff_type']]=currently_selected_skill['self_stat_debuff_power']
     player_self_inflicted_debuffs_turn_count[currently_selected_skill['debuff_type']]=turn_count
     player_self_debuff_ends_at[currently_selected_skill['debuff_type']]=currently_selected_skill['self_stat_debuff_duration']
     player_self_debuff_stats_decreased[currently_selected_skill['debuff_type']]=currently_selected_skill['stat_decreased']
     player_is_stat_debuffed=True

     print(f'You are now afflicted with {currently_selected_skill['debuff_type']}')

    elif currently_selected_skill['debuff_type'] in current_player_status:
     print(f'Your {currently_selected_skill['debuff_type']} now lasts longer!')
     player_self_inflicted_debuffs_turn_count[currently_selected_skill['debuff_type']]+=(currently_selected_skill['self_stat_debuff_duration']//2)+(currently_selected_skill['self_stat_debuff_duration']%2)

   except KeyError: #>Expected. If exception, debuff is permanent throught combat

    if 'DEF' in currently_selected_skill['stat_decreased']:
     player_defense_bonus-=currently_selected_skill['self_stat_debuff_power']

    if 'ATK' in currently_selected_skill['stat_decreased']:
     player_attack_bonus-=currently_selected_skill['self_stat_debuff_power']

   sleep(sleep_timer)


 if 'DEBUFF_SELF_SPECIAL' in currently_selected_skill['effect_types']:

  if currently_selected_skill['debuff_apply_chance_self']>=skill_fail_check:
   print(currently_selected_skill['use_message_hurt_self'])

   if currently_selected_skill['debuff_type'] not in current_player_status:

    if currently_selected_skill['debuff_type']=='SKIP_TURN':

     skip_player_turn=True
     current_player_status.append(currently_selected_skill['debuff_type'])
     print('Your next turn will be skipped!')

    if currently_selected_skill['debuff_type']=='SILENCE':

     current_player_status.append(currently_selected_skill['debuff_type'])
     player_self_inflicted_debuffs_turn_count[currently_selected_skill['debuff_type']]=turn_count
     player_self_debuff_ends_at[currently_selected_skill['debuff_type']]=currently_selected_skill['debuff_duration_self']
     print('You have been silenced!')

   else:
    print(f'You already have the {currently_selected_skill['debuff_type']} debuff!')

   sleep(sleep_timer)


 if 'DEBUFF_ENEMY_SPECIAL' in currently_selected_skill['effect_types']:

  if currently_selected_skill['debuff_apply_chance_enemy']>=skill_success_check:

   if currently_selected_skill['debuff_type'] not in current_enemy_status:

    if currently_selected_skill['debuff_type']=='SILENCE':

     current_enemy_status.append(currently_selected_skill['debuff_type'])
     turn_count_player_debuffs[currently_selected_skill['debuff_type']]=turn_count
     debuff_total_duration_player[currently_selected_skill['debuff_type']]=currently_selected_skill['debuff_duration']+player_stats['debuff_duration_modifier']
     print('The enemy has been silenced!')

   else:
    print(f'The enemy already has the {currently_selected_skill['debuff_type']} debuff')

   sleep(sleep_timer)


 if 'BUFF_ENEMY_STAT' in currently_selected_skill['effect_types']:

  if currently_selected_skill['buff_enemy_stat_chance']>=skill_fail_check:
   print(currently_selected_skill['use_message_hurt_self'])
   buff_power=currently_selected_skill['enemy_buff_power']

   if 'DODGE' in currently_selected_skill['stat_increased_enemy']:

    if currently_selected_skill['buff_type'] not in enemy_buff_was_applied_at.keys():

     #//current_enemy_status.append(currently_selected_skill['buff_type'])
     current_enemy_buffs_power[currently_selected_skill['buff_type']]=buff_power
     enemy_buffs_total_duration[currently_selected_skill['buff_type']]=currently_selected_skill['enemy_buff_duration']
     enemy_buffs_stat_increased[currently_selected_skill['buff_type']]=currently_selected_skill['stat_increased_enemy']
     enemy_buff_was_applied_at[currently_selected_skill['buff_type']]=turn_count
     enemy_dodge_bonus+=buff_power
     enemy_is_stat_buffed=True
     print('The enemy dodge chance has increased!')
    
    #*DONE Make this increase duration of buff by half the duration of the skill
    elif currently_selected_skill['buff_type'] in enemy_buff_was_applied_at.keys():
     enemy_buffs_total_duration[currently_selected_skill['buff_type']]+=(currently_selected_skill['enemy_buff_duration']//2)+(currently_selected_skill['enemy_buff_duration']%2)
     print('The enemy dodge bonus now lasts longer!')

   if 'DEF' in currently_selected_skill['stat_increased']:
    enemy_defense_bonus+=currently_selected_skill['enemy_buff_power']
    print('The enemy defense has increased!')

   sleep(sleep_timer)

 #TODO Eliminate the need for this by using the treatment given in the self debuff section
 if 'LOWER_STAT' in currently_selected_skill['effect_types']:

  if currently_selected_skill['debuff_apply_chance_self']>=skill_fail_check:
   print(currently_selected_skill['use_message_hurt_self'])

   if 'ATK' in currently_selected_skill['stat_decreased']:
    player_attack_bonus-=currently_selected_skill['debuff_power']
    print(f'Your attack has decreased by {currently_selected_skill['debuff_power']}')

   sleep(sleep_timer)


 if 'HEAL_PLAYER' in currently_selected_skill['effect_types']:

  if currently_selected_skill['heal_success_chance']>=skill_success_check:
   heal_value=currently_selected_skill['heal_power']
   heal_value+=player_stats['bonus_healing']

   player_stats['hp_current']+=heal_value
   if player_stats['hp_current']>player_stats['hp_max']:
    player_stats['hp_current']=player_stats['hp_max']

   print(f'You have healed for {heal_value} HP')

  sleep(sleep_timer)

 turn_skills_enter_cooldown[currently_selected_skill['name']]=turn_count
 currently_selected_skill['skill_is_in_cooldown']=True
 #//turn_skills_enter_cooldown[currently_selected_skill['name']]=turn_count

 '''elif currently_selected_skill['skill_is_in_cooldown'] is True:

  print(f'The {currently_selected_skill['name']} is on cooldown!')
 print()
 print('Press Enter to Continue'.center(format_size))
 input()'''


 return (
         #//player_stats,
         #//current_player_status,
         #//enemy_stats,
         #//current_enemy_status,
         player_attack_bonus,
         player_defense_bonus,
         enemy_attack_bonus,
         enemy_defense_bonus,
         #//damage_per_turn_player,
         #//turn_count_player_debuffs,
         #//debuff_total_duration_player,
         enemy_is_debuffed_damage,
         #//player_self_inflicted_debuffs_turn_count,
         #//player_self_inflicted_debuffs_damage,
         player_is_debuffed_damage,
         #//player_self_debuff_ends_at,
         #//player_stat_debuff_power,
         #//player_stat_debuff_data,
         enemy_is_debuffed_stat,
         #//player_self_inflicted_debuffs_stat_power,
         #//player_self_debuff_stats_decreased,
         player_is_stat_debuffed,
         skip_player_turn,
         player_has_rush,
         enemy_dodge_bonus,
         enemy_is_stat_buffed,
         player_is_stat_buffed,
         player_crit_bonus,
         player_dodge_bonus,
         enemy_crit_bonus,
         player_has_rage
       )