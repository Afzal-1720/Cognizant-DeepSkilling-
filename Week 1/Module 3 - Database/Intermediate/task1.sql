-- Task 35
SELECT
    s.student_id,
    s.first_name,
    s.last_name
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT student_id,
               COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) t
);


SELECT
    c.course_id,
    c.course_name
FROM courses c
WHERE NOT EXISTS
(
    SELECT *
    FROM enrollments e
    WHERE e.course_id = c.course_id
      AND e.grade <> 'A'
);


SELECT
    p.prof_name,
    p.salary,
    p.department_id
FROM professors p
WHERE p.salary =
(
    SELECT MAX(p2.salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);

SELECT
    d.dept_name,
    dept_avg.avg_salary
FROM
(
    SELECT
        department_id,
        AVG(salary) AS avg_salary
    FROM professors
    GROUP BY department_id
) dept_avg
JOIN departments d
ON dept_avg.department_id = d.department_id
WHERE dept_avg.avg_salary > 85000;