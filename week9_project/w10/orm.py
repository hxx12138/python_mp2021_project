class Field:
    def __init__(self, name, column_type):
        self.name=name
        self.column_type=column_type

class StringField(Field):
	def __init__(self,name):
		super().__init__(name,'varchar(256)')

class IntegerField(Field):
	def __init__(self,name):
		super().__init__(name,'int')

def convert_values(a):
	if isinstance(a,str):
		return a
	else:
		return repr(a)

class ModelMetaclass(type):
	def __new__(cls,name,bases,attrs):
		if name=='Model':#基类不处理
			return type.__new__(cls,name,bases,attrs)
		mapping=dict()#只保留Field的子类
		for k,v in attrs.items():
			if isinstance(v,Field):
				mapping[k]=v
		for k in mapping.keys():
			attrs.pop(k)
		attrs['__mappings__']=mapping
		attrs['__table__']=name
		return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError("Model object has no attribute {}".format(key))

	def __setattr__(self,key,value):
		self[key]=value

	def save(self):
		fields=[]
		args=[]
		for k,v in self.__mappings__.items():
			fields.append(v.name)
			args.append(getattr(self, k, None))
		print(args)
		sql="insert into {}({}) values({})".format(\
			self.__table__,','.join(fields),','.join(list(map(convert_values,args))))
		#借助数据库相关的类操作实现
		print('execute: '+sql)

	def delete(self):
		pass

	def update(self):
		pass

class User(Model):
	id=IntegerField('id')
	name=StringField('username')
	email=StringField('email')
	password=StringField('password')

u=User(id=33060828,name='赵吉昌',email='jichang@buaa.edu.cn',password='md5hash',major='cs')
u.save()

