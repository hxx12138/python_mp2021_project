import psycopg
import random
with psycopg.connect("dbname=zhaojichang") as conn:
	with conn.cursor() as cursor:
		with cursor.copy("COPY test (num, data) FROM STDIN") as copy:
			records=[(random.randint(0,100000),random.randint(0,100000)) for i in range(100000)]
			print(len(records))
			for r in records:
				copy.write_row(r)
print("finished...")