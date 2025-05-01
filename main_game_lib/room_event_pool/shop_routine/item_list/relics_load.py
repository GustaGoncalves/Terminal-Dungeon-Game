def persistent_item_sheet():
 """
 Contains the full list of items that persist through play
 return: when called returns a set containing the information of all itens listed
 """


 #0
 relic_hidden_blade:dict ={'name':'Hidden Blade',
                 'description':'A small sharp blade strapped to a arm guard.\nIt uses a spring mechanism to extend and retract\na small blade .',
                 'critical_chance':10,
                 'attack_current':2,
                 'price':46,
                 'bought':False,
                 #//'relic_index':0 #> Used to generate new items and delete already seen ones from the pool of available ones
                 }
 

 #1
 relic_lucky_coin:dict ={'name':'Lucky Coin',
                 'description':'An old rusted coin of copper with no apparent value whatsoever.\nThese are often used as good luck charms by the supersticious.',
                 'luck':1,
                 'critical_chance':5,
                 'dodge_chance':5,
                 'price':34,
                 'bought':False,
                 #//'relic_index':1
                 }
 

 #2
 relic_ruler_scepter:dict ={'name':"Ruler's Scepter",
                 'description':"A rather poor imitation of the scepter\nheld by Lavhren's Pontifex Archard Magnom.\nIt possesses a mere fraction of it's power",
                 'debuff_damage_modifier':2,
                 'debuff_duration_modifier':2,
                 'price':41,
                 'bought':False,
                 #//'relic_index':2
                 }
 

 #3
 relic_armor_plate:dict ={'name':'Armor Plate',
                 'description':'A standard steel plate used for reinforcing armor.\nSurprisingly heavy for such a small plate.',
                 'defense':1,
                 'block_power':3,
                 #//'dodge_chance':-5,
                 'price':41,
                 'bought':False,
                 #//'relic_index':3
                 }
 

 #4
 relic_spark_plug:dict ={'name':'Spark Plug',
                 'description':"An old spark plug. Seems to be faulty,\nas it releases sparks constantly",
                 'elemental_damage_bonus':[
                  #//'FIRE',
                  'SHOCK'
                 ],
                 'price':39,
                 'bought':False,
                 #//'relic_index':4
                 }
 

 #? Change this to cursed relics?
 #5
 relic_syphon_seal:dict ={'name':"Syphon's Seal",
                 'description':'A spiral token held by\nthe ruthless Syphon and his followers.\nRumors tell of their ability to rob ones energy\n and use as their own.',
                 'life_steal':0.30, #> This relic stats are percentage based
                 'hp_max':-0.35,
                 'hp_gain_loss':0,
                 'price':33,
                 'bought':False,
                 #//'relic_index':5
                 }
 

#6
 relic_spike_shield:dict ={'name':'Spike Shield',
                 'description':'A shield with spikes embeded in it.\nThis allows one to attack while defending.',
                 'block_power':1,
                 'attack_current':1,
                 'block_decreases_attack':False,
                 'price':37,
                 'bought':False,
                 #//'relic_index':6
                 }
 

#7
 relic_boot_grease:dict ={'name':'Boot Grease',
                 'description':'A small can with grease for polishing boots.\nEven in the middle of a desert,\ntaking care of your boots is important.',
                 'dodge_chance':15,
                 'price':40,
                 'bought':False,
                 #//'relic_index':7
                 }
 

 #8
 relic_ebony_scarf:dict ={'name':'Ebony Scarf',
                 'description':"Bro really said 'The desert people should use scarfs'", #> Using placeholders like this from now on
                 'has_ebony_scarf':True,
                 'price':40,
                 'bought':False,
                 #//'relic_index':8
                 }
 

 #9
 relic_longinus_spear_tip:dict ={'name':"Longinus' Spear Tip",
                  'description':'You know the guy who stabbed Jesus?\nThis is the tip of his spear, I think...', #> Placeholder
                  'armor_piercing':0.30,
                  'price':40,
                  'bought':False,
                  #//'relic_index':9
                  }


 #10
 relic_gamer_bath_water={
  'name':'Noxious Coating',
  'description':"The forbidden cool aid.\nTry drinking it, it's great!", #> Placeholder
  'debuff_on_attack':[ #> Being makes the process of adding the stat to the player simpler
   'POISON'
  ],
  'attack_current':1,
  'price':45,
  'bought':False,
  #//'relic_index':10
 }


 #11
 relic_igniter={
  'name':'Igniter',
  'description':'Flamming sword on the go.\nOil included!', #? Placeholder?
  'debuff_on_attack':[
   'BURN'
  ],
  'attack_current':1,
  'price':45,
  'bought':False,
  #//'relic_index':11
 }

 #12
 relic_crystal_coin={ #> Stats for this are on combat section
  'name':'Crystal Coin',
  'description':'A coin made solely of crystals.\nHolding makes you feel a little richer',
  'player_has_crystal_coin':True,
  'price':52,
  'bought':False
 }

 #13
 relic_star_amulet={
  'name':'Sacred Star',
  'description':'A star shaped amulet.\nSaid to protect the body of those who wear it',
  'cant_lower_player_attack':True,
  'price':45,
  'bought':False
 }

 #! Don't forget to account for player healing bonuses
 #! when adding any healing skill or other particular stuff
 #! In the future
 #14
 relic_lotus_flower={
  'name':'Hallowed Lotus',
  'description':'A beautiful blue lotus flower.\nHeld by many as sacred, it is believed to possess\nstrong healing capabilities.',
  'bonus_healing':10,
  'price':50,
  'bought':False
 }


 #15
 relic_fenrir_fange={
  'name':"Fenrir's Fang",
  'description':"Big dog who will kill loki's dad", #? Placeholder?
  'debuff_on_attack':[
   'FROSTBITE'
  ],
  'attack_current':1,
  'price':42,
  'bought':False
  #//'relic_index':11
 }

 #16
 relic_noble_mandragora={
  'name':'Noble Mandragora',
  'description':'"Ummm...Ackshually, the correct terminology is mandrake"\n-🤓',
  'player_immunity':[
   'POISON'
  ],
  'defense':1,
  'price':45,
  'bought':False
 }

