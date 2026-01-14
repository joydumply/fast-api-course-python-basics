from Enemy import Enemy 
from Zombie import Zombie
from Ogre import Ogre

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


zombie = Zombie(hp = 15, ad = 3) # made a stronger zombie
ogre = Ogre(20, 3)

zombie.print_info()
ogre.print_info()

battle(zombie, ogre)