from random import randint,choice

#*DONE Separate the AI's of enemies in their own function
# Up for refactoring, turn all of it in a hashtable
# Current solution sucks dick - 05/08/2024
# Done in like, 5 minutes lmao - 05/08/2024
def level_1_enemy_list():
 """
 All the early game and easy enemy data is stored here
 random_enemy_choice: An integer number that decides which enemy will be loaded
 """
 
 # Due to how randint works it is necessary to store it's hp outside the dict - 05/08/2024

 base_hp_general=randint(20,25)

 base_hp_general=1000 #* Debug


 zombie_enemy_data={
  'enemy_name':'ZOMBIE',
  'hp_max':base_hp_general,
  'hp_current':base_hp_general,
  'defense':10,
  'block_power':2,
  'block_duration':2,
  'dodge_chance':0,
  'attack':4,
  'steal_chance':20,
  'steal_class':'GOLD',
  'item_stolen':randint(1,5),
  'enemy_has_been_stolen':False,
  'critical_chance':5,
  'debuff_type':[
   ''
  ],
  'debuff_immunity':[
   None
  ],
  'elemental_resistance':[
   #'FIRE' #* Debug
  ],
  'debuff_duration': [
   None
  ],
  'debuff_strenght':[
   None
  ],

  'ai_load':0,

  'gold_drop':randint(5,10)
 }
 

 # Re-use hp variable to make setting the hp of enemies easier
 # Unlike other things :v - 05/08/2024         
 # Looking at the stuff I am doing now makes this comment funny - Forgot when I made this one
 # The interesting thing is that I managed to improve a lot of the code - 14/10/2024
 base_hp_general=randint(15,20)
 base_hp_general=1000 #*debug


 #|MEMO This enemy should be capable of lowering player attack a bit to compensate for the lack of defensive power - 05/08/2024

 slimy_boi_enemy_data={
  'enemy_name':'SLIME',
  'hp_max':base_hp_general,
  'hp_current':base_hp_general,
  'defense':-1,
  'dodge_chance':5,
  'attack':6,
  'block_duration':0,
  'block_power':0,
  'steal_chance':0,
  'steal_class':None,
  'item_stolen':None,
  'enemy_has_been_stolen':True,
  'critical_chance':0,
  #//'debuff_type':[
   #//'WEAK'

   #//,'FRAIL'   # Debug
  #//],

  #//'stat_decreased':{
   #//'WEAK':[
    #//'ATK',
    #//'DEF'
    #//,'DEF'   # Debug
   #//]

   #//,'FRAIL':[   # Debug
    #//'DEF'
   #//]
  #//},

  'debuff_immunity':[
   'WEAK',
   #//'BLEED'
  ],
  'elemental_resistance':[
   None
  ],
  #//'debuff_duration':{
   #//'WEAK':2

   #//,'FRAIL':3   # Debug
  #//},
  #//'debuff_strength':{
   #//'WEAK':1

   #//,'FRAIL':1   # Debug
  #//},

  'special_attacks':{
   'goo_spray':{
    'use_message':'The slime throws a bunch of goo on you!',
    'effects':[
     'DEBUFF_STAT_PLAYER'
    ],
    'debuff_apply_chance':100,
    'stat_debuff_power':1,
    'stat_decreased':[
     'ATK',
     'DEF'
    ],
    'debuff_type':'WEAK',
    'stat_debuff_duration':2
   }
  },

  'ai_load':1,

  'gold_drop':randint(2,16)
 }

 base_hp_general=randint(18,22)
 #//base_hp_general=200 #*debug

 mario_piranha_plant_data={
  'enemy_name':'TIGER LILY',
  'hp_max':base_hp_general,
  'hp_current':base_hp_general,
  'defense':2,
  'dodge_chance':-10,
  'attack':7,
  'steal_chance':50,
  'steal_class':'ITEM',
  'item_stolen':{
   'name':'Tiger Lily Petal',
   'description':'A petal freshly plucked from a Tiger Lily',
   'effect_types':[
    'HEAL'
   ],
   'heal_power':10,
   'price':10,
   'usage_message':'You ate the petal\nIt has a surprisingly sweet taste'
  },
  'enemy_has_been_stolen':False,
  'critical_chance':5,
  #//'debuff_type':[
   #//'POISON',
   #//'SLOW'
  #//],
  #//'stat_decreased':{
   #//'SLOW':[
    #//'DODGE'
   #//]
  #//},
  'debuff_immunity':[
   'POISON'
  ],
  'elemental_resistance':[
   None
  ],
  'elemental_weakness':[
   'FIRE'
  ],
  #//'debuff_duration':{
   #//'POISON':2,
   #//'SLOW':2
  #//},
  #//'debuff_strength':{
   #//'SLOW':10
  #//},
  #//'damage_overtime':{
   #//'POISON':4
  #//},
  'special_attacks':{
   'entangle':{
    'effects':'DEBUFF_STAT_PLAYER',
    'debuff_apply_chance':100,
    'stat_debuff_power':10,
    'stat_decreased':[
     'DODGE'
    ],
    'debuff_type':'SLOW',
    'stat_debuff_duration':2,
    'use_message':"The Tiger Lily uses it's vines to constrict you"
   },

   'poison_embrace':{
    'effects':[
     'DAMAGE',
     'DEBUFF_PLAYER_DAMAGE'
    ],
    'accuracy':100,
    'damage':6,
    'damage_debuff_apply_chance':100,
    'debuff_damage':4,
    'damage_debuff_duration':2,
    'debuff_type_damage':'POISON',
    'use_message':"The Tiger Lily constricts you with poisonous vines!"
   }

  },
  'ai_load':2,
  'gold_drop':randint(10,20)
 }

 base_hp_general=randint(39,45)

 base_hp_general=100 #*debug

 thief_data={
  'enemy_name':'GRAVE ROBBER', #TODO Give him the capability to inflict wounded on player
  'hp_max':base_hp_general,
  'hp_current':base_hp_general,
  'defense':0,
  'block_power':3,
  'block_duration':4,
  'dodge_chance':5,
  'critical_chance':15,
  'attack':3, #*DONE Update increase attack to 3
  'steal_chance':100,
  'steal_class':'ITEM',
  'item_stolen':{
   'name':'Smoke Veil',
   'description':'How everyone thinks actual smoke bombs work',
   'effect_types':[
    'BUFF',
   ],
   'buff_types':[
    'DODGE'
   ],
   'buff_name':'SPEED+',
   'buff_power':20,
   'buff_duration':3,
   'price':23,
   'usage_message':'You drop the grenade near you!\nYou are now enveloped in smoke!'
  },
  'enemy_has_been_stolen':False,
  'debuff_immunity':[
   None
  ],
  'elemental_resistance':[
   None
  ],
  'elemental_weakness':[
   None
  ],
  #//'debuff_type':[
   #//'SLOW'
  #//],
  #//'debuff_duration':{
   #//'SLOW':3
  #//},
  #//'debuff_strength':{
   #//'SLOW':15
  #//},
  #//'stat_decreased':{
   #//'SLOW':[
    #//'DODGE'
   #//]
  #//},
  #//'buff_type':[
   #//'SPEED+'
  #//],
  #//'buff_duration':{
   #//'SPEED+':4
  #//},
  #//'buff_power':{
   #//'SPEED+':20
  #//},
  #//'buff_stat_increase':{
   #//'SPEED+':[
    #//'DODGE'
   #//]
  #//},
  'attack_effects':{
   'STEAL_GOLD':15
  },

  'special_attacks':{
   'throw_bolas':{
    'effects':[
     'DEBUFF_STAT_PLAYER'
    ],
    'debuff_type':'SLOW',
    'stat_decreased':[
     'DODGE'
    ],
    'stat_debuff_power':15,
    'stat_debuff_duration':3,
    'debuff_apply_chance':100,
    'use_message':'The robber threw bolas at your feet to difficult your movement!'
   },

   'throw_smoke_bomb':{
    'effects':[
     'BUFF_ENEMY_STAT'
    ],
    'buff_apply_chance':100,
    'stat_increased':[
     'DODGE'
    ],
    'buff_type':'SPEED+',
    'buff_power':20,
    'buff_duration':4,
    'use_message':'The robber threw a smoke bomb and is hiding in the smoke!'
   }
  },

  'ai_load':3,
  'gold_drop':randint(20,35),
  'ai_control_value':0,
  'runaway_message':'The robber managed to get away with your gold!'
 }

 base_hp_general=randint(23,37)

 base_hp_general=100 #*debug

 alolan_sandshrew={
  'enemy_name':'ARTIC MOLE',
  'hp_max':base_hp_general,
  'hp_current':base_hp_general,
  'defense':-3,
  'dodge_chance':30,
  'critical_chance':5,
  'attack':6,
  'steal_chance':30,
  'steal_class':'ITEM',
  'item_stolen':{
   'name':'Sharp Icicle',
   'description':'The icicle of an Artic Mole\nAlthough it is used defensively by the moles\nit is sharp enough to be useful as a weapon',
   'effect_types':[
    'DAMAGE'
   ],
   'power_damage':12,
   'elemental':'FROST',
   'usage_message':'You hurl the spike like a dagger on the enemy!'
  },
  'enemy_has_been_stolen':False,
  'debuff_immunity':[
   'FROSTBITE'
  ],
  'elemental_resistance':[
   'FROST'
  ],
  'elemental_weakness':[
   'FIRE'
  ],
  #//'buff_type':[
   #//'HARDEN',
   #//'RUSH'
  #//],
  #//'buff_power':{
   #//'HARDEN':3
  #//},
  #//'buff_stat_increase':{
   #//'HARDEN':[
    #//'DEF'
   #//],
   #//'RUSH':[
    #//'RUSH'
   #//]
  #//},

  'special_attacks':{
   'frost_spikes':{
    'damage':15,
    'elemental':'FROST',
    'accuracy':100,
    'effects':[
     'DAMAGE',
     'DEBUFF_STAT_ENEMY'
    ],
    'stat_debuff_enemy_power':3,
    'stat_debuff_enemy_chance':100,
    'stat_decreased':[
     'DEF'
    ],
    'use_message':"The mole hurls the spikes on it's back at you!"
   },

   'breaking_claw':{
    'damage':9,
    'elemental':None,
    'accuracy':100,
    'effects':[
     'DEBUFF_STAT_PLAYER',
     'DAMAGE'
    ],
    'debuff_apply_chance':50,
    'debuff_type':'WEAK',
    'stat_decreased':[
     'DEF',
     'ATK'
    ],
    'stat_debuff_power':2,
    'stat_debuff_duration':3,
    'use_message':"The mole breaks through you with it's claws!"
   },

   'harden':{
    'effects':[
     'BUFF_ENEMY_STAT'
    ],
    'buff_apply_chance':100,
    'stat_increased':[
     'DEF'
    ],
    'buff_power':3,
    'use_message':"The mole starts growing ice spikes on it's back!"
   },

   'burrow':{
    'effects':[
     'BUFF_ENEMY_STAT'
    ],
    'buff_apply_chance':100,
    'stat_increased':[
     'RUSH'
    ],
    'use_message':'The mole digs and hides away in a hole!'
   }
  },
  'ai_load':4,
  'gold_drop':randint(22,29)
 }

 base_hp_general=randint(29,33)

 weakest_pitbull_named_princess_data={
  'enemy_name':'HOWLER',
  'hp_max':base_hp_general,
  'hp_current':base_hp_general,
  'defense':-2,
  'dodge_chance':10,
  'critical_chance':25,
  'attack':15,
  'steal_chance':0,
  'steal_class':None,
  'item_stolen':None,
  'enemy_has_been_stolen':True,
  'debuff_immunity':[
   None
  ],
  'elemental_resistance':[
   None
  ],
  'elemental_weakness':[
   None
  ],
  'attack_effects':{
   'WOUNDED':2
  },
  'special_attacks':{
   'howl':{
    'effects':[
     'BUFF_ENEMY_STAT'
    ],
    'buff_apply_chance':100,
    'buff_power':15,
    'stat_increased':[
     'CRIT',
    ],
    'buff_type':'PRECISON+',
    'buff_duration':3,
    'use_message':"He let's out sharp howl!"
   }
  },
  'ai_load':5,
  'gold_drop':randint(24,31)
 }

 base_hp_general=randint(56,67)

 gun_sentry_data={
  'enemy_name':'GUN SENTRY',
  'hp_max':base_hp_general,
  'hp_current':base_hp_general,
  'defense':2,
  'block_power':5,
  'block_duration':6,
  'dodge_chance':0,
  'critical_chance':0,
  'attack':20,
  'steal_chance':80,
  'steal_class':'ITEM',
  'item_stolen':{
   'name':'Shock Grenade',
   'description':'A grenade that uses a coil\nto overcharge a crystal\ngenerating an electric explosion',
   'effect_types':[
    'DAMAGE'
   ],
   'power_damage':18,
   'elemental':'SHOCK',
   'price':13,

   'usage_message':'You threw the grenade!\nIt explodes with a thunderous sound!'
  },
  'enemy_has_been_stolen':False,
  'debuff_immunity':[
   'WOUNDED',
   'FROSTBITE',
   'WEAK',
   'POISON'
  ],
  'elemental_resistance':[
   'SHOCK',
   'FROST'
  ],
  'elemental_weakness':[
   'FIRE'
  ],
  'special_attacks':{
   'shock_voley':{
    'effects':[
     'DAMAGE'
    ],
    'accuracy':100,
    'damage':17,
    'use_message':'The sentry fires several shock rounds at you!'
   }
  },
  'ai_load':6,
  'gold_drop':randint(29,39)
 }

 base_hp_general=randint(18,26)

 wasp_drone_data={
  'enemy_name':'GALVANIZED WASP',
  'hp_max':base_hp_general,
  'hp_current':base_hp_general,
  'defense':0,
  'dodge_chance':25,
  'critical_chance':20,
  'attack':10,
  'steal_chance':0,
  'steal_class':None,
  'item_stolen':None,
  'enemy_has_been_stolen':True,
  'debuff_immunity':[
   'POISON'
  ],
  'elemental_resistance':[
   'SHOCK'
  ],
  'elemental_weakness':[
   'EARTH'
  ],
  'special_attacks':{

   'toxic_stinger':{
    'effects':[
     'DAMAGE',
     'DEBUFF_PLAYER_DAMAGE'
    ],
    'damage':10,
    'accuracy':100,
    'damage_debuff_apply_chance':10,
    'debuff_damage':5,
    'debuff_type_damage':'POISON',
    'damage_debuff_duration':3,
    'use_message':"The wasp uses it's stinger to attack!"
   },

   'sharpen':{
    'effects':[
     'BUFF_ENEMY_STAT'
    ],
    'buff_apply_chance':100,
    'buff_power':30,
    'stat_increased':[
     'CRIT'
    ],
    'buff_type':'PRECISION+',
    'buff_duration':3,
    'use_message':"The wasp grinds it's stinger making it sharper!"
   }
  },
  'ai_load':7,
  'gold_drop':randint(32,39)
 }

 base_hp_general=randint(34,47)

 tiki_man_data={
  'enemy_name':"GAIA FOLLOWER",
  'hp_max':base_hp_general,
  'hp_current':base_hp_general,
  'defense':1,
  'block_power':5,
  'block_duration':3,
  'dodge_chance':20,
  'critical_chance':10,
  'attack':5,
  'steal_chance':60,
  'steal_class':'ITEM',
  'item_stolen':{
   'name':'Feather Dart',
   'description':'Did you know? There are species of birds\nwhose feathers are actually poisonous!\nFor real you can look it up',
   'effect_types':[
    'DEBUFF_DAMAGE'
   ],
   'debuff_type':'POISON',
   'elemental':None,
   'power_debuff_damage':2,
   'debuff_turn_duration':6,
   'price':15,
   'usage_message':'You threw the dart straight into the enemy!'
  },
  'enemy_has_been_stolen':False,
  'debuff_immunity':[
   None
  ],
  'elemental_resistance':[
   None
  ],
  'elemental_weakness':[
   'FIRE'
  ],
  'special_attacks':{

   'poison_dart':{
    'effects':[
     'DAMAGE',
     'DEBUFF_PLAYER_DAMAGE'
    ],
    'accuracy':100,
    'damage':4,
    'damage_debuff_apply_chance':65,
    'debuff_type_damage':'POISON',
    'debuff_damage':7,
    'damage_debuff_duration':3,
    'use_message':"The tiki mask spits a green feathered dart\nout of it's blowgun!"
   },

   'weakening_dart':{
    'effects':[
     'DAMAGE',
     'DEBUFF_STAT_PLAYER'
    ],
    'accuracy':100,
    'damage':3,
    'debuff_apply_chance':80,
    'stat_debuff_power':3,
    'stat_decreased':[
     'ATK',
     'DEF'
    ],
    'debuff_type':'WEAK',
    'stat_debuff_duration':4,
    'use_message':"The tiki mask spits a blue feathered dart\nout of it's blowgun!"
   },

   'steel_point_dart':{
    'effects':[
     'DAMAGE'
    ],
    'accuracy':70,
    'damage':17,
    'use_message':"The tiki mask spits a red feathered dart\nout of it's blowgun"
   }

  },
  'ai_load':8,
  'gold_drop':randint(22,40)
 }

 base_hp_general=randint(25,33)

 winter_spirit_data={
  'enemy_name':'WINTER SPIRIT',
  'hp_max':base_hp_general,
  'hp_current':base_hp_general,
  'defense':-4,
  'dodge_chance':30,
  'critical_chance':10,
  'attack':12,
  'steal_chance':0,
  'steal_class':None,
  'item_stolen':None,
  'enemy_has_been_stolen':True,
  'debuff_immunity':[
   'FROSTBITE'
  ],
  'elemental_resistance':[
   'FROST'
  ],
  'elemental_weakness':[
   'FIRE'
  ],
  'attack_effects':{
   'WOUNDED':4
  },
  'special_attacks':{

   #//'ice_shards':{
    #//'effects':[
     #//'DAMAGE',
     #//'DEBUFF_STAT_PLAYER'
    #//],
    #//'damage':12,
    #//'accuracy':100,
    #//'can_crit':True,
    #//'natural_crit_chance':10,
    #//'affected_by_defense':True,
    #//'debuff_apply_chance':45,
    #//'stat_debuff_power':4,
    #//'stat_decreased':[
     #//'ATK'
    #//],
    #//'debuff_type':'WOUNDED',
    #//'stat_debuff_duration':3,
    #//'use_message':"The spirit throws a volley of ice shards at you!"
   #//},

   'chilling_scream':{
    'effects':[
     'DEBUFF_STAT_PLAYER'
    ],
    'debuff_apply_chance':100,
    'stat_debuff_power':2,
    'stat_decreased':[
     'ATK'
    ],
    'use_message':"The spirit let's out a horrific scream that chills your spine!",
   },

   'frozen_mist':{
    'effects':[
     'DEBUFF_STAT_PLAYER'
    ],
    'debuff_apply_chance':100,
    'stat_debuff_power':5,
    'stat_decreased':[
     'DEF'
    ],
    'debuff_type':'FROSTBITE',
    'stat_debuff_duration':4,
    'use_message':"The spirit passes through you with a freezing mist!"
   }
  },
  'ai_load':9,
  'ai_control':0,
  'gold_drop':randint(28,37)
 }

 base_hp_general=randint(24,36)

 fire_spider_oh_god_why={
  'enemy_name':'FIRE WEAVER',
  'hp_max':base_hp_general,
  'hp_current':base_hp_general,
  'defense':-2,
  'dodge_chance':5,
  'critical_chance':5,
  'attack':3,
  'steal_chance':0,
  'steal_class':None,
  'item_stolen':None,
  'enemy_has_been_stolen':True,
  'debuff_immunity':[
   'BURN'
  ],
  'elemental_resistance':[
   'FIRE'
  ],
  'elemental_weakness':[
   'FROST',
   'EARTH'
  ],
  'attack_effects':{
   'BURN':4
  },
  'special_attacks':{

   'fire_web':{
    'effects':[
     'DEBUFF_PLAYER_DAMAGE'
    ],
    'damage_debuff_apply_chance':60,
    'debuff_damage':3,
    'debuff_type_damage':'BURN',
    'damage_debuff_duration':5,
    'use_message':'The Weaver throws a flamming web at you!',
    'damage_debuff_miss_message':"The Weaver missed it's web fling!"
   },

   'ferocious_bite':{
    'effects':[
     'DAMAGE'
    ],
    'accuracy':100,
    'damage':21,
    'use_message':'The Weaver jumped and gave you quite a bite!'
   }
  },
  'ai_load':10,
  'ai_control':0,
  'gold_drop':randint(26,29)
 }

 return [
  zombie_enemy_data,
  slimy_boi_enemy_data,
  mario_piranha_plant_data,
  thief_data,
  alolan_sandshrew,
  weakest_pitbull_named_princess_data,
  gun_sentry_data,
  wasp_drone_data,
  tiki_man_data,
  winter_spirit_data,
  fire_spider_oh_god_why
 ]


