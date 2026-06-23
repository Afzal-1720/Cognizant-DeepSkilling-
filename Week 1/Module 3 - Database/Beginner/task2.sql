-- 1NF Analysis
-- All tables store atomic values only.
-- No column contains multiple values or repeating groups.
-- Therefore the schema satisfies 1NF.

-- 2NF Analysis
-- All tables are in 1NF.
-- In enrollments, enrollment_date and grade depend on the complete enrollment record.
-- No partial dependency exists.
-- Therefore the schema satisfies 2NF.

-- 3NF Analysis
-- No non-key attribute depends on another non-key attribute.
-- Department details are stored in the departments table and referenced through foreign keys.
-- No transitive dependency exists.
-- Therefore the schema satisfies 3NF.