import os
import sys

class Course:
	'''Course class
	properties: id, name, credits,lecturer 
	methods: print_course, set_credicts
	'''
	ID=0
	def __init__(self,name,credits,lecturer):
		self.id=Course.ID
		self.name=name
		self.credits=credits
		self.lecturer=lecturer
		Course.ID+=1


	def print_course(self):
		print(f"{self.id}\t{self.name}\t{self.credits}\t{self.lecturer}")

class Student:
	def __init__(self,name):
		self.name=name
		self.courses=[]

	def choose_course(self,c:Course):
		self.courses.append(c)

	def total_credits(self):
		total=0.
		for c in self.courses:
			total+=c.credits
		return total

def main():
	cc=Course('c',2,'z')
	cp=Course('python',2,'z')
	cc.print_course()
	cp.print_course()

	s=Student('l')
	s.choose_course(cc)

	print(Course.ID)
	Course.print_course(cc)

if __name__=='__main__':main()
