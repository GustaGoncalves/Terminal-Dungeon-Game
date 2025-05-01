from random import randint

def level_1_miniboss_list():
 """
 Contains the early level mini-bosses
 mini_boss_choice: integer number that decides which enemy will be loaded
 """


 base_hp=randint(52,71)

 #TODO Add to the wizard the ability to invoke a shield that boosts his defense temporarily
 #TODO Allow wizard to poison player too
 #*DONE Add weakness to earth element
 charred_wizard_data={
  'enemy_name':'CHARRED WIZARD',
  'hp_max':base_hp,
  'hp_current':base_hp,
  'defense':-1,
  'dodge_chance':0, # 0 out of 100, as in 0% chance
  'attack':2,
  #//'damage_overtime':{ # Applied overtime
   #//'BURN':6,
   #//'POISON':7 #//debug
  #//},
  #//'debuff_duration':{ # Debuff duration modifiers
   #//'BURN':4,
   #//'POISON':4 #//debug
  #//},
  'steal_chance':50,
  'steal_class':'GOLD',
  'item_stolen':randint(20,30),
  'enemy_has_been_stolen':False,
  #//'debuff_type':[
   #//'BURN',
   #//'POISON' #*debug
  #//],
  'debuff_immunity':[
   'BURN'
  ],
  'elemental_resistance':[
   'FIRE' 
  ],
  'elemental_weakness':[
   'EARTH'
  ],
  'special_attacks':{
   'scorch':{
    'effects':[
     'DAMAGE',
     'DEBUFF_PLAYER_DAMAGE'
    ],
    'accuracy':100,
    'damage':11,
    'damage_debuff_apply_chance':80,
    'debuff_damage':5,
    'debuff_type_damage':'BURN',
    'damage_debuff_duration':3,
    'use_message':'The wizard chant summoned flames that singe your skin!'
   },

   'smog':{
    'effects':[
     'DEBUFF_PLAYER_DAMAGE'
    ],
    'damage_debuff_apply_chance':100,
    'debuff_damage':6,
    'debuff_type_damage':'POISON',
    'damage_debuff_duration':4,
    'use_message':'The wizard conjures a toxic cloud on you!'
   },

   'magic_shield':{
    'effects':[
     'BUFF_ENEMY_STAT'
    ],
    'buff_apply_chance':100,
    'buff_power':4,
    'stat_increased':[
     'DEF'
    ],
    'use_message':'The wizard puts up a magical barrier!'
   }
  },
  #//'block_duration':0, #? Are these needed? #No they arent!
  #//'block_power':0,
  'critical_chance':0, #> Out of 100
  'ai_load':0,
  'gold_drop':randint(30,55),
  'ai_control':0,
  'encounter_message':[
   'On the corridor, you find a corpse',
   'It has been SCORCHED ENTIRELY',
   "But there's a chance he has something on him still..."
  ]
 }

 base_hp=randint(91,113)

 #*DONE Give Punisher ability to debuff player
 the_punisher_data={
  'enemy_name':'THE PUNISHER',
  'hp_max':base_hp,
  'hp_current':base_hp,
  'defense':0,
  'dodge_chance':0,
  'attack':3,
  #//'dodge_chance':0,
  #//'buff_power':{
   #//'RAGE':2
  #//},
  #//'buff_type':[
   #//'RAGE'
  #//],
  #//'buff_stat_increase':{
   #//'RAGE':[
    #//'ATK'
   #//]
  #//},
  'critical_chance':0,
  'elemental_resistance':[
   None
  ],
  'debuff_immunity':[
   None
  ],
  'steal_class':'ITEM',
  #//'item_to_pull':6,
  'item_stolen':{
   'name':'Bottled Rage',
   'description':'Pure concentrated anger contained in a bottle.\nMerely looking at it makes you angry.',
   'effect_types':[
    'BUFF'
   ],
   'buff_types':[
    'RAGE'
   ],
   'price':11,

   'usage_message':'Right after openning the bottle\nYou smashed it into the ground furiously\nYou feel angry like never before!'
  },
  'steal_chance':70,
  'enemy_has_been_stolen':False,

  'special_attacks':{
   'rage':{
    'effects':[
     'BUFF_ENEMY_STAT'
    ],
    'buff_apply_chance':100,
    'buff_power':3,
    'stat_increased':[
     'ATK'
    ],
    'use_message':'The Punisher screams loudly!\nThat seems to have boosted his morale!'
   },

   'boreal_strike':{
    'effects':[
     'DAMAGE',
     'DEBUFF_STAT_PLAYER'
    ],
    'damage':17,
    'accuracy':100,
    'debuff_apply_chance':100,
    'stat_debuff_power':4,
    'stat_decreased':[
     'DEF'
    ],
    'debuff_type':'FROSTBITE',
    'stat_debuff_duration':4,
    'use_message':'The Punisher strikes with the power of the frigid winds!'
   }
  },
  'ai_load':1,
  'ai_control':0,
  'gold_drop':randint(45,55),
  'encounter_message':[
   'On your way through you find someones body',
   'It has been THOROUGHLY BEATEN with a blunt weapon',
   'It may be wise to leave',
   "But maybe there's something left on him..."
  ]
 }

 base_hp=randint(68,82)

 storm_talon_data={
  'enemy_name':'STORM TALON',
  'hp_max':base_hp,
  'hp_current':base_hp,
  'defense':1,
  'dodge_chance':10,
  'attack':11,
  'critical_chance':20,
  'elemental_resistance':[
   'SHOCK'
  ],
  'debuff_immunity':[
   None
  ],
  'elemental_weakness':[
   'EARTH'
  ],
  'steal_chance':135,
  'steal_class':'RELIC',
  'item_stolen':{
   'name':'Gnashing Talon',
   'description':"A single sharp claw taken from a Storm Talon\nYou can feel a small electric current\nrun through your body when holding",
   'critical_chance':15,
   'attack_current':6,
   'price':60
  },
  'enemy_has_been_stolen':False,
  'attack_effects':{
   'WOUNDED':3
  },
  'special_attacks':{

   'shock_slash':{
    'effects':[
     'DAMAGE',
     'DEBUFF_UNIQUE_PLAYER' #*DONE Develop the unique buff system
    ],
    'debuff_apply_chance_unique':50,
    'unique_debuff':'SKIP_TURN',
    'accuracy':100,
    'damage':23,
    'use_message':"The Storm Talon strikes with a charged claw!"
   },

   'raging_sweep':{
    'effects':[
     'DAMAGE'
    ],
    'accuracy':55,
    'damage':37,
    'use_message':"The Storm Talon fly's down with tremendous speed to strike!"
   }
  },
  'ai_load':2,
  'ai_control':0,
  'gold_drop':randint(54,71),
  'encounter_message':[
   "On your way, you find a corpse COMPLETELY MAULED",
   "His bag is still mostly intact",
   "Maybe you can find something useful in it..."
  ]
 }

 return [
  charred_wizard_data,
  the_punisher_data,
  storm_talon_data
 ]


