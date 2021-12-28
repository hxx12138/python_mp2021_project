import psycopg
#AsyncConnection.connect() creates an asyncio connection instead
with psycopg.connect("dbname=zhaojichang") as conn:
	with conn.cursor() as cur:
		cur.execute("SELECT * FROM test;")
		for record in cur:
			print(record)
		conn.commit()