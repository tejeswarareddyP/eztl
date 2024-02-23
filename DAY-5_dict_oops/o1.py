#oops
class student:
	def student1(self,name,age,sec):
		self.name=name
		self.age=age
		self.sec=sec
		print(age,sec,name)
	def student2(self,name,age,sec):
		self.name=name
		self.age=age
		self.sec=sec
		print(name,age,sec)
obj=student()
obj.student1("charan","20","ece2")	
obj.student2("charan","20","ece3")	