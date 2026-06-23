EXPLAIN ANALYZE
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
    ON s.student_id = e.student_id
JOIN courses c
    ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

EXPLAIN
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
    ON s.student_id = e.student_id
JOIN courses c
    ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

/*
TASK 48-50 PERFORMANCE ANALYSIS

EXPLAIN ANALYZE was executed on the join query.

Observations:

1. PostgreSQL performed a Sequential Scan
   on the enrollments table.

2. PostgreSQL performed a Sequential Scan
   on the students table.

3. The filter condition
   (enrollment_year = 2022)
   removed 7 rows and returned 3 rows.

4. PostgreSQL used a Hash Join to join
   students and enrollments.

5. PostgreSQL used an Index Scan on
   courses because course_id is a PRIMARY KEY.

6. Execution Time = 0.310 ms.

Conclusion:
At least one Sequential Scan exists,
which establishes the baseline before
adding indexes.
*/