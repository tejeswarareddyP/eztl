#training
class training:
	def __init__(self,l):
		self.l=l
	def section1(self):
		print("training sec1:",self.l)
	def section2(self):
		print("training sec2:",self.l)
obj=training("python")
obj.section1()
obj.section2()