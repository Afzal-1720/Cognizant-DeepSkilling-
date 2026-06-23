import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="college_db",
    user="postgres",
    password="Afzal@2006"
)

cur = conn.cursor()

cur.execute("""
    SELECT
        e.enrollment_id,
        s.first_name,
        s.last_name
    FROM enrollments e
    JOIN students s
    ON e.student_id=s.student_id
""")

rows = cur.fetchall()

for row in rows:
    print(row)

print("Queries Executed = 1")

cur.close()
conn.close()