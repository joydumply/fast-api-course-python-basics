class Weapon:
	
	def __init__(
		self, 
		type: str = 'Sword', 
		attack_increase: int = 3
	):
		self.type = type
		self.attack_increase = attack_increase