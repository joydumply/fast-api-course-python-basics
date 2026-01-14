from Enemy import * 
from Zombie import Zombie
from Ogre import Ogre

zombie = Zombie(hp = 15, ad = 3) # made a stronger zombie
ogre = Ogre(20, 3)

zombie.print_info()
ogre.print_info()

zombie.talk()

ogre.talk()