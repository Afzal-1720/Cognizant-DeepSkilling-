
CREATE OR REPLACE FUNCTION fn_enroll_student(
    p_student_id INT,
    p_course_id INT,
    p_enrollment_date DATE
)
RETURNS VOID
LANGUAGE plpgsql
AS $$
BEGIN

    -- Check duplicate enrollment
    IF EXISTS (
        SELECT 1
        FROM enrollments
        WHERE student_id = p_student_id
          AND course_id = p_course_id
    ) THEN
        RAISE EXCEPTION
        'Student % is already enrolled in Course %',
        p_student_id,
        p_course_id;
    END IF;

    -- Insert enrollment
    INSERT INTO enrollments(
        student_id,
        course_id,
        enrollment_date
    )
    VALUES(
        p_student_id,
        p_course_id,
        p_enrollment_date
    );

END;
$$;


/* TEST FUNCTION */

SELECT fn_enroll_student(
    2,
    5,
    CURRENT_DATE
);





CREATE TABLE IF NOT EXISTS department_transfer_log
(
    log_id SERIAL PRIMARY KEY,
    student_id INT,
    old_department INT,
    new_department INT,
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE OR REPLACE FUNCTION sp_transfer_student(
    p_student_id INT,
    p_new_department INT
)
RETURNS VOID
LANGUAGE plpgsql
AS $$
DECLARE
    v_old_department INT;
BEGIN

    SELECT department_id
    INTO v_old_department
    FROM students
    WHERE student_id = p_student_id;

    UPDATE students
    SET department_id = p_new_department
    WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log(
        student_id,
        old_department,
        new_department
    )
    VALUES(
        p_student_id,
        v_old_department,
        p_new_department
    );

END;
$$;


/* TEST FUNCTION */

SELECT sp_transfer_student(
    1,
    2
);





BEGIN;

UPDATE students
SET department_id = 2
WHERE student_id = 3;

-- Deliberate error
UPDATE students
SET department_id = 999
WHERE student_id = 4;

COMMIT;


ROLLBACK;





BEGIN;

-- First insert (valid)
INSERT INTO enrollments(
    student_id,
    course_id,
    enrollment_date,
    grade
)
VALUES(
    2,
    5,
    CURRENT_DATE,
    'A'
);

SAVEPOINT sp1;

-- Second insert (invalid FK)
INSERT INTO enrollments(
    student_id,
    course_id,
    enrollment_date,
    grade
)
VALUES(
    2,
    999,
    CURRENT_DATE,
    'A'
);

ROLLBACK TO SAVEPOINT sp1;

COMMIT;




SELECT * FROM enrollments;

SELECT * FROM students;

SELECT * FROM department_transfer_log;