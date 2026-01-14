from Enemy import Enemy

class Ogre(Enemy):

	def __init__(self, hp, ad):
		super().__init__(
					type_of_enemy = 'Ogre',
					hp = hp,
					ad = ad
				)
		
	def talk(self):
		print('Ogre is slamming his hands all around')