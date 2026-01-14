from Enemy import * 
from Zombie import Zombie
from Ogre import Ogre

def battle(e: Enemy):
	e.talk()
	e.attack()

zombie = Zombie(hp = 15, ad = 3) # made a stronger zombie
ogre = Ogre(20, 3)

zombie.print_info()
ogre.print_info()

battle(zombie)
battle(ogre)