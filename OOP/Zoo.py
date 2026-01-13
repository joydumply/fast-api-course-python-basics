class Animal: 
	weight: int
	color: str
	age: int
	animal_type: str

	def eat(self):
		print("Animal eating")

	def sleep(self):
		print('Animal sleeping')


class Dog(Animal):

	def talk(self):
		print('Bark!')

	def eat(self):
		print('Dog is eating!')

class Bird(Animal):
	birdType: str

	def talk(self):
		print('Chirp!')

	def fly(self):
		print('Bird is flying')

bird = Bird()
bird.talk()
bird.fly()