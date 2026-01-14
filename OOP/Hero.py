from Weapon import Weapon

class Hero:
	def __init__(self, hp, ad):
		self.hp = hp
		self.ad = ad
		self.is_weapon_equipped = False
		self.weapon: Weapon = None

	def equip_weapon(self, weapon):
		if weapon is not None and not self.is_weapon_equipped:
			self.weapon = weapon
			self.ad += self.weapon.attack_increase
			self.is_weapon_equipped = True
			print(f'Hero equips the {weapon.type} and increase his damage by {weapon.attack_increase}')

	def attack(self):
		print(f"Hero attacks with {self.ad} damage!")

	def print_hp_left(self):
		print(f'Hero has {self.hp} HP left.') 