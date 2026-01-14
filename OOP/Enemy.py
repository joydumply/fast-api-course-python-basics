class Enemy: 
	__type_of_enemy: str # Made a private
	hp: int = 10
	ad: int = 1

	def __init__(self, type_of_enemy, hp = 10, ad = 1):
		self.__type_of_enemy = type_of_enemy
		self.hp = hp
		self.ad = ad

	def talk (self):
		print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")
	
	def walk_forward(self):
		print(f'{self.__type_of_enemy} moves closer to you.')
	
	def attack(self):
		print(f'{self.__type_of_enemy} attacks for {self.ad} damage!')

	def get_type_of_enemy(self):
		return self.__type_of_enemy
	
	def print_info(self):
		print(f'Type: {self.__type_of_enemy}\nHP: {self.hp}\nAD: {self.ad}\n')
	