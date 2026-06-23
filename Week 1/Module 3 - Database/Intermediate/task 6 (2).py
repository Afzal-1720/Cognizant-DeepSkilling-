import time

start = time.time()

# JOIN code

end = time.time()

print(
    "Time:",
    end-start
)

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