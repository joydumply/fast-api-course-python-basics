from Enemy import Enemy
import random
class Ogre(Enemy):

	def __init__(self, hp, ad):
		super().__init__(
					type_of_enemy = 'Ogre',
					hp = hp,
					ad = ad
				)
		
	def talk(self):
		print('Ogre is slamming his hands all around')

	def special_attack(self):
		did_special_attack_work = random.random() < 0.20
		
		if did_special_attack_work:
			self.ad += 4
			print(f'{self.get_type_of_enemy()} gets angry and increases his attack by 4')