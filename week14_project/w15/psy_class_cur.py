from dataclasses import dataclass
import psycopg
from psycopg.rows import class_row

@dataclass
class Test:
	id: int
	num: int
	data: str

with psycopg.connect("dbname=zhaojichang") as conn:
	with conn.cursor(row_factory=class_row(Test)) as class_cur:
		class_cur.execute('SELECT * FROM test;')
		test=class_cur.fetchone()
		print(test.id)
		print(test.num)
		print(test.data)