#17
 relic_cronos_pocketwatch={
  'name':"Cronos' Pocketwatch",
  'description':'Even the god of time,\nought to keep track of things sometimes',
  'cooldown_reduction':1,
  'price':57,
  'bought':False
 }

 #18
 relic_sword_scope_why={
  'name':'Sword Scope',
  'description':'A scope to be placed on a sword\nWho thought this was a good idea??',
  'critical_chance':10,
  'attack_current':-2,
  'player_has_sword_scope':True,
  'price':39,
  'bought':False
 }

 #19
 relic_heavy_duty_boots={
  'name':'Heavy Duty Boots',
  'description':'A heavy pair of boots covered in several steel plates',
  'cant_lower_player_dodge':True,
  #//'dodge_chance':-5,
  'defense':1,
  'price':43,
  'bought':False
 }

 #20
 relic_scale_mail={
  'name':'Scale Mail',
  'description':'A chain mail made with scales of a mythical creature\nIt is said the creature had a breath of fire',
  'player_immunity':[
   'BURN'
  ],
  'defense':2,
  'price':55,
  'bought':False
 }

 #21
 relic_vice_grip={
  'name':'Vice Grip',
  'description':'A tool used by mechanics to hold parts in place',
  'debuff_on_attack':[
   'SLOW'
  ],
  'attack_current':1,
  'price':36,
  'bought':False
 }

#22
 relic_gaia_shovel={
  'name':"Gaia's Shovel",
  'description':'A shovel entangled in vines\nIt has a beautiful flower in it',
  'elemental_damage_bonus':[
   'EARTH'
  ],
  'attack_current':1,
  'price':42,
  'bought':False
 }

 #23
 relic_frost_lirius={
  'name':"Frost Lirius",
  'description':"A beautiful winter born flower.\nGrows near frozen lakes after snowfalls",
  'frostbite_does_damage':True,
  'bonus_healing':2,
  'price':51,
  'bought':False
 }

 #24
 relic_horseshoe={
  'name':'Horseshoe',
  'description':'A famous, albeit less common, good luck charm\nVery few people carry these with them.\nMostly held by those who live on the country side of Hawkwel',
  'first_attack_does_extra_damage':True,
  'luck':1,
  'price':39,
  'bought':False
 }

 #25
 relic_iron_heart={
  'name':'Iron Heart',
  'description':'A small gadget that has a shape resembling a heart\nIt is regarded by engineers as the heart of most machines\nand an important piece for any mechanical',
  'hp_max':25,
  'hp_current':25,
  'defense':1,
  'price':58,
  'bought':False
 }


 return{
  relic_hidden_blade['name']:relic_hidden_blade,
  relic_lucky_coin['name']:relic_lucky_coin,
  relic_ruler_scepter['name']:relic_ruler_scepter,
  relic_armor_plate['name']:relic_armor_plate,
  relic_spark_plug['name']:relic_spark_plug,
  relic_syphon_seal['name']:relic_syphon_seal,
  relic_spike_shield['name']:relic_spike_shield,
  relic_boot_grease['name']:relic_boot_grease,
  relic_ebony_scarf['name']:relic_ebony_scarf,
  relic_longinus_spear_tip['name']:relic_longinus_spear_tip,
  relic_gamer_bath_water['name']:relic_gamer_bath_water,
  relic_igniter['name']:relic_igniter,
  relic_crystal_coin['name']:relic_crystal_coin,
  relic_star_amulet['name']:relic_star_amulet,
  relic_lotus_flower['name']:relic_lotus_flower,
  relic_fenrir_fange['name']:relic_fenrir_fange,
  relic_noble_mandragora['name']:relic_noble_mandragora,
  relic_cronos_pocketwatch['name']:relic_cronos_pocketwatch,
  relic_sword_scope_why['name']:relic_sword_scope_why,
  relic_heavy_duty_boots['name']:relic_heavy_duty_boots,
  relic_scale_mail['name']:relic_scale_mail,
  relic_vice_grip['name']:relic_vice_grip,
  relic_gaia_shovel['name']:relic_gaia_shovel,
  relic_frost_lirius['name']:relic_frost_lirius,
  relic_horseshoe['name']:relic_horseshoe,
  relic_iron_heart['name']:relic_iron_heart
 }