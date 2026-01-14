from Enemy import Enemy


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
