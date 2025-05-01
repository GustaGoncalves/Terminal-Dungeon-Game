from .combat_interface import *
from .usable_item_effects import *
from .skill_functionality import *
from .enemy_sheet import *
from random import randint
from time import sleep
import os

# NOTE all sleep commands are delays, that are to compensate the lack of actual visuals - 29/07/2024
#*DONE Refactor block system to: If player is already blocking, choosing block does nothing (Does not waste turn)

def combat_base(size_format_combat_screen: int,
                player_combat_stats: dict,
                current_enemy_stats: dict,
                mini_boss: bool=False):
 """
 Base combat loops where player stats are used and altered alongside the enemy being fought

 size_format_combat_screen: Integer value used for lines and centering

 player_combat_stats: Current player stats that will be used and altered

 current_enemy_stats: Current loaded enemy stats

 mini_boss: Logical check to see if the loaded enemy is a mini-boss. Default is False.

 return: None
 """

 # Due to me using the counters and damage variables within the checks to reset or extend them
 # This means they need to be all loaded here -23/07/2024

 #// In the end there will be lots of flags for player stuff
 #// Need to turn the buff/debuff flags into a dict for easier comprehension
 #// Fix block extending duration message

 #> Player load region
 #damage debuffs
 damage_per_turn_player={}

 #stat bonuses
 current_player_attack_bonus=0
 current_player_defense_bonus=0
 current_player_dodge_bonus=0
 current_player_crit_bonus=0

 attack_decrease_from_block_player=0
 current_player_status=[]
 turn_count_player_block=0

 #debuff duration
 turn_count_player_debuffs={}   
 debuff_total_duration_player={}

 #stat debuffs
 player_stat_debuff_data={}
 player_stat_debuff_power={}

 #status flags
 player_is_blocking=False
 player_is_stat_debuffed=False
 player_is_debuffed_damage=False
 player_is_stat_buffed=False
 player_has_rage=False
 player_has_rush=False
 skip_player_turn=False
 item_used_breaks=True
 first_player_attack=True

 #buffs
 player_stat_buff_data={}
 player_stat_buff_power={}
 player_stat_buff_duration={}
 player_stat_buff_was_applied_at={}

 #> End region

 #> Enemy load region
 #damage debuffs
 damage_per_turn_enemy={}

 #bonus counters
 current_enemy_attack_bonus=0
 current_enemy_defense_bonus=0
 current_enemy_dodge_bonus=0
 current_enemy_crit_bonus=0
 attack_decrease_from_block_enemy=0

 current_enemy_status=[]
 turn_count_enemy_block=0

 #debuff duration
 turn_count_enemy_debuffs={}   
 enemy_debuff_ends_at={}
 
 #status flags
 enemy_is_blocking=False
 enemy_is_debuffed_damage=False
 enemy_is_debuffed_stat=False
 enemy_is_stat_buffed=False
 enemy_has_rush=False

 #stat debuffs
 enemy_stat_debuff_power={}
 enemy_stat_decreased={}

 #buffs
 enemy_buffs_power={}
 enemy_buffs_duration={}
 enemy_buffs_stat_increased={}
 enemy_buff_was_applied_at={}

 enemy_action=''
 #> End region

 turn_count=1   # Seeing something start at one instead of zero is a bizarre experience
 #//ai_control_value=1 #> Used to control and create AI routines for enemies more easily
 sleep_timer=0.5
 turn_skills_enter_cooldown={} # This is the worst

 # This sucks
 stat_debuffs={
  'FROSTBITE':[
   'DEF'
  ],
  'SLOW':[
   'DODGE'
  ],
  'WOUNDED':[
   'ATK'
  ]
 }
 #//defense_decrease_debuff=[
  #//'FROSTBITE'
 #//]
 damage_debuffs=[
  'BURN',
  'POISON'
 ]

 try:
  if player_combat_stats['player_has_sword_scope']:
   enemy_can_dodge=False

 except KeyError:
  enemy_can_dodge=True

 player_combat_stats['player_has_taken_damage_this_turn']=False

 #//try:
  #//if player_combat_stats['player_has_runebook_of_power']:
   #//cooldown_multiplier+=1
 #//except KeyError:
  #//pass
 #//skill_index_in_inventory={} #! Bad solution, but whatever

 # Stores original player stats that could be altered during combat
 # They will be reseted later after combat has finished if the player won - 29/07/2024
 #! Obsolete
 #//player_original_defense=player_combat_stats['defense']
 #//original_player_attack=player_combat_stats['attack_current']

 ai_test=0   #* Debug

 while True:
  os.system('cls')
  damage_dealt=0
  enemy_damage=0
  crit_check=randint(1,100)
  dodge_check=randint(1,100)
  
  try:
   if player_combat_stats['has_ebony_scarf'] and (turn_count%4)==0:
    current_player_dodge_bonus+=30

  except KeyError:
   pass

  try:

   if player_combat_stats['player_has_rolling_pendulum'] and turn_count%2==0:
    current_player_defense_bonus+=8 #> 8 to acount for previous bonus
    current_player_attack_bonus-=8

   elif player_combat_stats['player_has_rolling_pendulum'] and turn_count%2==1:
    if turn_count>1: #>Accounts for previous bonus
     current_player_defense_bonus-=8
     current_player_attack_bonus+=8
    else:
     current_player_defense_bonus-=4
     current_player_attack_bonus+=4

  except KeyError:
   pass

  try:
   if player_combat_stats['player_has_hermes_cronometer']:

    if turn_count==1:
     current_player_attack_bonus+=10

    else:
     if turn_count<12:
      current_player_attack_bonus-=2

  except KeyError:
   pass

  #>Player Turn Region
  # Player Interaction loop, used for when the player decides to mess with the inventory
  # Gave me more headaches then it should - 31/07/2024
  while True:

   os.system('cls')

   combat_screen(
    player_combat_stats,       
    current_enemy_stats,
    size_format_combat_screen,
    current_player_status,
    current_enemy_status,
    current_player_attack_bonus,
    current_player_defense_bonus,
    current_player_dodge_bonus,
    current_enemy_attack_bonus,
    current_enemy_defense_bonus,
    turn_count,
    player_has_rage,
    player_has_rush,
    current_enemy_dodge_bonus,
    current_player_crit_bonus,
    enemy_has_rush,
    current_enemy_crit_bonus
   )
   if not skip_player_turn:
    player_combat_action=integer_check('Your action: ',size_format_combat_screen)
    print_line(size_format_combat_screen)

    #* Player action section starts here

    match player_combat_action:

     case 1:     #| Player attacks

      print('You strike!')
      sleep(sleep_timer)

      if ((current_enemy_stats['dodge_chance']+current_enemy_dodge_bonus-player_combat_stats['luck'])>=dodge_check or enemy_has_rush) and enemy_can_dodge:  # This WILL be annoying
       print('The enemy has avoided your strike!')
       enemy_has_rush=False

      else:
       # Damage calculation has been improved
       # Now defense works against critical hits - 16/08/2024
       try:
        if player_combat_stats['player_attack_is_halved']:
         damage_dealt+=((player_combat_stats['attack_current']//2)+(player_combat_stats['attack_current']%2>0))+current_player_attack_bonus

       except KeyError:
        damage_dealt+=player_combat_stats['attack_current']+current_player_attack_bonus

       try:
        if player_combat_stats['first_attack_does_extra_damage']:
         if first_player_attack:
          damage_dealt+=12
          first_player_attack=False
       except KeyError:
        pass


       damage_dealt-=current_enemy_stats['defense']+current_enemy_defense_bonus#-((int((current_enemy_stats['defense']+current_enemy_defense_bonus)*player_combat_stats['armor_piercing']))+(((current_enemy_stats['defense']+current_enemy_defense_bonus)*player_combat_stats['armor_piercing'])%1>0)))

       if current_enemy_stats['defense']+current_enemy_defense_bonus>0: #| Armor Piercing
        damage_dealt+=((int((current_enemy_stats['defense']+current_enemy_defense_bonus)*player_combat_stats['armor_piercing']))+(((current_enemy_stats['defense']+current_enemy_defense_bonus)*player_combat_stats['armor_piercing'])%1>0))

       try:
        if player_combat_stats['player_has_crystal_coin']:
         damage_dealt+=int(((player_combat_stats['money']*0.1)+((player_combat_stats['money']*0.1)%1>0)))

       except KeyError:
        pass

       if (player_combat_stats['critical_chance']+current_player_crit_bonus+player_combat_stats['luck'])>=crit_check or player_has_rage:     # TF2 random crit moment 
        damage_dealt*=2
        print('CRITICAL HIT!')
        sleep(sleep_timer)
        player_has_rage=False


       for debuff in player_combat_stats['debuff_on_attack']:
        debuff_success_check=randint(1,100)

        if (10+player_combat_stats['luck'])>=debuff_success_check:

         if debuff not in current_enemy_status:

          if debuff in damage_debuffs:
           current_enemy_status.append(debuff)
           turn_count_player_debuffs[debuff]=turn_count
           debuff_total_duration_player[debuff]=(3+player_combat_stats['debuff_duration_modifier'])
           damage_per_turn_player[debuff]=(4+player_combat_stats['debuff_power_modifier'])
           enemy_is_debuffed_damage=True

          elif debuff in stat_debuffs.keys():
           current_enemy_status.append(debuff)
           turn_count_player_debuffs[debuff]=turn_count
           #//player_stat_debuff_power[debuff]=(1+player_combat_stats['debuff_power_modifier'])
           player_stat_debuff_data[debuff]=[]
           debuff_total_duration_player[debuff]=(2+player_combat_stats['debuff_duration_modifier'])
           enemy_is_debuffed_stat=True

           if 'DEF' in stat_debuffs[debuff]:
            current_enemy_defense_bonus-=(1+player_combat_stats['debuff_power_modifier'])
            player_stat_debuff_power[debuff]=(1+player_combat_stats['debuff_power_modifier'])

            player_stat_debuff_data[debuff].append('DEF')

           if 'DODGE' in stat_debuffs[debuff]:
            current_enemy_dodge_bonus-=(5+player_combat_stats['debuff_power_modifier'])
            player_stat_debuff_power[debuff]=(5+player_combat_stats['debuff_power_modifier'])
            player_stat_debuff_data[debuff].append('DODGE')

          print(f'Your attack inflicted {debuff} on the enemy!')

         elif debuff in current_enemy_status:
          if debuff in damage_debuffs:
           damage_per_turn_player[debuff]+=(((player_combat_stats['debuff_power_modifier']+4)//2)+((player_combat_stats['debuff_power_modifier']+4)%2))
           print(f'The enemy {debuff} is now stronger!')

          elif debuff in stat_debuffs.keys():
           debuff_total_duration_player[debuff]+=1
           print(f'The enemy {debuff} now lasts longer!')


       try:
        if player_combat_stats['player_has_glass_dagger']:
         damage_dealt*=2
       except KeyError:
        pass

       print(f'You dealt {damage_dealt} damage')
       current_enemy_stats['hp_current']-=damage_dealt

       if player_combat_stats['life_steal']>0:
        life_stolen=int(player_combat_stats['life_steal']*damage_dealt)+((player_combat_stats['life_steal']*damage_dealt)%1>0)

        try:
         if player_combat_stats['player_has_blood_talisman']:
          current_enemy_stats['hp_current']-=life_stolen
          print('The blood talisman converts the healing to damage!')
          print(f'The enemy took {life_stolen} damage')

        except KeyError: #> Expected
         player_combat_stats['hp_current']+=life_stolen
         if player_combat_stats['hp_current']>player_combat_stats['hp_max']:
          player_combat_stats['hp_current']=player_combat_stats['hp_max']

         print(f'You have siphoned {life_stolen} HP from the enemy!')

       sleep(sleep_timer)

      break


     case 2:     #| Player blocks

      try:
       if player_combat_stats['player_cant_block']:
        print('Your block has been disabled!')

      except KeyError:
       if not player_is_blocking:    
        if player_combat_stats['action_available']['steal']==True: 
         print('You retreat and brace yourself a strike!')

        elif player_combat_stats['action_available']['parry']==True:
         print('You raise your guard, changing into a defensive stance!')

        elif player_combat_stats['action_available']['berserk']==True:
         print('You tense yourself up, boosting your tolerance to attacks!')

        sleep(sleep_timer)

        print(f'Your defense increases for the next {player_combat_stats['block_duration_modifier']} turns!')

        turn_count_player_block=turn_count
        current_player_defense_bonus+=player_combat_stats['block_power']

        if player_combat_stats['block_decreases_attack']:
         attack_decrease_from_block_player=int(player_combat_stats['attack_current']*(20/100))
         current_player_attack_bonus-=attack_decrease_from_block_player

        player_is_blocking=True
        break

       else:    
        print(f'You are already blocking!')

        #turn_count_player_block+=player_combat_stats['block_duration_modifier']//2

       sleep(sleep_timer)

       #break


     case 3:    #| Case player opens inventory

      if len(player_combat_stats['inventory'])<=0:     #| If player inventory is empty
       os.system('cls')
       print('Your inventory is empty')

      else:
       while True:  # Main Inventory loop

        while True:  #? Forgot exactly what made put this one here, but it made the inventory work how I wanted

         while True:

          os.system('cls')
          print('INVENTORY'.center(size_format_combat_screen))
          print_line(size_format_combat_screen)
          item_and_skill_display(
           player_combat_stats['inventory'],
          )
          print(f'[{len(player_combat_stats['inventory'])+1}] Return')       #| Prints exit option, with number properly adapted

          player_inventory_choice=integer_check('Your choice: ')

          if player_inventory_choice>0 and player_inventory_choice<=len(player_combat_stats['inventory'])+1:

           break

          else:   
           print('Choose a valid option!')


         if player_inventory_choice==len(player_combat_stats['inventory'])+1:      #| If player decides to leave inventory
          break


         else:      #| If player chooses to use an item

          player_inventory_choice-=1 #| Decrement to use as index

          display(player_combat_stats['inventory'][player_inventory_choice]['name'],
                  size_format_combat_screen)
          print(f'{player_combat_stats['inventory'][player_inventory_choice]['description']}')
          print_line(size_format_combat_screen)


          while True:
           try:
            player_item_use_confirm=str(input(f'Use the {player_combat_stats['inventory'][player_inventory_choice]['name']}? [Y/N] ')).strip().upper()

           except ValueError:
            print('Input only Y or N')

            continue

           else:

            if player_item_use_confirm in 'YyNn':
             break

            print('Input only Y or N!')


          if player_item_use_confirm in 'Yy':    #| Player confirms the item use

           # I can't help but laugh like a dumbass looking at this
           # And then I start crying
           # Finally... a light at the end of the tunnel. Nevermind, it's worse

           (
           #//current_enemy_stats,
           #//damage_per_turn_player,
           #//debuff_total_duration_player,
           #//current_enemy_status,
           current_player_attack_bonus,
           current_player_defense_bonus,
           current_enemy_attack_bonus,
           current_enemy_defense_bonus,
           #//turn_count_player_debuffs,
           enemy_is_debuffed_damage,
           #//player_stat_debuff_data,
           #//player_stat_debuff_power,
           enemy_is_debuffed_stat,
           player_has_rage,
           player_has_rush,
           player_is_debuffed_damage,
           player_is_stat_debuffed,
           current_player_dodge_bonus,
           player_is_stat_buffed,
           item_used_breaks
           )=usable_item_effects(
            player_combat_stats['inventory'][player_inventory_choice],
            current_enemy_stats,
            current_enemy_status,
            player_combat_stats,
            current_player_status,
            size_format_combat_screen,
            current_player_attack_bonus,
            current_player_defense_bonus,
            current_enemy_attack_bonus,
            current_enemy_defense_bonus,
            turn_count,
            enemy_is_debuffed_damage,
            damage_per_turn_player,
            debuff_total_duration_player,
            turn_count_player_debuffs,
            player_stat_debuff_data,
            player_stat_debuff_power,
            enemy_is_debuffed_stat,
            player_has_rage,
            player_has_rush,
            player_is_debuffed_damage,
            player_is_stat_debuffed,
            turn_count_enemy_debuffs,
            damage_per_turn_enemy,
            enemy_debuff_ends_at,
            enemy_stat_debuff_power,
            enemy_stat_decreased,
            player_stat_buff_data,
            player_stat_buff_power,
            player_stat_buff_duration,
            player_stat_buff_was_applied_at,
            current_player_dodge_bonus,
            player_is_stat_buffed,
            item_used_breaks
           )

           if item_used_breaks:
            del player_combat_stats['inventory'][player_inventory_choice]
           break

          elif player_item_use_confirm in 'Nn':   #| Player denies using the item
           continue

        break


     case 4:    #| Case player decides to use skill

      if 'SILENCE' not in current_player_status:
       os.system('cls')
       print('SKILLS'.center(size_format_combat_screen))
       print_line(size_format_combat_screen)

       item_and_skill_display(
        player_combat_stats['skill_list']
       )
       print(f'[{len(player_combat_stats['skill_list'])+1}] Return')


       while True:
        player_skill_choice=integer_check('Your choice: ')

        if player_skill_choice>=1 and player_skill_choice<=len(player_combat_stats['skill_list'])+1:
         print_line(size_format_combat_screen)
         break

        else:
         print('Choose a valid option!')


       if player_skill_choice==1:   #| Case player choose to use their character skill

        player_skill_choice-=1   #| Decrement to use player input as the skill index

        # Massive and ugly looking, but oh well - 03/08/2024
        # Not as bad as the others - 30/08/2024
        
         #//player_combat_stats,
         #//current_enemy_stats
        basic_character_skills(
         player_combat_stats['action_available'],
         size_format_combat_screen,
         current_enemy_stats['steal_chance'],
         player_combat_stats['skill_list'][player_skill_choice],
         current_enemy_stats['enemy_has_been_stolen'],
         current_enemy_stats['steal_class'],
         current_enemy_stats['item_stolen'],
         player_combat_stats,
         current_enemy_stats
        )
        break

       elif player_skill_choice==len(player_combat_stats['skill_list'])+1:     #| Case player decides to not use any skill
        pass

       else:   #| Player chooses to use any of the other available skills
        player_skill_choice-=1

        try:
         if player_combat_stats['player_has_runebook_of_power']:
          if 'DAMAGE' in player_combat_stats['skill_list'][player_skill_choice]['effect_types']:
           cooldown_multiplier=2
          else:
           cooldown_multiplier=1
        except KeyError:
         cooldown_multiplier=1

        # This used to look worse
        # Now it's just shit - 30/08/2024 
        #//if player_combat_stats['skill_list'][player_skill_choice]['skill_is_in_cooldown'] is False:
        
        try:
         if (turn_count-turn_skills_enter_cooldown[player_combat_stats['skill_list'][player_skill_choice]['name']])>=((player_combat_stats['skill_list'][player_skill_choice]['cooldown_turn_total']*cooldown_multiplier)-player_combat_stats['cooldown_reduction']):
          player_combat_stats['skill_list'][player_skill_choice]['skill_is_in_cooldown']=False

        except KeyError: #> Expected
         player_combat_stats['skill_list'][player_skill_choice]['skill_is_in_cooldown']=False #| Avoids skills staying on cooldown forever

        except Exception as erro:
         print("This wasn't expected")
         print(erro)

        if not player_combat_stats['skill_list'][player_skill_choice]['skill_is_in_cooldown']:
         (
          #//player_combat_stats,
          #//current_player_status,
          #//current_enemy_stats,
          #//current_enemy_status,
          current_player_attack_bonus,
          current_player_defense_bonus,
          current_enemy_attack_bonus,
          current_enemy_defense_bonus,
          #//damage_per_turn_player,
          #//turn_count_player_debuffs,
          #//debuff_total_duration_player,
          enemy_is_debuffed_damage,
          #//turn_count_enemy_debuffs,
          #//damage_per_turn_enemy,
          player_is_debuffed_damage,
          #//enemy_debuff_ends_at,
          #//player_stat_debuff_power,
          #//player_stat_debuff_data,
          enemy_is_debuffed_stat,
          #//enemy_stat_debuff_power,
          #//enemy_stat_decreased,
          player_is_stat_debuffed,
          #//player_combat_stats['skill_list'][player_skill_choice]
          skip_player_turn,
          player_has_rush,
          current_enemy_dodge_bonus,
          enemy_is_stat_buffed,
          player_is_stat_buffed,
          current_player_crit_bonus,
          current_player_dodge_bonus,
          current_enemy_crit_bonus,
          player_has_rage
         )=acquired_skill_routine(
           player_combat_stats['skill_list'][player_skill_choice],
           player_combat_stats,
           current_enemy_stats,
           current_player_status,
           current_enemy_status,
           current_player_attack_bonus,
           current_player_defense_bonus,
           current_enemy_attack_bonus,
           current_enemy_defense_bonus,
           size_format_combat_screen,
           turn_count,
           damage_per_turn_player,
           turn_count_player_debuffs,
           debuff_total_duration_player,
           enemy_is_debuffed_damage,
           turn_count_enemy_debuffs,
           damage_per_turn_enemy,
           player_is_debuffed_damage,
           enemy_debuff_ends_at,
           player_stat_debuff_power,
           player_stat_debuff_data,
           enemy_is_debuffed_stat,
           enemy_stat_debuff_power,
           enemy_stat_decreased,
           player_is_stat_debuffed,
           turn_skills_enter_cooldown,
           skip_player_turn,
           player_has_rush,
           enemy_buffs_power,
           enemy_buffs_duration,
           enemy_buffs_stat_increased,
           enemy_buff_was_applied_at,
           current_enemy_dodge_bonus,
           enemy_is_stat_buffed,
           player_stat_buff_data,
           player_stat_buff_power,
           player_stat_buff_duration,
           player_stat_buff_was_applied_at,
           player_is_stat_buffed,
           current_player_crit_bonus,
           current_player_dodge_bonus,
           current_enemy_crit_bonus,
           player_has_rage
         )

         break

        else:
         print(f'The {player_combat_stats['skill_list'][player_skill_choice]['name']} is on cooldown!')
         print()
         print('Press Enter to Continue'.center(size_format_combat_screen))
         input()

         #//turn_skills_enter_cooldown[player_combat_stats['skill_list'][player_skill_choice]['name']]=turn_count
         #//player_combat_stats['skill_list'][player_skill_choice]['skill_is_in_cooldown']=True
         
         

        #//else: #? Is this really needed? no it ain't lmao
        #//print(f'The {player_combat_stats['skill_list'][player_skill_choice]['name']} is on cooldown!')
        #//print()
        #//print('Press Enter to Continue'.center(size_format_combat_screen))
      else:
       print('You are silenced and unable to use your skills!')
       input('Press Enter to Continue')
     

   else:
    print('Your turn has been skipped!')
    skip_player_turn=False
    current_player_status.remove('SKIP_TURN')
    break


  if enemy_is_debuffed_damage:

   for debuff in damage_per_turn_player.keys():

    if damage_per_turn_player[debuff]>0:
     print(f'The enemy took {damage_per_turn_player[debuff]} from their {debuff}!')
     current_enemy_stats['hp_current']-=damage_per_turn_player[debuff]

   #! Removing something from a list used in a 'for' causes
   #! It to end prematurely leaving an eternal debuff on enemy
   #! So it iterates every single applied debuff this fight instead
   #! The condition above is to avoid performance issues
   for debuff in damage_per_turn_player.keys():

    if (turn_count-turn_count_player_debuffs[debuff])==debuff_total_duration_player[debuff]: #| Debuff wears off

     print(f'The enemy {debuff} wore off!')

     turn_count_player_debuffs[debuff]=0
     debuff_total_duration_player[debuff]=0
     damage_per_turn_player[debuff]=0
     current_enemy_status.remove(debuff)


   if sum(damage_per_turn_player.values())<=0:   #| No debuffs active
    enemy_is_debuffed_damage=False


  if enemy_is_debuffed_stat:    #| Enemy stat debuff wears off
   for debuff in player_stat_debuff_power.keys():

    if (turn_count-turn_count_player_debuffs[debuff])==debuff_total_duration_player[debuff]:     #| If debuff ends this turn

     if 'ATK' in player_stat_debuff_data[debuff]:
      current_enemy_attack_bonus+=player_stat_debuff_power[debuff]

     if 'DEF' in player_stat_debuff_data[debuff]:
      current_enemy_defense_bonus+=player_stat_debuff_power[debuff]

     if 'DODGE' in player_stat_debuff_data[debuff]:
      current_enemy_dodge_bonus+=player_stat_debuff_power[debuff]

     if 'CRIT' in player_stat_debuff_data[debuff]:
      current_enemy_crit_bonus+=player_stat_debuff_power[debuff]

     turn_count_player_debuffs[debuff]=0
     #//player_stat_debuff_data.pop(debuff)
     debuff_total_duration_player[debuff]=0
     player_stat_debuff_power[debuff]=0
     current_enemy_status.remove(debuff)

     print(f'The enemy {debuff} wears off!')

   if sum(player_stat_debuff_power.values())<=0:  #| No active stat debuffs
    enemy_is_debuffed_stat=False


  if (turn_count-turn_count_player_block)==player_combat_stats['block_duration_modifier'] and player_is_blocking==True:  # Block ends
   turn_count_player_block=0
   current_player_attack_bonus+=attack_decrease_from_block_player
   current_player_defense_bonus-=player_combat_stats['block_power']
   player_is_blocking=False

   print('Your defensive stance bonus wears off!')

  if 'SILENCE' in current_enemy_status:
   if (turn_count-turn_count_player_debuffs['SILENCE'])==debuff_total_duration_player['SILENCE']:

    print('The enemy is no longer silenced!')
    current_enemy_status.remove('SILENCE')
    turn_count_player_debuffs.pop('SILENCE')
    debuff_total_duration_player.pop('SILENCE')


  if player_is_stat_buffed:

   for buff in player_stat_buff_was_applied_at.keys():

    if (turn_count-player_stat_buff_was_applied_at[buff])==player_stat_buff_duration[buff]:

     if 'CRIT' in player_stat_buff_data[buff]:
      current_player_crit_bonus-=player_stat_buff_power[buff]

     if 'DODGE' in player_stat_buff_data[buff]:
      current_player_dodge_bonus-=player_stat_buff_power[buff]

     player_stat_buff_power[buff]=0
     player_stat_buff_was_applied_at[buff]=0
     player_stat_buff_data.pop(buff)
     player_stat_buff_duration[buff]=0

     print(f'Your {buff} buff runs out!')

   if sum(player_stat_buff_power.values())<=0:
    player_is_stat_buffed=False


  if current_enemy_stats['hp_current']<=0:     # Checks if the enemy is dead

   display('VICTORY',size_format_combat_screen)
   print(f'You gained {current_enemy_stats['gold_drop']} gold')

   player_combat_stats['money']+=current_enemy_stats['gold_drop']

   print()
   input(f'{'Press Enter to Continue':^{size_format_combat_screen}}\n')
   break

  print()
  input(f'{'Press Enter to Continue\n':^{size_format_combat_screen}}')

  #> Player Turn Region End


  #> Enemy Turn Region

  os.system('cls')
  player_combat_stats['player_has_taken_damage_this_turn']=False

  combat_screen(
   player_combat_stats,       
   current_enemy_stats,
   size_format_combat_screen,
   current_player_status,
   current_enemy_status,
   current_player_attack_bonus,
   current_player_defense_bonus,
   current_player_dodge_bonus,
   current_enemy_attack_bonus,
   current_enemy_defense_bonus,
   turn_count,
   player_has_rage,
   player_has_rush,
   current_enemy_dodge_bonus,
   current_player_crit_bonus,
   enemy_has_rush,
   current_enemy_crit_bonus
   )

  if mini_boss==False:
   enemy_action,enemy_buff_debuff_choice=level_1_enemy_ai(
    turn_count,
    #current_player_status,
    current_player_attack_bonus,
    player_is_debuffed_damage,
    player_is_stat_debuffed,
    enemy_is_blocking,
    enemy_is_stat_buffed,
    current_enemy_stats,
    current_enemy_defense_bonus,
    damage_dealt
   )

  elif mini_boss==True:
   (
    enemy_action,
    enemy_buff_debuff_choice,
    #//ai_control_value
   )=level_1_miniboss_ai(
                         turn_count,
                         #//current_player_status,
                         player_is_debuffed_damage,
                         player_is_stat_debuffed,
                         current_enemy_stats,
                         enemy_action,
                         #//ai_test #*Debug
                        )

  sleep(sleep_timer)

  # It dawns on me this might grow much beyond what I believe
  # I will stick with it for now, but might need refactoring in the future - 23/07/2024

  if enemy_action=='DEF':

   #if not enemy_is_blocking:      

   current_enemy_defense_bonus+=current_enemy_stats['block_power']
   attack_decrease_from_block_enemy=int(current_enemy_stats['attack']*20/100)
   current_enemy_attack_bonus-=attack_decrease_from_block_enemy
   enemy_is_blocking=True
   turn_count_enemy_block=turn_count

   print(f'The enemy defense increases for {current_enemy_stats['block_duration']} turns!')

   #elif enemy_is_blocking==True:
    #turn_count_enemy_block+=((current_enemy_stats['block_duration']//2))
    #print('The enemy extends their block further!')


  #*DONE Change this to use the actual real None value here and on enemy AI
  elif enemy_action==None:    # Freebie player action
   pass

  #*DONE Change this to ATK along with all the other AI returns
  elif enemy_action=='ATK':     # Standard attack action

   if (player_combat_stats['dodge_chance']+current_player_dodge_bonus+player_combat_stats['luck'])>=dodge_check or player_has_rush:
    print('You dodged the enemy strike!')

    player_has_rush=False
   
   else:
    enemy_damage=current_enemy_stats['attack']+current_enemy_attack_bonus+attack_decrease_from_block_enemy-(player_combat_stats['defense']+current_player_defense_bonus)

    try:
     if 'STEAL_GOLD' in current_enemy_stats['attack_effects'].keys():
      gold_stolen=randint((current_enemy_stats['attack_effects']['STEAL_GOLD']//2),current_enemy_stats['attack_effects']['STEAL_GOLD'])

      if player_combat_stats['money']<gold_stolen:
       gold_stolen=player_combat_stats['money']

      player_combat_stats['money']-=gold_stolen
      current_enemy_stats['gold_drop']+=gold_stolen

      print(f'The enemy has stolen {gold_stolen} gold from you!')
     
     else:
      for effect in current_enemy_stats['attack_effects'].keys():
       effect_apply_check=randint(1,100)

       if effect in stat_debuffs.keys():
        if (20-player_combat_stats['luck'])>=effect_apply_check:
         print(f'The enemy attack has inflicted {effect}!')

         if effect not in current_player_status:
          debuff_power=current_enemy_stats['attack_effects'][effect]
          enemy_stat_decreased[effect]=[]

          if 'ATK' in stat_debuffs[effect]:
           try:
            if player_combat_stats['cant_lower_player_attack']:
             print('You are immune to the attack drop!')
           except KeyError:
            current_player_attack_bonus-=debuff_power

          current_player_status.append(effect)
          player_is_stat_debuffed=True
          enemy_stat_debuff_power[effect]=debuff_power
          turn_count_enemy_debuffs[effect]=turn_count
          enemy_debuff_ends_at[effect]=2
          enemy_stat_decreased[effect].append('ATK')


       elif effect in damage_debuffs:
        if (20-player_combat_stats['luck'])>=effect_apply_check:
         print(f'The enemy attack has inflicted {effect}!')

         if effect not in player_combat_stats['player_immunity']:
          debuff_power=current_enemy_stats['attack_effects'][effect]

          if effect not in current_player_status:

           turn_count_enemy_debuffs[effect]=turn_count
           enemy_debuff_ends_at[effect]=2
           current_player_status.append(effect)
           damage_per_turn_enemy[effect]=debuff_power
           player_is_debuffed_damage=True
          
          elif effect in current_player_status:
           damage_per_turn_enemy[effect]+=(debuff_power//2)+(debuff_power%2>0)

         elif effect in player_combat_stats['debuff_immunity']:
          print(f'You are immune to the {effect}!')

    except KeyError:
     pass

    try:
     if player_combat_stats['player_has_glass_dagger']:
      enemy_damage*=2
    except KeyError:
     pass

    if (current_enemy_stats['critical_chance']+current_enemy_crit_bonus-player_combat_stats['luck'])>=crit_check and enemy_damage>0:
     enemy_damage*=2
     print('It landed a critical hit!')

  #! Obsolete, do not use
  #//elif enemy_action=='OVERTIME_DAMAGE':       # Damage debuff action

   #//if 'SILENCE' not in current_enemy_status:
    #//if enemy_buff_debuff_choice not in player_combat_stats['player_immunity']:

     #//if enemy_buff_debuff_choice not in current_player_status:

      #//damage_per_turn_enemy[enemy_buff_debuff_choice]=current_enemy_stats['damage_overtime'][enemy_buff_debuff_choice]
      #//current_player_status.append(enemy_buff_debuff_choice)
      #//turn_count_enemy_debuffs[enemy_buff_debuff_choice]=turn_count
      #//enemy_debuff_ends_at[enemy_buff_debuff_choice]=current_enemy_stats['debuff_duration'][enemy_buff_debuff_choice]
      #//player_is_debuffed_damage=True

      #//print(f'You are now suffering from {enemy_buff_debuff_choice}!')

     #//elif enemy_buff_debuff_choice in current_player_status:         
      #//damage_per_turn_enemy[enemy_buff_debuff_choice]+=(current_enemy_stats['damage_overtime'][enemy_buff_debuff_choice]//2)  

      #//print(f'Your {enemy_buff_debuff_choice} hurts more!')

    #//else:
     #//print('The player is immune to the debuff!')

   #//else:
    #//print('The enemy is silenced and unable to use their own abilities')

  #*//DONE Have to refactor this too. Shit
  #*//DONE use the new 'enemy_stat_decreased' dict
  #! Obsolete, do not use
  #//elif enemy_action=='LOWER_STAT':

   #//if 'SILENCE' not in current_enemy_status:

    #//if enemy_buff_debuff_choice not in player_combat_stats['player_immunity']:
    #//if enemy_buff_debuff_choice not in current_player_status:

      #*//DONE Change this so it only applies for each individual debuff
      #*//DONE stat change rather than this atrocity
     #//try:
      #//if player_combat_stats['cant_lower_player_attack']:
       #//print('You are immune to the enemy stat debuff!')

       #//except KeyError: #> Expected'''
     #//enemy_stat_decreased[enemy_buff_debuff_choice]=current_enemy_stats['stat_decreased'][enemy_buff_debuff_choice]
     #//enemy_stat_debuff_power[enemy_buff_debuff_choice]=current_enemy_stats['debuff_strength'][enemy_buff_debuff_choice]

     #//if 'ATK' in enemy_stat_decreased[enemy_buff_debuff_choice]:

      #//try:
       #//if player_combat_stats['cant_lower_player_attack']:
        #//print('You are immune to the attack drop!')
      #//except KeyError:
       #//current_player_attack_bonus-=enemy_stat_debuff_power[enemy_buff_debuff_choice]

     #//if 'DEF' in enemy_stat_decreased[enemy_buff_debuff_choice]:   
      #//current_player_defense_bonus-=enemy_stat_debuff_power[enemy_buff_debuff_choice]

     #//if 'DODGE' in enemy_stat_decreased[enemy_buff_debuff_choice]:

      #//try:
       #//if player_combat_stats['cant_lower_player_dodge']:
        #//print('You are immune to the dodge drop!')
        #//enemy_stat_decreased.pop(enemy_buff_debuff_choice)
        #//enemy_stat_debuff_power.pop(enemy_buff_debuff_choice)

      #//except KeyError:
       #//current_player_dodge_bonus-=enemy_stat_debuff_power[enemy_buff_debuff_choice]

       #//current_player_status.append(enemy_buff_debuff_choice)
       #//enemy_debuff_ends_at[enemy_buff_debuff_choice]=current_enemy_stats['debuff_duration'][enemy_buff_debuff_choice]
       #//player_is_stat_debuffed=True
       #//turn_count_enemy_debuffs[enemy_buff_debuff_choice]=turn_count
       #//enemy_stat_debuff_power[enemy_buff_debuff_choice]=current_enemy_stats['debuff_strength'][enemy_buff_debuff_choice]
       #//enemy_stat_decreased[enemy_buff_debuff_choice]=current_enemy_stats['stat_decreased'][enemy_buff_debuff_choice]

       #//print(f'You are now afflicted with {enemy_buff_debuff_choice}!')

    #//elif enemy_buff_debuff_choice in current_player_status:  
     #//turn_count_enemy_debuffs[enemy_buff_debuff_choice]+=current_enemy_stats['debuff_duration'][enemy_buff_debuff_choice]//2

     #//print(f'The {enemy_buff_debuff_choice} will now last longer')

    #//else:
     #//print('The player is immune to the debuff!')

   #//else:
    #//print('The enemy is silenced and unable to use their own abilities')

  #! Obsolete, do not use
  #//elif enemy_action=='STAT_BOOST': #// Buffs that last the whole fight
   #//if 'SILENCE' not in current_enemy_status:

    #//if 'ATK' in current_enemy_stats['buff_stat_increase'][enemy_buff_debuff_choice]:
     #//current_enemy_attack_bonus+=current_enemy_stats['buff_power'][enemy_buff_debuff_choice]
     #//print("The enemy has boosted it's own attack!")

    #//if 'DEF' in current_enemy_stats['buff_stat_increase'][enemy_buff_debuff_choice]:
     #//current_enemy_defense_bonus+=current_enemy_stats['buff_power'][enemy_buff_debuff_choice]
     #//print("The enemy has boosted it's own defense")

    #//if 'DODGE' in current_enemy_stats['buff_stat_increase'][enemy_buff_debuff_choice]:

     #//current_enemy_dodge_bonus+=current_enemy_stats['buff_power'][enemy_buff_debuff_choice]
     #//enemy_buffs_power[enemy_buff_debuff_choice]=current_enemy_stats['buff_power'][enemy_buff_debuff_choice]
     #//enemy_buffs_duration[enemy_buff_debuff_choice]=current_enemy_stats['buff_duration'][enemy_buff_debuff_choice]
     #//enemy_buffs_stat_increased[enemy_buff_debuff_choice]=current_enemy_stats['buff_stat_increase'][enemy_buff_debuff_choice]
     #//enemy_buff_was_applied_at[enemy_buff_debuff_choice]=turn_count
     #//enemy_is_stat_buffed=True

     #//print("The enemy increased it's dodge chance!")

    #//if 'RUSH' in current_enemy_stats['buff_stat_increase'][enemy_buff_debuff_choice]:
     #//enemy_has_rush=True
     #//print('The enemy will dodge the next attack!')

   #//else:
    #//print('The enemy is silenced and unable to use their own abilities')


  elif enemy_action=='SPECIAL_ATTACK':

   if 'SILENCE' not in current_enemy_status:
    (
     current_enemy_attack_bonus,
     current_enemy_defense_bonus,
     current_enemy_dodge_bonus,
     current_enemy_crit_bonus,
     enemy_has_rush,
     enemy_is_stat_buffed,
     current_player_attack_bonus,
     current_player_defense_bonus,
     current_player_dodge_bonus,
     player_is_stat_debuffed,
     player_is_debuffed_damage,
     skip_player_turn
    )=enemy_skills(
     enemy_buff_debuff_choice,
     player_combat_stats,
     current_enemy_stats,
     current_enemy_attack_bonus,
     current_enemy_defense_bonus,
     current_enemy_dodge_bonus,
     current_enemy_crit_bonus,
     enemy_has_rush,
     enemy_is_stat_buffed,
     current_player_attack_bonus,
     current_player_defense_bonus,
     current_player_dodge_bonus,
     skip_player_turn,
     enemy_debuff_ends_at,
     enemy_stat_decreased,
     enemy_stat_debuff_power,
     turn_count_enemy_debuffs,
     current_player_status,
     player_is_stat_debuffed,
     enemy_buffs_power,
     enemy_buff_was_applied_at,
     enemy_buffs_duration,
     enemy_buffs_stat_increased,
     damage_per_turn_enemy,
     player_is_debuffed_damage,
     turn_count
    )

   elif 'SILENCE' in current_enemy_status:
    print('The enemy has been silenced and cannot use special abilities!')


  elif enemy_action=='RUN':
   print(current_enemy_stats['runaway_message'])
   print('\nPress Enter to Continue')
   input()
   break


  if enemy_damage>0:      # Performs this damage step only if the enemy has attacked
   print(f'The {current_enemy_stats['enemy_name']} dealt {enemy_damage} damage')
   player_combat_stats['hp_current']-=enemy_damage
   player_combat_stats['player_has_taken_damage_this_turn']=True
   sleep(sleep_timer)

  elif enemy_damage<0:
   print(f"The {current_enemy_stats['enemy_name']} attack couldn't hurt you")


  if player_is_debuffed_damage:   

   for debuff in damage_per_turn_enemy.keys():

    if damage_per_turn_enemy[debuff]>0:
     player_combat_stats['hp_current']-=damage_per_turn_enemy[debuff]
     print(f'You take {damage_per_turn_enemy[debuff]} damage from the {debuff}!')

   sleep(sleep_timer)

   for debuff in damage_per_turn_enemy.keys():  #| Debuff runs out

    # This is needed mainly because it iterates for every debuff the enemy has available
    # If the enemy has not used some of them, those will generate an error on the turn count check - 21/08/2024
    # With the new method I'm confident this wont be needed anymore, just gotta test a little - 31/08/2024
    #//try:
    if (turn_count-turn_count_enemy_debuffs[debuff])==enemy_debuff_ends_at[debuff]:

     damage_per_turn_enemy[debuff]=0
     turn_count_enemy_debuffs[debuff]=0
     enemy_debuff_ends_at[debuff]=0
     current_player_status.remove(debuff)

     print(f'The {debuff} wears off')

    #//except KeyError:
     #//pass

    #//finally:
     #//continue

   if sum(damage_per_turn_enemy.values())<=0:
    player_is_debuffed_damage=False

   sleep(sleep_timer)

  try:
   if (turn_count-turn_count_enemy_block)==current_enemy_stats['block_duration'] and enemy_is_blocking==True:  # Block wears off

    turn_count_enemy_block=0
    current_enemy_attack_bonus+=attack_decrease_from_block_enemy
    current_enemy_defense_bonus-=current_enemy_stats['block_power']
    enemy_is_blocking=False

    print('The enemy blocking bonus fades!')
    sleep(sleep_timer)

  except KeyError:
   pass


  #*DONE Nuclear refactoring incoming. Use new 'enemy_stat_decreased' dict
  #*DONE Must test tomorrow
  if player_is_stat_debuffed:  # Stat debuff runs out

   #total_check=0 # Check for any active debuff
   for debuff in enemy_stat_debuff_power.keys(): # Iterates each debuff

    # If a certain debuff hasn't been applied, but player was debuffed before
    # It can raise a KeyError due to how it iterates
     if (turn_count-turn_count_enemy_debuffs[debuff])==enemy_debuff_ends_at[debuff]:  # Debuff runs out

      print(f'The {debuff} fades away!')

      turn_count_enemy_debuffs[debuff]=0
      current_player_status.remove(debuff)
      #//total_check+=turn_count_enemy_debuffs[debuff]

      if 'ATK' in enemy_stat_decreased[debuff]:

       try:
        if player_combat_stats['cant_lower_player_attack']:
         pass
       except KeyError:
        current_player_attack_bonus+=enemy_stat_debuff_power[debuff]

      if 'DEF' in enemy_stat_decreased[debuff]:
       current_player_defense_bonus+=enemy_stat_debuff_power[debuff]

      if 'DODGE' in enemy_stat_decreased[debuff]:
       try:
        if player_combat_stats['cant_lower_player_dodge']:
         pass
       except KeyError:
        current_player_dodge_bonus+=enemy_stat_debuff_power[debuff]

      enemy_stat_debuff_power[debuff]=0
      enemy_debuff_ends_at[debuff]=0

   if sum(enemy_stat_debuff_power.values())==0:  # If no stat debuffs are active
    player_is_stat_debuffed=False

   sleep(sleep_timer)


  if enemy_is_stat_buffed: #> Only temporary buffs will be Dodge and Crit for now - 25/09/2024

   for buff in enemy_buffs_power.keys():

    if (turn_count-enemy_buff_was_applied_at[buff])==enemy_buffs_duration[buff]:

     if 'DODGE' in enemy_buffs_stat_increased[buff]:
      current_enemy_dodge_bonus-=enemy_buffs_power[buff]
      print('The enemy dodge bonus waned!')

     if 'CRIT' in enemy_buffs_stat_increased[buff]:
      current_enemy_crit_bonus-=enemy_buffs_power[buff]
      print('The enemy critical bonus waned!')

     #//current_enemy_status.remove(buff)
     enemy_buffs_power[buff]=0
     enemy_buffs_duration[buff]=0
     enemy_buff_was_applied_at.pop(buff) #! Popped so it can check for reapplying debuffs and applying the same debuff again properly

    if sum(enemy_buffs_power.values())==0:
     enemy_is_stat_buffed=False


  #> Enemy Turn Region End

  if 'SILENCE' in current_player_status:
   if (turn_count-turn_count_enemy_debuffs['SILENCE'])==enemy_debuff_ends_at['SILENCE']:

    print('You are no longer silenced!')
    current_player_status.remove('SILENCE')
    turn_count_enemy_debuffs.pop('SILENCE')
    enemy_debuff_ends_at.pop('SILENCE')


  try:
   if player_combat_stats['has_ebony_scarf'] and turn_count%4==0:
    current_player_dodge_bonus-=30

  except KeyError: #>Expected when player does not have scarf
   pass

  ai_test+=1  #* Debug

  turn_count+=1
  #//ai_control_value+=1

  try:
   if player_combat_stats['player_has_stone_armor'] and turn_count%2==0:
    skip_player_turn=True
  except KeyError:
   pass

  #?//for skill in turn_skills_enter_cooldown.keys():
   #?//if turn_skills_enter_cooldown[skill]>0:
    #?//turn_skills_enter_cooldown[skill]-=1
  


  if player_combat_stats['hp_current']<=0:  # Player is un-alive
   player_combat_stats['player_is_alive']=False

  if player_combat_stats['player_is_alive'] is False:
   del current_enemy_stats
   return 

  print_line(size_format_combat_screen)
  print()
  input(f'{'Press Enter to Continue':^{size_format_combat_screen}}\n')


 # This might not be needed anymore, won't remove it quite yet though - 16/08/2024
 #//player_combat_stats['attack_current']=original_player_attack
 #//player_combat_stats['defense']=player_original_defense 

 return None
