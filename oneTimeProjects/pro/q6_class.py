class Student:
	def __init__(self, name, rno, clsn, ml):
		self.name = name
		self.rollNo = rno
		self.classSection = clsn
		self.setMarks(ml)

	def setMarks(self, marks):
		for x in marks:
			assert x>=0 and x<=100,"Marks should Be B/w 0-100"
		self.marksList = marks

	def computeTotal(self):
		sum=0
		for i in self.marksList:
			sum += i
		return sum

	def __str__(self):
		print(f"Name : {self.name}")
		print(f"Roll No. : {self.rollNo}")
		print(f"Class & Section : {self.classSection}")
		print(f"Marks : {self.marksList}")

S1 = Student("Rajesh", 19, "IX-C", [92,96,83,97,91])
S1._