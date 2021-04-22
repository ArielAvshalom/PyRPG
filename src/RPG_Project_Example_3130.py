# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 09:30:54 2021
Limitiations: Written in an hour and 20 minutes
@author: Ariel
"""
import random as r
import pprint as p

class player:
    def __init__(self, name : str, nature : str, bag, health, experience, level : int, money, attack_list, stats) -> None:
        self.name = name
        self.nature = nature
        self.bag = bag
        self.health = health
        self.experience = experience
        self.level = level
        self.money = money
        
        self.attack_list = attack_list
        self.stats = stats
    
    def __repr__(self):
        return f"The player's name is {self.name}.\nThe player's nature is {self.nature}.\nhis current health is {self.health.current} out of {self.health.limit}.\nThe player's level is over 9000!@O!@!@ (JK, it's {self.level})\n\nThe player has {self.money} crembos."
    
    def level_up(self):
        #after each time the player gets experience, calculate the experience and if the experience is over 100%, then reduce it to itself - 100 and then level up the character
        if self.experience.current >  self.experience.limit:
            print("level up! You are now level ", self.level + 1)    
            self.level += 1
    
    def use_item(self):
        pass

class monster:
    def __init__(self, name, nature, health, drops, money, attack_list):
        self.name = name
        self.nature = nature
        self.health = health
        self.drops = drops
        self.money = money
        self.attack_list = attack_list
    
    def __repr__(self):
        return f"The monster's name is {self.name}, the monster's nature is {self.nature}, the monster's health is {self.health.current} out of {self.health.limit} and the monster's drops are {self.drops}. The monster will give you {self.money} upon defeat."

class items:
    def __init__(self, item_dict):
        self.item_dict = item_dict
    
    def add_item_to_dict(self, item_name, item_effect, item_power = None, item_nature = None):
        pass

    class item:
        def __init__(self, name, kind_of_item):
            self.name = name
            self.kind_of_item = kind_of_item #is it key to the plot, or a disposable or a weapon etc?
        
        def __repr__(self):
            return f'{self.name} is a {self.kind_of_item} type of item.'
        
    class healing(item):
        def __init__(self, name, effect, power, kind_of_item):
            super.__init__(self, name, kind_of_item)
            self.effect = effect
            self.power = power
            
        def describe(self):
            return f'{self.name} is a {self.kind_of_item} which has a {self.effect} effect and it\'s base {self.effect} power is {self.power}'
    
    class damage(item):
        def __init__(self, name, effect, power, nature, kind_of_item):
            super.__init__(self, name, kind_of_item)
            self.effect = effect
            self.power = power
            self.nature = nature
    
        def describe(self):
            return f'{self.name} is a {self.kind_of_item} which has a {self.effect} effect and it\'s base {self.effect} power is {self.power}. The nature of this item is {self.nature}.'
    
    class armor(item):
        def __init__(self, name, armor_type, armor_effect, armor_abilities):
            #not using super will override item's methods
            self.name = name
            self.armor_type = armor_type
            self.armor_effect = armor_effect
            self.armor_abilities = armor_abilities
            
    class weapon(item):
        pass
    
    class pants(armor):
        #you can inherit from multiple classes with Python.
        pass
    
    class shirt(armor):
        pass
    
    class shoes(armor):
        pass
    
    class helm(armor):
        pass
    
    class sword(weapon):
        pass
    
    class wand(weapon):
        pass
    
    class bow(weapon):
        pass
    
    class arrow(weapon):
        pass
            

class attack:
    def __init__(self, name, power, nature, accuracy, effect, effect_chance):
        self.name = name
        self.power = power
        self.nature = nature
        self.accuracy = accuracy
        self.effect = effect
        self.effect_chance = effect_chance
        
    # def attack_success(self) -> bool:
    #     chance = r.uniform(0, 1)
    #     if chance
    
class environment:
    pass
    
class bag:
    def __init__(self, item_list):
        self.item_list = item_list
class bar:
    def __init__(self, current, limit):
        self.current = current
        self.limit = limit
    #This means that you have an amount of something and a limit for how much you can have of it.
    #you have x/100 experience
    #you have 75 out 387 health
    

def battle(player, monster):
    while player.health.current > 0 and monster.health.current > 0:
        print("player's attack options are:")
        p.pprint(player.attack_list, width = 30)
        
        
        
        attack_choice = input("What is your attack?\n")
        
        while True:
            if attack_choice in player.attack_list:
                break
            else:
                p.pprint(player.attack_list, width = 30)
                input("invalid attack choose again\n")
                
        
        attack_power = player.attack_list[attack_choice]
        
        monster.health.current -= attack_power
        
        print(f"The attack was a success. {player.name} used {attack_choice}.\nThe monster's health was {monster.health.current+attack_power}, now it is {monster.health.current}")
        
        monster_attacks = list(monster.attack_list.keys())
        monster_length_attack_choices =len(list(monster.attack_list.keys()))
        
        monster_attack_choice = monster_attacks[r.randint(0, monster_length_attack_choices-1)]
        
        print(f"The monster attacked with {monster_attack_choice}. It did {monster.attack_list[monster_attack_choice]} damage. The player's health is now {player.health.current-monster.attack_list[monster_attack_choice]}")
        
        player.health.current-=monster.attack_list[monster_attack_choice]
        
        
        
    if player.health.current <= 0:
        return "you lost game over"
    if monster.health.current <= 0:
        return "you won"




if __name__ == "__main__":

    slash = attack("Sword Slash", 70)
    ram = attack("Shoulder Ram", 90)    
    erupt = attack("Eruption", 120)
    snore = attack("Snore", 10)
    
    
    Ham_bag = bag(['generic light saber', 'subtle knife', 'potion', 'some really snazzy quest item'])
    Ham_health = bar(250, 250)
    Ham_exp = bar(0, 100)
    Hamil = player("Alexander Hamilton", "Light", Ham_bag, Ham_health, Ham_exp, 0, 0, {slash.name : slash.power, ram.name : ram.power})
    
    Cam_health = bar(175, 175)
    
    Cam = monster("CamelEruption", "Fire", Cam_health, ["potion, fire gem"], 1.68271, {erupt.name: erupt.power, snore.name : snore.power})
    
    #test battle, still a lot of issues but it should work for a basic battle:
    battle(Hamil, Cam)