def level_1_miniboss_ai(turn_count: int,
                           #//current_player_status: dict,
                           player_is_debuffed_damage: bool,
                           player_is_stat_debuffed: bool,
                           enemy_stats: dict,
                           last_enemy_action: str,
                           test_var=None
                           ):
 """
 Executes the AI routine of each miniboss
 It will know which to execute based on their internal indexing
 #//mini_boss_choice: Which mini_boss has been loaded
 turn_count: Current turn count/number

 player_is_debuffed_damage: Player has active damaging debuffs flag

 player_is_stat_debuffed: Player has active stat debuffs flag
 #//current_player_status: Current player status in the battle
 enemy_stats: Dict containing all the current enemy stats

 ai_control: Int value used for turn related AI decision loops

 test_var: Debug only

 player_is_debuffed: Bool value to check if player is currently debuffed (stat decreases not included)
 """

 # I ought to figure something better than this
 # So far not many ideas though - 16/08/2024

 match enemy_stats['ai_load']:

  case 0: #| Charred Wizard AI

   #//if test_var==0 or test_var==2:
    #//random_action=19

   #//elif test_var==1:
    #//print("He BURN's you")

    #//return 'OVERTIME_DAMAGE',enemy_stats['debuff_type'][0]
   
   #//elif turn_count==8:

    #//print('Burn is real lmao')

    #//return 'OVERTIME_DAMAGE',enemy_stats['debuff_type'][0]

   #//elif test_var>2 and test_var!=8:

    #//return None,None'''

   #//Applies burn to player if they haven't been debuffed in 3 turns
   #//Must be independent check or else conflict ensues
   if turn_count==1:
    print('The wizard is preparing a different spell!')
    return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['magic_shield']

   if enemy_stats['ai_control']==0:

    if not player_is_debuffed_damage:
     print('The wizard chants something!')
     enemy_stats['ai_control']+=1
     #//print('Flames suddenly appear and singe your skin!')

     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['scorch']
    
    else:
     print('The wizard strikes you with an old cane!')
     return 'ATK',None

   elif enemy_stats['ai_control']==1:
    
    if not player_is_debuffed_damage:
     print('The wizard is chanting something!')
     enemy_stats['ai_control']+=1

     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['smog']

    else:
     print('The wizard strikes you with an old cane!')

     return 'ATK',None

   else:
    
    if not player_is_debuffed_damage:
     enemy_stats['ai_control']=0



    random_action=randint(1,100)

   #//Action debuff player with poison
    if random_action<=80:
     print('The wizard strikes you with an old cane')
     #//print('Flames suddenly appear and singe your skin!')

     return 'ATK',None
    
    elif 80<random_action<=90:
     print('The wizard chants something')

     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['scorch']

    elif 90<random_action<=100:
     print('The wizard is preparing something!')

     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['smog']

   #//Action standard attack
   #//if random_action<=100 and random_action>20:
    #//print('The wizard swings at you with and old cane!')

    #//return 'ATK',None


  case 1: #| Punisher AI

   if turn_count%3==0:

    if enemy_stats['ai_control']>0 and not player_is_stat_debuffed:
     print('The Punisher is preparing a special strike!')
     enemy_stats['ai_control']=0

     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['boreal_strike']

    else:
     print('The Punisher swings his massive spiked club at you!')
     enemy_stats['ai_control']+=1
     return(
      'ATK',
      None
     )
   
   else:

    if last_enemy_action=='ATK':
     #//print('The Punisher shouts agressively!')
     #//print('He seems somehow stronger from it')

     return(
      'SPECIAL_ATTACK',
      enemy_stats['special_attacks']['rage']
     )
    
    elif turn_count==1:
     #//print('The Punisher shouts agressively!')
     #//print('He seems somehow stronger from it')

     return(
      'SPECIAL_ATTACK',
      enemy_stats['special_attacks']['rage']
     )

    else:
     print('The Punisher is preparing his next attack!')

     return(
      None,
      None
     )
    
    '''elif turn_count%2==1:
     print('The Punisher shouts agressively!')
     print('He seems somehow stronger from it')

     return(
      'STAT_BOOST',
      enemy_stats['buff_type'][0]
     )'''

   #*DONE Improve this by using the modulus operator properly for turn checks instead of a unique value
   '''if ai_control==2:
    print('The Punisher is readying a strike!')

    return (
     None,
     None,
     ai_control
    )

   elif ai_control==3:
    print('The Punisher swings his massive spiked club at you!')
    ai_control=0

    return (
     'ATTACK',
     None,
     ai_control
    )

   else:
    print('The Punisher shouts agressively!')
    print('He seems stronger from it somehow')

    return (
     'STAT_BOOST',
     enemy_stats['buff_type'][0],
     ai_control
    )'''


  case 2:
   if enemy_stats['ai_control']==0:
    print("The Talon uses it's sharp beak to strike!")
    enemy_stats['ai_control']+=1
    return 'ATK',None
   
   elif enemy_stats['ai_control']==1:

    if last_enemy_action==None:
     enemy_stats['ai_control']+=1
     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['shock_slash']
    
    print('The Talon seems to be gathering an electric charge!')
    return None,None
   
   elif enemy_stats['ai_control']==2:

    if last_enemy_action==None:
     print('The Talon takes off!')
     enemy_stats['ai_control']+=1
     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['raging_sweep']
    
    print('The Talon seems to be preparing to lift off!')
    return None,None
   
   elif enemy_stats['ai_control']==3:
    print("The Talon seems to be recovering it's strength")
    enemy_stats['ai_control']=0
    return None,None
