from random import randint
from time import sleep

def enemy_skills(
  enemy_selected_skill: dict,
  player_stats: dict,
  enemy_stats: dict,
  enemy_attack_bonus: dict,
  enemy_defense_bonus: int,
  enemy_dodge_bonus: int,
  enemy_crit_bonus: int,
  enemy_has_rush: bool,
  enemy_is_stat_buffed: bool,
  player_attack_bonus: int,
  player_defense_bonus: int,
  player_dodge_bonus: int,
  player_turn_is_skipped: bool,
  debuff_at_player_duration: dict,
  stat_debuff_at_player_data: dict,
  stat_debuff_at_player_power: dict,
  debuff_at_player_was_applied_at: dict,
  player_status: list,
  player_stat_debuff_flag: bool,
  enemy_stat_buff_power: dict,
  enemy_buff_was_applied_at: dict,
  enemy_buff_duration: dict,
  enemy_buff_stat_increased: dict,
  debuff_inflicted_damage: dict,
  player_is_debuffed_damage: bool,
  turn_count: int
):
 """
 Functionality of all enemy skills

 currently_selected_skill: The currently selected enemy skill

 player_stats: Current stats of the player

 enemy_stats: Current stats of the enemy

 enemy_defense_bonus: Current enemy defense bonus

 enemy_dodge_bonus: Current enemy dodge bonus

 enemy_crit_bonus: Current enemy crit bonus

 enemy_has_rush: flag for enemy rush buff

 enemy_is_stat_buffed: flag for enemy being stat buffed

 player_attack_bonus: Current player attack bonus

 player_defense_bonus: Current player defense bonus

 player_dodge_bonus: Current player dodge bonus

 player_turn_is_skipped: Flag for skipping the player turn

 debuff_at_player_duration: Total duration in turns of debuffs applied on player

 stat_debuff_at_player_data: Which stats the debuff on player have lowered

 stat_debuf_at_player_power: How much the debuff lowered the player stats

 debuff_at_player_was_applied_at: Turn in which debuffs were applied on the player

 debuff_inflicted_damage: Dict with the damage of active enemy debuffs

 player_is_debuffed_damage: Player has damaging debuffs flag

 turn_coun: Current turn count

 player_status: current player status list

 player_stat_debuff_flag: Flag to check if player is stat debuffed

 return: Updated stat modifiers from both player and enemy
 """

 sleep_timer=0.5

 skill_success_chance=randint(1,100)
 skill_fail_chance=randint(1,100)

 perma_stat_debuff_flag=True #! Shit solution for a bullshit problem

 print(enemy_selected_skill['use_message'])

 if 'DAMAGE' in enemy_selected_skill['effects']:

  if enemy_selected_skill['accuracy']>=skill_success_chance:
   skill_damage=enemy_selected_skill['damage']

   #//try:
    #//if enemy_selected_skill['affected_by_defense']:
     #//skill_damage-=(player_stats['defense']+player_defense_bonus)

   #//except KeyError:
    #//pass

   #//try:
    #//critical_hit_check=randint(1,100)
    #//if (enemy_selected_skill['natural_crit_chance']+enemy_stats['critical_chance'])>=critical_hit_check:
     #//skill_damage*=2
     #//print('CRITICAL HIT!')
   #//except KeyError:
    #//pass

   try:
    if player_stats['player_has_glass_dagger']:
     skill_damage*=2
   except KeyError:
    pass

   player_stats['hp_current']-=skill_damage
   print(f'You took {skill_damage} damage!')

   player_stats['player_has_taken_damage_this_turn']=True

  else:
   print('The enemy attack missed!')

  sleep(sleep_timer)


 if 'DEBUFF_STAT_ENEMY' in enemy_selected_skill['effects']:

  if enemy_selected_skill['stat_debuff_enemy_chance']>=skill_fail_chance:
   debuff_power=enemy_selected_skill['stat_debuff_enemy_power']

   if 'DEF' in enemy_selected_skill['stat_decreased']:
    enemy_defense_bonus-=debuff_power
    print('The enemy defense has been lowered!')

  sleep(sleep_timer)


 if 'DEBUFF_STAT_PLAYER' in enemy_selected_skill['effects']:

  if enemy_selected_skill['debuff_apply_chance']>=skill_success_chance:
   stat_decreased_value=enemy_selected_skill['stat_debuff_power']

   try: 
    #! Mysteriously, when using try and except properly, for some reason
    #! It returns a 'integer value' error.
    #! I tried fixing but it refused to budge even tho I wrote and re-wrote everything several times
    #! So fuck you python, I will be a caveman if that's what you want!!!
    #TODO Try to do this the "correct way" again
    #TODO Hopefully the update to python 3.13 fixed the issue I had
    if enemy_selected_skill['debuff_type'] in player_status:
     perma_stat_debuff_flag=False
   except KeyError:
    pass

   #//if enemy_selected_skill['debuff_type'] not in player_status:
   if perma_stat_debuff_flag:
    if 'ATK' in enemy_selected_skill['stat_decreased']:

     try:
      if player_stats['cant_lower_player_attack']:
       print('You are immune to the attack drop!')
     except KeyError:
      player_attack_bonus-=stat_decreased_value
      print('Your attack has been lowered!')

    if 'DEF' in enemy_selected_skill['stat_decreased']:
     player_defense_bonus-=stat_decreased_value
     print('Your defenser has been lowered!')

    if 'DODGE' in enemy_selected_skill['stat_decreased']:

     try:
      if player_stats['cant_lower_player_dodge']:
       print('You are immune to the dodge drop!')
     except KeyError:
      player_dodge_bonus-=stat_decreased_value
      print('Your dodge chance has decreased!')

   try:
    if enemy_selected_skill['debuff_type'] not in player_status:
     debuff_at_player_duration[enemy_selected_skill['debuff_type']]=enemy_selected_skill['stat_debuff_duration']
     stat_debuff_at_player_data[enemy_selected_skill['debuff_type']]=enemy_selected_skill['stat_decreased']
     stat_debuff_at_player_power[enemy_selected_skill['debuff_type']]=stat_decreased_value
     debuff_at_player_was_applied_at[enemy_selected_skill['debuff_type']]=turn_count
     player_status.append(enemy_selected_skill['debuff_type'])
     player_stat_debuff_flag=True

     print(f'You are now afflicted with {enemy_selected_skill['debuff_type']}!')

    elif enemy_selected_skill['debuff_type'] in player_status:
     debuff_at_player_duration[enemy_selected_skill['debuff_type']]+=(enemy_selected_skill['stat_debuff_duration']//2)+(enemy_selected_skill['stat_debuff_duration']%2>0)
     print(f'The {enemy_selected_skill['debuff_type']} now lasts longer!')

   except KeyError:
    pass

  sleep(sleep_timer)


 if 'BUFF_ENEMY_STAT' in enemy_selected_skill['effects']:

  if enemy_selected_skill['buff_apply_chance']>=skill_success_chance:
   try:
    stat_buff_power=enemy_selected_skill['buff_power']
   except KeyError:
    pass

   if 'ATK' in enemy_selected_skill['stat_increased']:
    enemy_attack_bonus+=stat_buff_power
    print('The enemy attack has increased!')

   if 'DEF' in enemy_selected_skill['stat_increased']:
    enemy_defense_bonus+=stat_buff_power
    print('The enemy defense has increased!')

   if 'RUSH' in enemy_selected_skill['stat_increased']:
    enemy_has_rush=True
    print('The enemy will dodge the next attack!')

   if 'DODGE' in enemy_selected_skill['stat_increased']:
    enemy_dodge_bonus+=stat_buff_power
    print('The enemy dodge chance has increased!')

   if 'CRIT' in enemy_selected_skill['stat_increased']:
    enemy_crit_bonus+=stat_buff_power
    print('The enemy critical chance has increased!')

   try:
    if enemy_selected_skill['buff_type'] not in enemy_buff_was_applied_at.keys():
     enemy_stat_buff_power[enemy_selected_skill['buff_type']]=stat_buff_power
     enemy_buff_was_applied_at[enemy_selected_skill['buff_type']]=turn_count
     enemy_buff_duration[enemy_selected_skill['buff_type']]=enemy_selected_skill['buff_duration']
     enemy_buff_stat_increased[enemy_selected_skill['buff_type']]=enemy_selected_skill['stat_increased']
     enemy_is_stat_buffed=True

    elif enemy_selected_skill['buff_type'] in enemy_buff_was_applied_at.keys():
     enemy_buff_duration[enemy_selected_skill['buff_type']]=(enemy_selected_skill['buff_duration']//2)+(enemy_selected_skill['buff_duration']%2>0)

   except KeyError:
    pass

  sleep(sleep_timer)


 if 'DEBUFF_PLAYER_DAMAGE' in enemy_selected_skill['effects']:

  if enemy_selected_skill['damage_debuff_apply_chance']>=skill_success_chance:
   debuff_power=enemy_selected_skill['debuff_damage']
   if enemy_selected_skill['debuff_type_damage'] not in player_stats['player_immunity']:

    if enemy_selected_skill['debuff_type_damage'] not in player_status:

     debuff_inflicted_damage[enemy_selected_skill['debuff_type_damage']]=debuff_power
     player_status.append(enemy_selected_skill['debuff_type_damage'])
     debuff_at_player_was_applied_at[enemy_selected_skill['debuff_type_damage']]=turn_count
     debuff_at_player_duration[enemy_selected_skill['debuff_type_damage']]=enemy_selected_skill['damage_debuff_duration']
     player_is_debuffed_damage=True

     print(f'You now have the {enemy_selected_skill['debuff_type_damage']} debuff!')

    elif enemy_selected_skill['debuff_type_damage'] in player_status:
     debuff_inflicted_damage[enemy_selected_skill['debuff_type_damage']]+=debuff_power//2
     print(f'The {enemy_selected_skill['debuff_type_damage']} is now stronger!')

   elif enemy_selected_skill['debuff_type_damage'] in player_stats['debuff_immunity']:
    print('You are immune to the debuff!')

  else:
   try:
    print(enemy_selected_skill['damage_debuff_miss_message'])

   except KeyError:
    pass


 if 'DEBUFF_UNIQUE_PLAYER' in enemy_selected_skill['effects']:
  if enemy_selected_skill['debuff_apply_chance_unique']>=skill_success_chance:

   if enemy_selected_skill['unique_debuff']=='SKIP_TURN':
    player_turn_is_skipped=True
    player_status.append('SKIP_TURN')
    print('Your next turn will be skipped!')


 return (
  enemy_attack_bonus,
  enemy_defense_bonus,
  enemy_dodge_bonus,
  enemy_crit_bonus,
  enemy_has_rush,
  enemy_is_stat_buffed,
  player_attack_bonus,
  player_defense_bonus,
  player_dodge_bonus,
  player_stat_debuff_flag,
  player_is_debuffed_damage,
  player_turn_is_skipped
 )
