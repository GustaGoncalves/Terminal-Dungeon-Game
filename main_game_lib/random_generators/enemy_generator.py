import random

#TODO Allow it to re-generate new enemies and minibosses

def get_random_enemies(
  enemies:list,
  minibosses:list,
  enemies_to_be_fought:dict,
  #//basic_item_list: list
):
 """
 Generates the enemies that will be used in the events and combat

 enemies: List containing all normal enemies

 minibosses: List containing all minibosses

 enemies_to_be_fought: The holds the enemies the generated enemies

 basic_item_list: List containing all game consumable items

 return: Returns the dict containing generated enemies
 """

 enemies_to_be_fought.clear()

 enemies_to_be_fought['normal_enemy']=random.choice(enemies)

 enemies_to_be_fought['normal_enemy']=enemies[0] #* debug

 enemies_to_be_fought['miniboss']=random.choice(minibosses)

 enemies_to_be_fought['miniboss']=minibosses[1]

 #//if enemies_to_be_fought['miniboss']['steal_class']=='ITEM':
  #//enemies_to_be_fought['miniboss']['item_stolen']=basic_item_list[enemies_to_be_fought['miniboss']['item_to_pull']].copy()

 return(
  enemies_to_be_fought
 )