from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
import random

Base = declarative_base()

class Student(Base):
	__tablename__='student' #mapping the table and class
	id=Column(Integer, primary_key=True) #mapping the column and property
	name=Column(String(50))
	credits=Column(Integer)

	'''other methods
	'''

	def __repr__(self):
		return "<Student(name='%s', credits='%s')>" %(self.name,self.credits)

db_link='postgresql://localhost/zhaojichang'
engine = create_engine(db_link)
Session = sessionmaker(bind=engine)
session = Session()
names='abcdefeghigklmnopqrstuvwxyz0123456789!@#$%^&*()'
for i in range(1000):
	name=''.join(random.sample(names,6))
	credits=random.randint(1,100)
	#print(name,credits)
	s=Student(name=name,credits=credits)
	session.add(s)
session.flush()
session.commit()
