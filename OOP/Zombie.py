from Enemy import Enemy
import random

class Zombie(Enemy):
	def __init__(self, hp, ad ):
		super().__init__(
			type_of_enemy = 'Zombie', 
			hp = hp, 
			ad = ad
		)
	
	def talk(self):
		print('*Grumbling...*')

	def spread_infection(self):
		print('Zombie spreading infection!')

	def special_attack(self):
		did_special_attack_work = random.random() < 0.50
		
		if did_special_attack_work:
			self.hp += 2
			print(f'{self.get_type_of_enemy()} regenerated 2 HP!')
