import psycopg
from psycopg.rows import dict_row

with psycopg.connect("dbname=zhaojichang") as conn:
	with conn.cursor(row_factory=dict_row) as dict_cur:
		dict_cur.execute('SELECT * FROM test;')
		res=dict_cur.fetchone()
		print(res['id'])
		print(res['data'])