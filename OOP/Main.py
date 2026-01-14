from Enemy import Enemy 
from Zombie import Zombie
from Ogre import Ogre
from Hero import Hero
from Weapon import Weapon

def battle(e1: Enemy, e2: Enemy):
	e1.talk()
	e2.talk()

	while e1.hp > 0 and e2.hp > 0:
		print('------------')
		e1.special_attack()
		e2.special_attack()

		e2.attack()
		e1.hp -= e2.ad

		e1.attack()
		e2.hp -= e1.ad

		e1.print_hp_left()
		e2.print_hp_left()

		if e1.hp > 0:
			print(f'{e1.get_type_of_enemy()} wins')
		else:
			print(f'{e2.get_type_of_enemy()} wins')

def hero_battle(h: Hero, e: Enemy):

	while h.hp > 0 and e.hp > 0:
		print('------------')
		e.special_attack()

		e.attack()
		h.hp -= e.ad
		
		h.attack()
		e.hp -= h.ad

		h.print_hp_left()
		e.print_hp_left()

		if e.hp <= 0:
			print('Hero wins')

		elif h.hp <= 0:
			print(f'{e.get_type_of_enemy()} wins')



zombie = Zombie(hp = 15, ad = 3) # made a stronger zombie
ogre = Ogre(20, 3)
hero = Hero(10, 1)
weapon = Weapon('Sword', 5)
zombie.print_info()

hero.equip_weapon(weapon)



hero_battle(hero, ogre)