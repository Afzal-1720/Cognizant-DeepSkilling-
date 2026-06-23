SELECT
    s.first_name || ' ' || s.last_name AS full_name,
    d.dept_name
FROM students s
INNER JOIN departments d
ON s.department_id = d.department_id;

SELECT
    s.first_name || ' ' || s.last_name AS student_name,
    c.course_name,
    e.grade
FROM enrollments e
INNER JOIN students s
ON e.student_id = s.student_id
INNER JOIN courses c
ON e.course_id = c.course_id;

SELECT
    s.student_id,
    s.first_name,
    s.last_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.student_id IS NULL;

SELECT
    c.course_name,
    COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
ORDER BY c.course_name;

SELECT
    d.dept_name,
    p.prof_name,
    p.salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id
ORDER BY d.dept_name;