
#//This will contain general porpuse functions
#// Similar to integer_check, most will likely be error catchers
# This is the item generator now - 10/09/2024

import random

#TODO Allow it to re-generate itens while deleting
#TODO Previous relics and skills from the pool of available itens

def get_random_itens(
  consumable_itens:list,
  relics:list,
  skills:list,
  shop_contents:dict,
  event_itens:dict,
  special_relic_list: dict,
  cursed_relics: list,
  update_pool: bool =False
):
 """
 Generates the itens that appear on shops and events

 consumable_itens: List of all available consumables

 relics: List of all available relics

 skills: list of all available skills

 shop_contents: Dict of the itens to be used in the shop

 event_itens: Dict of the itens to be used in random events

 special_relic_list: Dict containing all the special/unique event relics

 cursed_relics: List containing all the cursed relics

 update_pool (optional): If the current relic and skill pool should be updated or not
 """

 #TODO Include event stuff on the pool update
 if update_pool:

  for relic in shop_contents['shop_relics']:
   del relics[relic['name']]

  for skill in shop_contents['shop_skills']:
   del skills[skill['name']]

  shop_contents.clear()
  event_itens.clear()


 shop_item_1=random.choice(consumable_itens) #// Must be -1 or else it may raise a KeyError

 shop_item_1=consumable_itens[10] #* debug

 while True: # Ensure item won't repeat
  shop_item_2=random.choice(consumable_itens)

  if shop_item_2['name']!=shop_item_1['name']:
   break

 while True:
  shop_item_3=random.choice(consumable_itens)

  if shop_item_1['name']!=shop_item_3['name']!=shop_item_2['name']:
   break


 shop_relic_1=random.choice(list(relics.values()))
 shop_relic_1=relics["Iron Heart"] #*debug

 while True:
  shop_relic_2=random.choice(list(relics.values()))
  if shop_relic_1['name']!=shop_relic_2['name']:
   break

 shop_relic_2=relics["Horseshoe"] #*debug
 #//shop_relic_2=4  # * Debug

 shop_skill_1=random.choice(list(skills.values()))
 shop_skill_1=skills["Spin Kick"] #*debug

 while True:
  shop_skill_2=random.choice(list(skills.values()))

  if shop_skill_1['name']!=shop_skill_2['name']:
   break

 shop_skill_2=skills['Caustic Strike'] #*debug

 while True:
  mini_boss_event=random.choice(list(relics.values()))
  #//mini_boss_event=shop_relic_2 #* debug

  if shop_relic_1['name']!=mini_boss_event['name']!=shop_relic_2['name']:
   break

 while True:
  trader_relic=random.choice(list(relics.values()))

  if shop_relic_1['name']!=trader_relic['name'] and shop_relic_2['name']!=trader_relic['name'] and mini_boss_event['name']!=trader_relic['name']:
   break

 while True:
  trader_skill=random.choice(list(skills.values()))

  if shop_skill_1['name']!=trader_skill['name']!=shop_skill_2['name']:
   break

 event_itens={
  'mini_boss_event_relic':mini_boss_event,
  'midas_chicken_event':special_relic_list['midas_drumstick'],
  'cursed_relic':random.choice(cursed_relics),
  'consumable_trader_item':random.choice(consumable_itens),
  'relic_trader_item':trader_relic,
  'skill_trader_item':trader_skill
 }

 event_itens['cursed_relic']=cursed_relics[7] #*debug

 shop_contents={
  'shop_itens':[shop_item_1,shop_item_2,shop_item_3],
  'shop_relics':[shop_relic_1,shop_relic_2],
  'shop_skills':[shop_skill_1,shop_skill_2]
 }

 return (
  shop_contents,
  event_itens
 )
