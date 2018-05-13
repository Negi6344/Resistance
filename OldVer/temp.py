class test:
	def __init__(self, temp):
		self.temp = temp

	def checker(self, listA):
		if self in listA:
			print("LOL")
		else:
			print("Poop")

	def rem(self,listA):
		listA.remove(self)
		if self in listA:
			print("LOL")
		else:
			print("Poop")

A = test(1)
B = [A, test(2), test(3), test(4)]
A.checker(B)
A.rem(B)