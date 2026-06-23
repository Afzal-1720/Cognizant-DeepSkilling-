import psycopg2
import time

start = time.time()

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
end = time.time()

print(
    "Time:",
    end-start
)

cur.close()
conn.close()

"""
N+1 ANALYSIS

N+1 occurs when an application first
loads N rows and then executes one
additional query per row to fetch
related data.

Example:

1 query to fetch enrollments
+
10 queries to fetch student names

=
11 total queries.

For 10,000 enrollments:

1 + 10,000
=
10,001 queries.

The JOIN approach retrieves all
required data in a single query,
reducing database round-trips and
improving performance.

This issue is commonly seen in ORM
frameworks such as Hibernate when
lazy loading is used.
"""