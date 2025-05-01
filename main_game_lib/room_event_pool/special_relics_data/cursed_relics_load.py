def cursed_relics():
 """
 Contains the data of all the cursed relics
 """

 glass_dagger={ #! Stats for this relic are on the combat, item effects and skill effects functions.
  'name':'Glass Dagger',
  'description':'Turns out this actually obsidian.\nNot much of difference really', #? Placeholder?
  'player_has_glass_dagger':True
 }


 stone_armor={ #> Stats for this relic are done in the combat section of the code
  'name':'Stone Bulwark',
  'description':'An armor made of stone.\nNothing else to say about it really', #> Placeholdeer
  'player_has_stone_armor':True,
  'defense':10
 }


 rolling_pendulum={ #> Stats for this relic are on the combat section
  'name':'Rolling Pendulum',
  'description':'Kinda like the Newton Pendulum,\nbut on a little see-saw', #> Placeholder
  'player_has_rolling_pendulum':True,
  #//'relic_index':12
 }

 #! Don't forget to add the blood talisman functionality to all future
 #! COMBAT EXCLUSIVE healing moves
 blood_talisman={ #> This relic functionality is on the combat section
  'name':'Blood Talisman',
  'description':'"Sacrifice is the path for power"',
  'hp_max':-0.10,
  'hp_gain_loss':0,
  'life_steal':0.10,
  'player_has_blood_talisman':True
 }


 twisting_dagger={ #> This relic functionality is on the combat section
  'name':'Twisting Dagger',
  'description':'Would a dagger like this actually be useful?\nGeniuine question here',
  'player_attack_is_halved':True,
  'critical_chance':50
 }


 mark_of_the_fighter={
  'name':'Mark of the Fighter',
  'description':'The best defense is killing the shit\nout of the enemy before he hits you',
  'player_cant_block':True,
  'attack_current':10,
  'defense':-5,
  'dodge_chance':-20,
  'critical_chance':5
 }


 hermes_cronometer={
  'name':"Hermes' Cronometer",
  'description': 'The times registered on this thing are ludicrous',
  'player_has_hermes_cronometer':True
 }


 runebook_of_power={
  'name':'Runebook Of Power',
  'description':'Verba Potestatem Habent',
  'player_has_runebook_of_power':True
 }


 return[
  glass_dagger,
  stone_armor,
  rolling_pendulum,
  blood_talisman,
  twisting_dagger,
  mark_of_the_fighter,
  hermes_cronometer,
  runebook_of_power
 ]