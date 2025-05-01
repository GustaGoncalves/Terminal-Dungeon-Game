
#TODO Separate normal itens and permanent itens in their own files for better maintainabilty
#TODO Organize disposition of item dicts. They are all lined in a weird way
#TODO Add rarity/weight to items and relic, no going around this one, some are better than others


def item_sheet():
 """
 Contains the full list of items that can be obtained or found in shops
 return: when called returns a hashtable containing the information of each item
 """

 # Item 1
 item_throwing_star:dict ={'name':'Bladed Star',
         'description':'A small sharp blade in the shape of a 4 point star.\nMade for throwing',
         'effect_types':[
          'DAMAGE'
         ],
         'elemental':'NULL',
         'power_damage':6,
         'price':10,

         # If you update the stats, don't forget to update the message
         # if necessary - 01/08/2024
         'usage_message':'You threw the Bladed Star on the enemy'
         }


 # Item 2
 item_firecracker:dict ={'name':'Firecracker',
         'description':'A small, weak explosive.\nCommonly used for pranks by the young,\nthough it is still prone to burning.',
         'effect_types':[
          'DEBUFF_DAMAGE',
          'DAMAGE'
         ],
         'debuff_type':'BURN',
         'elemental':'NULL',
         'power_damage':1,
         'power_debuff_damage':2,
         'debuff_turn_duration':3,
         'price':15,

         'usage_message':'You lit and threw the firecracker!\nIt explodes on the enemy.'
         }


 # Item 3
 item_healing_compound:dict ={'name':'Healing Compound',
         'description':'A compound consisting of multiple medicinal herbs.\nCreated and blessed by the clergys of Lavhren.\nIt has a pungent smell.',
         'heal_power':20,
         'effect_types':[
          'HEAL'
         ],
         'price':12,

         'usage_message':'You applied the compound on yourself.\nThe odor now lingers on your body,\nbut you feel much better.'
         }


 # Item 4
 item_shock_grenade:dict ={'name':'Shock Grenade',
         'description':'A grenade that uses a coil\nto overcharge a crystal\ngenerating an electric explosion',
         'effect_types':[
          'DAMAGE'
         ],
         'power_damage':18,
         'elemental':'SHOCK',
         'price':13,

         'usage_message':'You threw the grenade!\nIt explodes with a thunderous sound!'
         }


 # Item 5
 item_lacerating_shiv:dict ={'name':'Lacerating Shiv',
         'description':'A small dented knife.\nDesigned to leave open wounds on opponents',
         'effect_types':[
          'DAMAGE',
          'DEBUFF_STAT', #//Debug, change to DEBUFF_STAT
         ],
         'debuff_type':'WOUNDED',
         'stat_decreased':[
          'ATK',
          #'DEF'
         ],
         'power_damage':6,
         'power_debuff_stat':2,
         'debuff_turn_duration':2,
         'elemental':'NULL',
         'price':17,

         'usage_message':'You throw the shiv!\nIt rips through the enemy leaving it wounded'
         }


 # Item 6
 item_frosted_vial:dict ={'name':'Frosted Vial',
         'description':'This liquid, when in contact with air,\nquickly generates powerful ice spikes\nOften used as a "lockpick" of sorts',
         'effect_types':[
          'DAMAGE'
         ],
         'elemental':'FROST',
         'power_damage':13,
         'price':14,
         'usage_message':'You threw the vial!\nAs it hits the enemy, it creates sharp ice spikes on it!'
         }


 # Item 7
 item_angy_bottle:dict ={
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
         }


 # Item 8
 item_air_up_bottle_lmao:dict ={
         'name':'Bottled Gust',
         'description':'A strong wind burst contained in a bottle.\nMerely holding it make your body feel lighter.',
         'effect_types':[
          'BUFF'
         ],
         'buff_types':[
          'RUSH'
         ],
         'price':8,

         'usage_message':'As soon as you opened the bottle\nA powerful gale blasted the lid away and now envelops you.\nYou feel much lighter and faster'
         }


 # Item 9
 item_panacea:dict ={
  'name':'Panacea'
  ,'description':'A mythical one-for-all solution for ailments.\nRather expensive for a small bottle.'
  ,'effect_types':[
          'HEAL_DEBUFF'
         ],
         'debuff_healed':[
          'ALL'
         ],
         'usage_message':'You drink all the contents of the bottle!\nIt has a perplexing after taste.',
         'price':40
         }
 

 # Item 10
 item_damage_debuff_amp_stone:dict ={'name':'Power Amplifier'
          ,'description':'A cracked red jewel used for boosting the power of certain ailments.\nIt might have enough strength for one more boost'
          ,'effect_types':[
           'UNIQUE_BUFF'
          ],
          'buff_types':[
           'DAMAGE_DEBUFF_DAMAGE'
          ],
          'buff_power':0.5, #> Percentage based
          'usage_message':'As you use the jewel it breaks apart!\nA powerful aura fills the room!',
          'price':28
          }


 # Item 11
 item_feather_dart={
  'name':'Feather Dart',
  'description':'Did you know? There are species of birds\nwhose feathers are actually poisonous!\nFor real you can look it up',
  'effect_types':[
   'DEBUFF_DAMAGE'
  ],
  'debuff_type':'POISON',
  'elemental':'NULL',
  'power_debuff_damage':2,
  'debuff_turn_duration':6,
  'price':15,

  'usage_message':'You threw the dart straight into the enemy!'
 }


 # Item 12
 item_ice_charge:dict ={
  'name':'Ice Charge',
  'description':"Y'know the minecraft Fire Charge?\nImagine that, but ice",
  'effect_types':[
   'DAMAGE'
  ],
  'elemental':'FROST',
  'power_damage':12,
  'price':24,

  'usage_message':'You used the charge on the enemy!\nThey are suddenly hit with an ice blast!'
 }


 # Item 13
 item_blizzard_in_a_bottle={
  'name':'Blizzard in a Bottle',
  'description':'Supposedly allows you to jump mid air\nRather just throw it',
  'effect_types':[
   'DEBUFF_STAT'
  ],
  'debuff_type':'FROSTBITE',
  'stat_decreased':[
   'DEF'
  ],
  'elemental':'FROST',
  'power_debuff_stat':2,
  'debuff_turn_duration':3,
  'price':20,

  'usage_message':'You throw the bottle on the enemy\nAs it hits him a burst of snow covers it!'
 }

 #Item 14
 item_smoke_bomb={
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
 }

 #item15
 item_stat_debuff_amp_stone={
  'name':'Intesity Amplifier',
  'description':'A broken stone used to increase the intensity of certain ailments\nIt might have a bit of power left still',
  'effect_types':[
  'UNIQUE_BUFF'
  ],
  'buff_types':[
   'STRENGTH_STAT_DEBUFF'
  ],
  'buff_power':0.5,
  'usage_message':'The gem breaks apart as soon as you use it!\nAn intense aura fills the room',
  'price':34
 }

 #item 16
 item_obsidian_dagger={
  'name':'Obsidian Dagger',
  'description':'The geologist weapon of choice.\nFun fact! Obsidian is very fragile due to being volcanic glass',
  'effect_types':[
   'DAMAGE',
   'DEBUFF_STAT'
  ],
  'power_damage':2,
  'elemental':'EARTH',
  'debuff_type':'WOUNDED',
  'power_debuff_stat':3,
  'stat_decreased':[
   'ATK'
  ],
  'debuff_turn_duration':3,
  'usage_message':'You throw the obsidian dagger on the enemy!\nIt breaks on hit leaving multiple wounds!',
  'price':28
 }

 #item 17
 item_strength_drink={ #?Should this item boost crits too?
  'name':'Power Tonic',
  'description':'A ready to drink protein mix\nGives a quick boost on the fly',
  'effect_types':[
   'BUFF'
  ],
  'buff_types':[
   'ATK'
  ],
  'buff_power':2,
  'usage_message':'You drink the whole bottle in one go\nIt has a strong bitter taste',
  'price':25
 }

 #item 18
 item_defense_drink={
  'name':'Dextrous Beverage',
  'description':'A relaxing drink with a pleasant scent\nYour senses sharpen just with the smell',
  'effect_types':[
   'BUFF'
  ],
  'buff_types':[
   'DEF'
  ],
  'buff_power':2,
  'usage_message':'You drink the contents of the bottle\nIt has light sweetness to it',
  'price':25
 }

 #item 19
 item_old_clock_gear={
  'name':'Old Clock Gear',
  'description':"A fairly rusty clock gear\nSupposedly used on Cronos' personal clock",
  'effect_types':[
   'UNIQUE_BUFF'
  ],
  'buff_types':[
   'DEBUFF_DURATION'
  ],
  'duration_increase_multiplier':2,
  'usage_message':"As you pull out the gear,\nit starts spinning on it's own",
  'price':35
 }

 #item 20
 item_boltarang={
  'name':'Boltarang',
  'description':'A lightning shaped boomerang\nthat can hit enemies twice with electricity',
  'effect_types':[
   'DAMAGE'
  ],
  'power_damage':10,
  'elemental':'SHOCK',
  'item_charges':2,
  'usage_messages':[
   'You throw the boomerang once more, but miss the enemy!\nHowever the boomerang hits the enemy on the way back',
   'You threw the boomerang at the enemy!'
  ],
  'price':42
 }

 return [item_throwing_star,
         item_firecracker,
         item_healing_compound,
         item_shock_grenade,
         item_lacerating_shiv,
         item_frosted_vial,
         item_angy_bottle,
         item_air_up_bottle_lmao,
         item_panacea,
         item_damage_debuff_amp_stone,
         item_feather_dart,
         item_ice_charge,
         item_blizzard_in_a_bottle,
         item_smoke_bomb,
         item_stat_debuff_amp_stone,
         item_obsidian_dagger,
         item_strength_drink,
         item_defense_drink,
         item_old_clock_gear,
         item_boltarang
 ]