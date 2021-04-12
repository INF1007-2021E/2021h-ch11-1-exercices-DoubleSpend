"""
Chapitre 11.1

Classes pour représenter un personnage.
"""

import time
import random

import utils


class Weapon:
	def __init__(self,name,damage,level, speed):
		self.name = name
		self.damage = damage
		self.level = level
		self.speed = speed
arm = Weapon("Arming Sword",21,13,20)
messer = Weapon("Messer", 31, 13, 10)
fists = Weapon("Fists", 14, 0, 15)



class Character:
	def __init__(self, name, max_hp, attack, defense, level, weapon,hp_left,skill):
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = weapon
		self.hp_left = hp_left
		self.skill = skill
morning = Character("Morning",100,100,200,200,arm,100,20)
ren = Character("Ren",100,100,120,200,messer,100,19)


def deal_damage(attacker, defender):
	if random.randint(1,16) == 16:
		crit = 1.5
	else:
		crit =1
	rng = (random.randint(85,100))/100
	modifier = crit * rng
	if random.randint(10,25) < defender.skill:
		damage = 0
		print(defender.name+" parries "+attacker.name+" and ripostes!")
		print("\n")
	else:
		damage = int(((((2*attacker.level/5)+2)*attacker.weapon.damage*(attacker.attack/defender.defense))/50)+2)*modifier
		print(attacker.name + " dealt " + str(int(damage)) + " damage with " + str(attacker.weapon.name))
		print("\t"+defender.name+" has "+str(int(defender.hp_left-damage))+" HP left.")
		print("\n")
	defender.hp_left -= damage
	return defender.hp_left, damage

def run_battle(c1, c2):
	print("Ronguat: I am not biased towards Ren at all. Let's start this duel! \n")
	c=0
	if random.randint(1,2) ==1:
		while c1.hp_left >=0:
			if c2.hp_left >= 0:
				deal_damage(c1,c2)
				deal_damage(c2,c1)
				c+=1
				time.sleep(1)
				if c1.hp_left <= 0:
					print(c1.name + " died in " + str(c) + " turns")
					break
				elif c2.hp_left <= 0:
					print(c2.name + " died in " + str(c) + " turns")
					break
	else:
		while c1.hp_left > 0 or c2.hp_left > 0:
			if c2.hp_left >= 0:
				deal_damage(c2,c1)
				deal_damage(c1,c2)
				c+=1
				time.sleep(5)
				if c1.hp_left <= 0:
					print(c1.name + " died in " + str(c) + " turns")
					break
				elif c2.hp_left <= 0:
					print(c2.name + " died in " + str(c) + " turns")
					break

if __name__ == "__main__":
	run_battle(ren,morning)