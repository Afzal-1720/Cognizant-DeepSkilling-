-- Task 30
SELECT
    c.course_name,
    COUNT(e.student_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

-- Task 31
SELECT
    d.dept_name,
    ROUND(AVG(p.salary), 2) AS avg_salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id
GROUP BY d.department_id, d.dept_name;

-- Task 32
SELECT
    dept_name,
    budget
FROM departments
WHERE budget > 600000;

-- Task 33
SELECT
    grade,
    COUNT(*) AS total_students
FROM enrollments
WHERE course_id = 1
GROUP BY grade;

-- Task 34
SELECT
    d.dept_name,
    COUNT(s.student_id) AS total_students
FROM departments d
JOIN students s
ON d.department_id = s.department_id
GROUP BY d.department_id, d.dept_name
HAVING COUNT(s.student_id) > 2;