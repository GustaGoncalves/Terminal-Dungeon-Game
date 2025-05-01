 #TODO Add rarity/weight to skills, no going around this one, some are better than others

def skill_data_sheet():
 """
 Contains all data from all skills available for the player to purchase
 """

 #1
 skill_charge_coil={
  'name':'Charge Coil',
  'description':'A sturdy steel coil made to be carried around.\nOriginally designed for recharging tools,\nbut due to the crystals fused in it increasing the power output,\nit is now used as way to energize and enpower weapons.',
  'effect_types':[
   'BUFF',
   'DAMAGE_SELF'
  ],
  'stat_increased':[
   'ATK'
  ],
  'buff_power':2,
  'buff_apply_chance':100,
  'self_damage_power':7,
  'self_damage_chance':100,
  'has_been_bought':False,
  'cooldown_turn_total':2, # Why did I choose to do this
  'skill_is_in_cooldown':False,
  'use_message':'You activate the coil.\nYou got yourself shocked!\nBut your weapon is now electrically charged!',
  'price':39
  #//'skill_index':0 #> Used for updating current pool of skills
 }

 #2
 skill_flame_essence={
  'name':'Flame Essence',
  'description':'The crystalized fire of a mythical creature.\nIt is warm to the touch.',
  'effect_types':[
   'DAMAGE',
   'DEBUFF_DAMAGE',
   #//'DEBUFF_SELF'
  ],
  'debuff_type':'BURN',
  'elemental':'FIRE',
  'attack_success_chance':100,
  'damage_power':9,
  #//'debuff_apply_chance_self':30,
  'debuff_apply_chance_enemy':70,
  #//'self_debuff_power':7,
  'debuff_power': 3,
  'debuff_duration':3,  # In turns
  #//'self_debuff_duration':3,
  'has_been_bought':False,
  'cooldown_turn_total':3,
  'skill_is_in_cooldown':False,
  'use_message':'You extend your hand towards the enemy\nSuddenly, flames wildly fly and hit it!',
  #//'use_message_hurt_self':'The flames flight is so wild\nthat some hit you too!',
  'price':35,
  #//'skill_index':1
 }

 #3
 skill_frost_core={
  'name':'Frost Core',
  'description':'A cracked core of Ice Golem.\nIt possesses a freezing aura surrounding it',
  'effect_types':[
   'DAMAGE',
   'DEBUFF_STAT',
   'DEBUFF_SELF_STAT'
  ],
  'debuff_type':'FROSTBITE',
  'stat_decreased':[
   'DEF'
  ],
  'elemental':'FROST',
  'attack_success_chance':100,
  'damage_power':9,
  'debuff_apply_chance_self':40,
  'debuff_apply_chance_enemy':95,
  'self_stat_debuff_power':3,
  'stat_debuff_power':5,
  'stat_debuff_duration':4,
  'self_stat_debuff_duration':4,
  'has_been_bought':False,
  'cooldown_turn_total':5,
  'skill_is_in_cooldown':False,
  'price':43,
  'use_message':'You hold the core towards the enemy!\nA sudden small blizzard hits the enemy',
  'use_message_hurt_self':'The frigid aura of the core\nfreezed your own hand!',
  #//'skill_index':2
 }

 #4
 skill_throw_lance={
  'name':'Mystical Spear',
  'description':'A spear blessed by [Insert god from Lavhren].\nA spear so powerful that merely holding it,\ncan be difficult and exhausting.', #> Placeholder
  'effect_types':[
   'DAMAGE',
   'DEBUFF_SELF_SPECIAL'
  ],
  'attack_success_chance':100,
  'elemental':None,
  'damage_power':65,
  'debuff_type':'SKIP_TURN',
  'debuff_apply_chance_self':100,
  #//'skip_player_turn':True,
  'cooldown_turn_total':7,
  'skill_is_in_cooldown':False,
  'has_been_bought':False,
  'price':37,
  'use_message':'You hold the lance tight and\nthrow it with all your might!',
  'use_message_hurt_self':'You now feel exhausted from the throw',
  #//'skill_index':3
 }

 #5
 skill_10S_MKII_mini_subwoofer={
  'name':'Silencer',
  'description':"This is actually a really small subwoofer.\nOne has to wonder why it's called silencer.",
  'effect_types':[
   'DEBUFF_ENEMY_SPECIAL',
   'DEBUFF_SELF_SPECIAL'
  ],
  'debuff_type':'SILENCE',
  'debuff_duration':3,
  'debuff_duration_self':2,
  'debuff_apply_chance_self':100,
  'debuff_apply_chance_enemy':100,
  'has_been_bought':False,
  'cooldown_turn_total':6,
  'skill_is_in_cooldown':False,
  'price':49,
  'use_message':'You turn the silencer on!\nIt makes a terribly loud noise\n-10/10 not actually silent',
  'use_message_hurt_self':'After using it, things get awfully silen --OOOOHHH\nThis is why it is called silencer!'
  #//'skill_index':4
 }

 #6
 skill_wind_shawl={
  'name':"Djinn's Shawl",
  'description':'A shawl said to be of some djinn.\nIt has a distinct cloud pattern.',
  'effect_types':[
   'BUFF',
   'DEBUFF_SELF_STAT'
  ],
  'stat_increased':[
   'RUSH'
  ],
  'stat_decreased':[
   'DEF'
  ],
  'self_stat_debuff_power':2,
  'buff_apply_chance':100,
  'debuff_apply_chance_self':100,
  'has_been_bought':False,
  'cooldown_turn_total':5,
  'skill_is_in_cooldown':False,
  'use_message':'You hold the shawl tight in your hands!\nSuddenly you are enveloped by a strong wind current!',
  'use_message_hurt_self':'After using the shawl,\nYour body feels lighter than usual!',
  'price':51
 }

 #7
 skill_winter_fan={
  'name':'Winter Fan',
  'description':'A light blue fan with a snowflake on it.\nCapable of creating small blizzards',
  'effect_types':[
   'DEBUFF_STAT',
   'BUFF_ENEMY_STAT'
  ],
  'debuff_type':'FROSTBITE',
  'buff_type':'SPEED+',
  'stat_increased_enemy':[
   'DODGE'
  ],
  'stat_decreased':[
   'DEF'
  ],
  'buff_enemy_stat_chance':100,
  'debuff_apply_chance_enemy':100,
  'enemy_buff_power':10,
  'enemy_buff_duration':4,
  'stat_debuff_power':2,
  'stat_debuff_duration':4,
  'has_been_bought':False,
  'cooldown_turn_total':3,
  'skill_is_in_cooldown':False,
  'price':43,
  'use_message':'With one wave of the fan, strong winds blow\n and envelop the enemy in a snowstorm!',
  'use_message_hurt_self':'The blizzard makes the enemy more difficult to see',
  #//'skill_index':2
 }

 #8
 skill_ivy_whip={
  'name':'Ivy Whip',
  'description':'-"Wait Belladonna? Isnt that poisonous?"\n-"Yes"\n-"Should I be concerned?"\n-"Im not"\n  - Sierra Knox to Agent 47',
  'effect_types':[
  'DAMAGE',
  'DEBUFF_DAMAGE',
  'DEBUFF_SELF'
  ],
  'debuff_type':'POISON',
  'elemental':None,
  'damage_power':3,
  'attack_success_chance':100,
  'debuff_apply_chance_self':60,
  'debuff_apply_chance_enemy':85,
  'self_debuff_power':5,
  'debuff_power': 10,
  'debuff_duration':3,
  'self_debuff_duration':3,
  'has_been_bought':False,
  'cooldown_turn_total':4,
  'skill_is_in_cooldown':False,
  'use_message':'You whip the enemy!\nFlowers fly all over as you swing it!',
  'use_message_hurt_self':'-"Oh...Doctor I dont feel so good..."\n-"Dont worry. Itll all be over soon, Miss Knox"',
  'price':45
 }

 #9
 skill_shock_pistol={
  'name':'Shock Pistol',
  'description':'A pistol that shoots electric bullets\nLike the average M16 it jams.',
  'effect_types':[
   'DAMAGE'
  ],
  'damage_power':20,
  'elemental':'SHOCK',
  'attack_success_chance':75,
  'has_been_bought':False,
  'cooldown_turn_total':4,
  'skill_is_in_cooldown':False,
  'use_message':'Aiming the pistol at the enemy head, you pull the trigger!',
  'use_message_fail':'The gun jams and wastes the shot!',
  'price':39
 }

 #10
 skill_sharpening_stone={
  'name':'Sharpening Stone',
  'description':'A small flint like stone.\nUsed to sharpen edges of blades and such.',
  'effect_types':[
   'BUFF',
   'LOWER_STAT'
  ],
  'stat_increased':[
   'CRIT'
  ],
  'buff_type':'PRECISION+',
  'buff_power':25,
  'buff_duration':4,
  'stat_decreased':[
   'ATK'
  ],
  'debuff_power':1,
  'buff_apply_chance':100,
  'debuff_apply_chance_self':65,
  'cooldown_turn_total':6,
  'skill_is_in_cooldown':False,
  'has_been_bought':False,
  'use_message_hurt_self':'You end up slightly chipping your weapon while sharpening!',
  'use_message':'You pull the stone out an quickly start\nsharpening your weapon!',
  'price':47
 }

 #11
 skill_dragon_gauntlet={
  'name':'Dragon Gauntlet',
  'description':'A gauntlet decorated with scales.\nThey possess a beautiful color\nIt emanates the power of a mythical creature',
  'effect_types':[
   'DAMAGE',
   'DEBUFF_SELF'
  ],
  'damage_power':23,
  'elemental':'FIRE',
  'attack_success_chance':100,
  'debuff_type':'BURN',
  'debuff_apply_chance_self':85,
  'self_debuff_power':7,
  'self_debuff_duration':3,
  'has_been_bought':False,
  'cooldown_turn_total':4,
  'skill_is_in_cooldown':False,
  'use_message':'You throw a fiery uppercut on your enemy!',
  'use_message_hurt_self':'After the strike, you can feel your skin\nburning inside the gauntlet!',
  'price':50
 }

 #12
 skill_snap_freeze={
  'name':'Snap Freeze',
  'description':'Instantaneous ice at the tip of your fingers!',
  'effect_types':[
   'DAMAGE',
   'DEBUFF_STAT'
  ],
  'damage_power':13,
  'elemental':'FROST',
  'attack_success_chance':100,
  'debuff_type':'FROSTBITE',
  'debuff_apply_chance_enemy':10,
  'stat_debuff_power':2,
  'stat_decreased':[
   'DEF'
  ],
  'stat_debuff_duration':2,
  'has_been_bought':False,
  'price':39,
  'cooldown_turn_total':4,
  'skill_is_in_cooldown':False,
  'use_message':'You snap your fingers!\nSeveral icicles fly from your finger and hit the enemy!'
 }

 #13
 skill_ensnaring_vines={
  'name':'Ensnaring Vines',
  'description':'A collection of tightly tangled vines\nThe more you try separating them\nthe more they seem to mesh together',
  'effect_types':[
   'DAMAGE',
   'DEBUFF_STAT',
   'DEBUFF_SELF_STAT'
  ],
  'attack_success_chance':100,
  'damage_power':15,
  'elemental':'EARTH',
  'debuff_apply_chance_enemy':50,
  'debuff_type':'SLOW',
  'stat_debuff_power':15,
  'stat_decreased':[
   'DODGE'
  ],
  'stat_debuff_duration':3,
  'debuff_apply_chance_self':70,
  'self_stat_debuff_power':20,
  'self_stat_debuff_duration':4,
  'use_message':'The vines pierce through the earth towards the enemy!\nThey constrict him strongly',
  'use_message_hurt_self':'You end up getting yourself wrapped on the vines!',
  'has_been_bought':False,
  'price':42,
  'cooldown_turn_total':3,
  'skill_is_in_cooldown':False
 }

 #14
 skill_the_onion={
  'name':'The Onion',
  'description':'A seemingly regular onion\nFor some reason, you want to eat it',
  'effect_types':[
   'DEBUFF_DAMAGE'
  ],
  'debuff_type':'POISON',
  'debuff_apply_chance_enemy':100,
  'debuff_power':2,
  'debuff_duration':4,
  'has_been_bought':False,
  'price':34,
  'cooldown_turn_total':2,
  'use_message':'Turns out that onion gave poison breath!\nWho would have thought'
 }

 #15
 skill_ice_rapier={
  'name':'Ice Rapier',
  'description':'Conjure a sharp and thorny ice rapier!',
  'effect_types':[
   'DAMAGE',
   'DEBUFF_STAT'
  ],
  'attack_success_chance':100,
  'damage_power':22,
  'elemental':'FROST',
  'debuff_type':'WOUNDED',
  'debuff_apply_chance_enemy':40,
  'stat_debuff_power':4,
  'stat_decreased':[
   'ATK'
  ],
  'stat_debuff_duration':5,
  'use_message':'You conjure the ice rapier and pierce the opponent with it!',
  'has_been_bought':False,
  'cooldown_turn_total':9,
  'price':60
 }

 #16
 skill_stone_wall={
  'name':'Stone Wall',
  'description':'Raise a wall for protection',
  'effect_types':[
   'BUFF',
   'BUFF_ENEMY_STAT'
  ],
  'buff_apply_chance':100,
  'buff_power':3,
  'stat_increased':[
   'DEF'
  ],
  'buff_enemy_stat_chance':100,
  'enemy_buff_power':2,
  'stat_increased_enemy':[
   'DEF'
  ],
  'use_message':'You slam your foot on the earth\nand raise a wall with your hands',
  'use_message_hurt_self':'Turns out the enemy can also use your wall',
  'has_been_bought':False,
  'cooldown_turn_total':4,
  'price':39
 }

 #17
 skill_boulder_dash={
  'name':'Boulder Dash',
  'description':'Case yourself in boulders\nand body your enemy at full speed',
  'effect_types':[
   'DAMAGE'
  ],
  'attack_success_chance':100,
  'elemental':'EARTH',
  'defense_for_damage':True,
  'use_message':'You create a rocky armor and\nthrow yourself into the enemy!',
  'has_been_bought':False,
  'cooldown_turn_total':4,
  'price':28
 }

 #18
 skill_hi_jump_kick={
  'name':'Lightning Step',
  'description':'Dash and leap into the air\nRaining down on your opponent a lightning kick!',
  'effect_types':[
   'DAMAGE'
  ],
  'attack_success_chance':70,
  'elemental':'SHOCK',
  'damage_power':45,
  'use_message':'You take a lightining quick step, jump into the air\nAnd aim a shocking kick towards the enemy',
  'use_message_fail':'You end up missing your opponent\nand crashing on the ground!',
  'damage_self':45//2,
  'price':45,
  'has_been_bought':False,
  'cooldown_turn_total':7
 }

 #19
 skill_dull_cry={
  'name':'Dull Cry',
  'description':"A cry so dull it disappoints the enemy\nIt's like you're not even trying to make it sound real",
  'effect_types':[
   'DEBUFF_STAT'
  ],
  'debuff_apply_chance_enemy':100,
  'debuff_type':'BLUNTED',
  'stat_debuff_power':25,
  'stat_decreased':[
   'CRIT'
  ],
  'stat_debuff_duration':5,
  'use_message':"You let out a loud cry!\nIt felt fake and forced as if you didn't care\nThe enemy seems disappointed with you",
  'price':42,
  'has_been_bought':False,
  'cooldown_turn_total':5
 }

 #20
 skill_stone_barrage={
  'name':'Stone Barrage',
  'description':'Quickly hurl several rocks on your enemy',
  'effect_types':[
   'DAMAGE'
  ],
  'attack_success_chance':100,
  'damage_power':14,
  'elemental':'EARTH',
  'price':36,
  'has_been_bought':False,
  'cooldown_turn_total':3,
  'use_message':'You raise the rocks on your surroundings\nand launch them at the enemy'
 }

 #21
 skill_drug_adction={
  'name':'Hyper Booster',
  'description':"A power supplement that gives you\nquite the strength boost!\nJust don't take too many at once",
  'effect_types':[
   'BUFF',
   'DEBUFF_SELF_STAT'
  ],
  'buff_apply_chance':100,
  'stat_increased':[
   'RAGE'
  ],
  'debuff_apply_chance_self':100,
  'stat_decreased':[
   'ATK'
  ],
  'self_stat_debuff_power':2,
  'price':42,
  'has_been_bought':False,
  'cooldown_turn_total':2,
  'use_message':'You gulp one of the boosters!\nYou feel a sudden rush of energy through you!',
  'use_message_hurt_self':'However your body feels a bit weird\nand compelled to keep taking these...'
 }

 #22
 skill_zap_glove={
  'name':'Zapping Glove',
  'description':'A glove that emits electric shocks\nAlthough often used as a engineer tool\nThe charges it generates can still hurt quite a bit',
  'effect_types':[
   'DAMAGE'
  ],
  'attack_success_chance':100,
  'elemental':'SHOCK',
  'damage_power':14,
  'price':38,
  'has_been_bought':False,
  'cooldown_turn_total':4,
  'use_message':'You charge your fist with electricity\nand give the enemy a strong punch'
 }

 #23
 skill_dash_slide={
  'name':'Dash Slide',
  'description':"A fighting technique where you dash\nand hit the enemy with slide, breaking their balance",
  'effect_types':[
   'DAMAGE',
   'DEBUFF_STAT',
   #//'DEBUFF_SELF',
   'BUFF'
  ],
  'buff_apply_chance':75,
  'buff_power':15,
  'stat_increased':[
   'DODGE'
  ],
  'buff_type':'SPEED+',
  'buff_duration':4,
  'attack_success_chance':75,
  'damage_power':19,
  'elemental':None,
  'damage_self':19,
  'debuff_apply_chance_enemy':75,
  'debuff_type':'SLOW',
  'stat_debuff_power':15,
  'stat_decreased':[
   'DODGE'
  ],
  'stat_debuff_duration':4,
  'self_stat_debuff_power':15,
  'self_stat_debuff_duration':4,
  'use_message':'You perform a quick dash\nchaining a speedy slide towards the enemy',
  'use_message_fail':'You end up missing the enemy\nand crash yourself against a wall',
  'price':45,
  'has_been_bought':False,
  'cooldown_turn_total':5,
 }

 #24
 skill_rupture={
  'name':'Rupture',
  'description':"Slam the ground, causing it to split\nand hit the enemy with the might of the earth",
  'use_message':'You slam your foot against the ground!\nIt trembles and explodes with a massive rupture on the enemy',
  'effect_types':[
   'DAMAGE'
  ],
  'attack_success_chance':100,
  'damage_power':16,
  'elemental':'EARTH',
  'debuff_for_bonus_damage':'SLOW',
  'bonus_damage_from_debuff':10,
  'price':45,
  'has_been_bought':False,
  'cooldown_turn_total':5
 }

 #25
 skill_bipolar_strike={
  'name':'Bipolar Strike',
  'description':'A weird technique that seemingly\ngains and loses in a fix interval',
  'use_message':'You swing at your enemy with an unnusual technique',
  'effect_types':[
   'DAMAGE'
  ],
  'attack_success_chance':100,
  'damage_power':10,
  'elemental':'SHOCK',
  'turn_divisor':2,
  'damage_mod_for_turns':5,
  'price':39,
  'has_been_bought':False,
  'cooldown_turn_total':3
 }

 #26
 skill_combust={
  'name':"Combust",
  'description':'Hit the enemy with an unholy fire\nThat strengthens burns',
  'use_message':'You create a ball of unholy fire\nand hurls it at the enemy',
  'effect_types':[
   'DEBUFF_DAMAGE'
  ],
  'debuff_power':16,
  'debuff_apply_chance_enemy':100,
  'debuff_type':'BURN',
  'message_skill_fail':"The fire passes through the enemy\nseemingly doing nothing",
  'price':42,
  'has_been_bought':False,
  'cooldown_turn_total':2
 }

 #27
 skill_power_through={
  'name':"Power Through",
  'description':"Harden your body in response to physical attacks\nIn order to improve your defenses",
  'use_message':'You harden your body through your wounds',
  'effect_types':[
   'BUFF'
  ],
  'buff_apply_chance':0,
  'activation_condition_type':[
   'PLAYER_TAKEN_DAMAGE'
  ],
  'buff_power':3,
  'stat_increased':[
   'DEF'
  ],
  'message_skill_fail':"As you weren't damaged this turn\nThe skill fails to have any effect",
  'price':45,
  'has_been_bought':False,
  'cooldown_turn_total':5
 }

 #28
 skill_swift_blow={
  'name':'Swift Blow',
  'description':"A lightning quick punch\nthrown right at the start of combat\nbefore the enemy can react",
  'use_message':"You rapidly strike the enemy before it can react",
  'effect_types':[
   'DAMAGE'
  ],
  'attack_success_chance':100,
  'activation_condition_type':[
   'TURN_SPECIFIC'
  ],
  'turn_for_activation':1,
  'damage_power':22,
  'elemental':None,
  'use_message_fail':"Despite your best efforts\nYou weren't quick enough\nand the enemy managed to avoid the attack",
  'price':47,
  'has_been_bought':False,
  'cooldown_turn_total':1
 }

 #29
 skill_bold_strike={
  'name':"Bold Strike",
  'description':"Attack the enemy with full force\ndisregarding your own safety for increased power",
  'use_message':'You jump agressively towards the enemy',
  'effect_types':[
   'DAMAGE_SELF',
   'DAMAGE'
  ],
  'self_damage_chance':55,
  'self_damage_power':24,
  'attack_success_chance':100,
  'damage_power':37,
  'elemental':None,
  'price':52,
  'has_been_bought':False,
  'cooldown_turn_total':7
 }

 #30
 skill_regenerate={
  'name':"Regenerate",
  'description':"Rest for a brief moment\nin order to recover from injuries",
  'use_message':'You stop for a brief moment\nand start recovering from your wounds',
  'effect_types':[
   'HEAL_PLAYER',
   'DEBUFF_SELF_SPECIAL'
  ],
  'heal_success_chance':100,
  'heal_power':35,
  'debuff_apply_chance_self':100,
  'use_message_hurt_self':'Your body needs resting in order to heal',
  'debuff_type':'SKIP_TURN',
  'price':60,
  'has_been_bought':False,
  'cooldown_turn_total':8
 }

 #31
 skill_spin_kick={
  'name':"Spin Kick",
  'description':'Spin around kicking your enemy\nwith increasing speed and force each consecutive hit',
  'effect_types':[
   'DAMAGE'
  ],
  'attack_success_chance':100,
  'elemental':None,
  'last_turn_used':0,
  'damage_power':-1,
  'original_damage':5,
  'damage_increased':6,
  'price':43,
  'has_been_bought':False,
  'cooldown_turn_total':0,
  'use_message':'You spin on your head, gathering momentum\nand hitting the enemy with a kick'
 }

 #32
 skill_caustic_strike={
  'name':"Caustic Strike",
  'description':"An insidious attack using a dagger\nIt is covered in a liquid that takes advantage\nfrom poisonous substances being present on the enemy",
  'use_message':'You strike the enemy with a coated dagger!',
  'effect_types':[
   'DAMAGE'
  ],
  'debuff_for_bonus_damage':'POISON',
  'elemental':None,
  'bonus_damage_from_debuff':21,
  'damage_power':4,
  'attack_success_chance':100,
  'price':32,
  'has_been_bought':False,
  'cooldown_turn_total':3
 }


 return{
  skill_charge_coil['name']:skill_charge_coil,
  skill_flame_essence['name']:skill_flame_essence,
  skill_frost_core['name']:skill_frost_core,
  skill_throw_lance['name']:skill_throw_lance,
  skill_10S_MKII_mini_subwoofer['name']:skill_10S_MKII_mini_subwoofer,
  skill_wind_shawl['name']:skill_wind_shawl,
  skill_winter_fan['name']:skill_winter_fan,
  skill_ivy_whip['name']:skill_ivy_whip,
  skill_shock_pistol['name']:skill_shock_pistol,
  skill_sharpening_stone['name']:skill_sharpening_stone,
  skill_dragon_gauntlet['name']:skill_dragon_gauntlet,
  skill_snap_freeze['name']:skill_snap_freeze,
  skill_ensnaring_vines['name']:skill_ensnaring_vines,
  skill_the_onion['name']:skill_the_onion,
  skill_ice_rapier['name']:skill_ice_rapier,
  skill_stone_wall['name']:skill_stone_wall,
  skill_boulder_dash['name']:skill_boulder_dash,
  skill_hi_jump_kick['name']:skill_hi_jump_kick,
  skill_dull_cry['name']:skill_dull_cry,
  skill_stone_barrage['name']:skill_stone_barrage,
  skill_drug_adction['name']:skill_drug_adction,
  skill_zap_glove['name']:skill_zap_glove,
  skill_dash_slide['name']:skill_dash_slide,
  skill_rupture['name']:skill_rupture,
  skill_bipolar_strike['name']:skill_bipolar_strike,
  skill_combust['name']:skill_combust,
  skill_power_through['name']:skill_power_through,
  skill_swift_blow['name']:skill_swift_blow,
  skill_bold_strike['name']:skill_bold_strike,
  skill_regenerate['name']:skill_regenerate,
  skill_spin_kick['name']:skill_spin_kick,
  skill_caustic_strike['name']:skill_caustic_strike
 }