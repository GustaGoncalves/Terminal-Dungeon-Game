
#* DONE Need to refactor this so it is just a single dict
#* DONE instead of being a but load of variables
#* DONE that become a dict anyways

def thief_base_load():
 """
 This contains all the starting stats of the thief
 When called returns a dictionary with all the stats
 """

 thief_stats:dict ={
  'character_icon':'🦊',
  'hp_max':1000, #*debug, change back to 50
  'hp_current':1000, #*debug, change back to 50
  'dodge_chance':10,
  'attack_current':21,  #* Debug
  'defense':1,
  'block_power':1,
  'block_duration_modifier':3,
  'debuff_power_modifier':0,
  'debuff_duration_modifier':1,
  'critical_chance':10,
  'luck':1,
  'total_item_slots':4,
  'inventory':[],
  'relics':[],
  'elemental_damage_bonus':[],
  'debuff_on_attack':[],
  'life_steal':0, #> This is percentage based, so use floats
  'armor_piercing':0,
  'bonus_healing':0,
  'cooldown_reduction':0,
  'block_decreases_attack':True,
  'player_immunity':[],

  'skill_list':[
   {
    'name':'Steal',
    'description':'Attempt to finesse your way into robbing your enemy',
    'steal_sucess_chance':10
   }
  ],
  'action_available':{
   'steal':True,
   'parry':False,
   'berserk':False
  },

  'money':999, #* Debug
  'first_time_on_shop':True,
  'player_is_alive':True,
  'player_has_taken_damage_this_turn':False
 }


 return thief_stats