# Should figure out a better way for this I hope
def level_1_enemy_ai(
  turn_count,
  #current_player_status,
  player_attack_bonus,
  player_is_debuffed_damage,
  player_is_stat_debuffed,
  enemy_is_blocking,
  enemy_is_stat_buffed,
  enemy_stats,
  enemy_defense_bonus,
  player_damage,
  test_var=None):
 """
 All early enemy ai decisions during combat will be placed here

 test_var: Debug

 turn_count: Current turn number

 current_player_status: Current player status

 player_is_debuffed: Bool value to check if player has active debuff (stat decreases not included)
 
 enemy_stats: the current enemy stats
 """
 #*DONE All none actions should use the actual None value

 match enemy_stats['ai_load']:

  case 0:   #| Zombie AI

   random_action=randint(1,100)

   #* debug, remove after - 23/07/2024
   '''if test_var==0:
    random_action=100

   if test_var>0:
    random_action=100'''

   if random_action<=25:
    message_random=randint(0,2)

    if message_random==0:
     print('The Zombie moves in a uncanny manner')
    
    elif message_random==1:
     print('The Zombie stares you in the eyes')

    elif message_random==2:
     print('The Zombie simply stands aorund')
    
    return None,None

   elif 25<random_action<=50:
    if not enemy_is_blocking:
     print('The Zombie braces itself!')
     return 'DEF',None
    
    else:
     return 'ATK',None
   
   elif 50<random_action<=100:
    print("The Zombie advances with it's sharp claws!")
    return 'ATK',None


  case 1:   #| Slime AI

   random_action=randint(1,100)

   '''if test_var==0:    #*Debug
    random_action=100

   #//elif test_var<=2: and test_var>0:
    
    #//return 'LOWER_STAT',enemy_stats['debuff_type'][0]

   elif test_var>2:
    random_action=29'''

   if random_action<=30:
    print('The Slime merely bounces around')
    return None,None

   elif random_action<=90 and random_action>30:
    print('The Slime bounces on you and it hurts quite a bit!')
    return 'ATK',None

   elif random_action<=100 and random_action>90:
    print('The Slime is preparing to throw something!')
    #//print('Your muscles fill a little numb!')
    return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['goo_spray']


  case 2:   #| Tiger Lily AI

   if not(turn_count%4==0):
    if turn_count%2==0:
     if not player_is_debuffed_damage and not player_is_stat_debuffed:

      special_attack_choice=choice(list(enemy_stats['special_attacks'].values()))
      print('The Tiger Lily is preparing a special move!')

      special_attack_choice=enemy_stats['special_attacks']['entangle'] #*debug

      return 'SPECIAL_ATTACK',special_attack_choice

      #//if debuff_choice=='':
       #//print("The Tiger Lily Prickles you with it's spiky vines!")
       #//return 'OVERTIME_DAMAGE',debuff_choice
      
      #//elif debuff_choice=='SLOW':
       #//print("The Tiger Lily entangles you with it's vines!")
       #//return 'LOWER_STAT',debuff_choice

     else:
      print("The Tiger Lily whips you with it's vines")
      return 'ATK',None

    else:
     print("The Tiger Lily whips you with it's vines!")
     return 'ATK',None
    
   else:
    print('The Tiger Lily seems to rest for a brief moment')
    return None,None


  case 3: #| Grave Robber AI

   if enemy_stats['hp_current']<=((enemy_stats['hp_max']*0.40)+((enemy_stats['hp_max']*0.40)%1>0)):

    if enemy_stats['ai_control_value']>2:
     print('The robber throws a bunch of rocks on you and runs away!')
     return 'RUN',None

    else:
     if not enemy_is_stat_buffed:
      print('The robber is preparing something')
      return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['throw_smoke_bomb']

     elif not enemy_is_blocking:
      print('The robber assumed a defensive stance!')
      return 'DEF',None

     if enemy_is_stat_buffed and enemy_is_blocking:
      print('The robber quickly slashes you with his blade')
      enemy_stats['ai_control_value']+=1
      return 'ATK',None

   else:

    random_action=randint(1,100)

    if random_action<=70 or turn_count%3==0:
     print('The robber quickly slashes you with his blade!')
     return 'ATK',None

    elif 70<random_action<=100:
     print('The robber is preparing something!')
     #//print('It snares your feet, difficulting your movement!')
     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['throw_bolas']


  case 4: #| Artic Mole AI

   if turn_count%2==0:

    if enemy_defense_bonus<3:
     print("The mole is preparing to buff itself!")
     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['harden']

    elif enemy_defense_bonus>=3:
     print('The mole is preparing a special attack!')
     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['frost_spikes']

   else:

    if player_damage>0:
     print('The mole is preparing to buff itself')
     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['burrow']

    else:

     random_action=randint(1,100)

     if random_action<=60:
      print('The mole claws away at you wildly!')
      return 'ATK',None

     elif 60<random_action<=100:
      print('The mole is preparing a special attack!')
      return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['breaking_claw']


  case 5: #| Howler AI

   if not enemy_is_stat_buffed:
    print('The Howler is preparing to buff itself!')
    return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['howl']

   else:
    print("The Howler growls and darts with it's jaw open towards you!")
    return 'ATK',None


  case 6: #| Gun Sentry AI

   if not enemy_is_blocking:
    print("The sentry boosts it's own defense!")
    return 'DEF',None
   
   else:
    random_action=randint(1,100)

    if random_action<=50:
     print("The sentry's systems malfunctioned!")
     return None,None
    
    elif 50<random_action<=100:

     random_action=randint(1,100)

     if random_action<=50:
      print('The sentry shoots a few rounds on you!')
      return 'ATK',None
     
     elif 50<random_action<=100:
      print("The sentry seems to be charging it's gun!")
      return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['shock_voley']


  case 7: #| Galvanized Wasp AI

   if not turn_count%3==0:

    if not enemy_is_stat_buffed:
     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['toxic_stinger']

    else:
     print('The wasp uses a different stinger to strike!')
     return 'ATK',None

   else:
    print('The wasp is preparing to buff itself!')
    return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['sharpen']


  case 8: #| Gaia Follower AI

   if not enemy_stats['hp_current']<=(int((enemy_stats['hp_max']*0.30)+((enemy_stats['hp_max']*0.30)%1>0))):

    random_action=randint(1,100)

    if random_action<=30:
     print('The tiki mask dances around and mocks you!')
     return None,None
    
    else:
     if turn_count%3==0:

      if not player_is_stat_debuffed and not player_is_debuffed_damage:
       print('The tiki mask is pulling out a dart!')
       special_attack_choice=choice([enemy_stats['special_attacks']['poison_dart'],enemy_stats['special_attacks']['weakening_dart']])
       return 'SPECIAL_ATTACK',special_attack_choice
      
      elif not player_is_stat_debuffed:
       print('The tiki mask is pulling out a dart!')
       return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['weakening_dart']
      
      elif not player_is_debuffed_damage:
       print('The tiki mask is pulling out a dart!')
       return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['poison_dart']
      
      else:
       print("The tiki weakly hits you with it's blowgun")
       return 'ATK',None
     
     elif random_action<=85:
      print("The tiki weakly hits you with it's blowgun!")
      return 'ATK',None
     
     elif 85<random_action<=100:
      print('The tiki mask is pulling out a dart!')
      return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['steel_point_dart']

   else:
    if not enemy_is_blocking:
     print("The creature cowers in fear behind it's mask!")
     return 'DEF',None

    else:

     random_action=randint(1,100)

     if random_action<=50:
      print('The creature is shaking in fear behind the mask!')
      return None, None
     
     elif 50<random_action<=100:

      if player_is_debuffed_damage:
       print('The tiki mask is pulling out a dart!')
       return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['steel_point_dart']
      
      else:
       print("The tiki mask is pulling out a dart!")
       return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['poison_dart']



  case 9: #| Winter Spirit AI

   if turn_count==1:
    print('The spirit is starting to get covered mist!')
    return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['frozen_mist']

   else:
    random_action=randint(1,100)
    if player_attack_bonus>0 or random_action<=15:
     print('The spirit is moving in a weird way!')
     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['chilling_scream']
    
    else:
     if enemy_stats['ai_control']==0:
      print('The spirit is conjuring up several ice shards!')
      enemy_stats['ai_control']+=1
      return None,None
     
     elif enemy_stats['ai_control']>0:
      print('The spirit readies an attack!')
      enemy_stats['ai_control']+=1

      if enemy_stats['ai_control']>2:
       enemy_stats['ai_control']=0

      return 'ATK',None


  case 10: #| Fire Weaver AI

   if not player_is_debuffed_damage:
    
    if enemy_stats['ai_control']==2:
     print('The Weaver is preparing itself!')
     enemy_stats['ai_control']=0
     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['ferocious_bite']
    
    else:
     print('The Weaver seems to be weaving something!')
     enemy_stats['ai_control']+=1
     return 'SPECIAL_ATTACK',enemy_stats['special_attacks']['fire_web']
    
   else:
    print('The Weaver gives you a fiery bite!')
    enemy_stats['ai_control']=0
    return 'ATK',None

# Debug
#for i in range(0,20):
# low_enemy_ai_sheet(0)


# Mini boss list
# Must be refactored

# The refactor was done for quite some time now
# Just forgot to comment - 26/08/2024