class college:
	def __init__(self,n):
		self.n=n
		self.section1()
		self.section2()
	def section1(self):
		print("training sec1:",self.n)
	def section2(self):
		print("training sec2:",self.n)
s=input()
obj=college(s)