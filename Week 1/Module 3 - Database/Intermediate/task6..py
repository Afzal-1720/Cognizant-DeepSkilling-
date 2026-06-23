import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="college_db",
    user="postgres",
    password="Afzal@2006"
)

cur = conn.cursor()

query_count = 0

# Query 1
cur.execute("""
    SELECT enrollment_id, student_id
    FROM enrollments
""")

query_count += 1

enrollments = cur.fetchall()

for enrollment in enrollments:

    student_id = enrollment[1]

    cur.execute("""
        SELECT first_name,last_name
        FROM students
        WHERE student_id=%s
    """,(student_id,))

    query_count += 1

    student = cur.fetchone()

    print(
        enrollment[0],
        student[0],
        student[1]
    )

print("Queries Executed =", query_count)

cur.close()
conn.close()