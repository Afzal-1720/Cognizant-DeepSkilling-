#C:\Users\fmdaf\Documents\Cognizant Deepskilling 2027\Week 1\Module 3 - Database\Advanced>alembic revision --autogenerate -m "initial schema"
#INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
#INFO  [alembic.runtime.migration] Will assume transactional DDL.
#INFO  [alembic.ddl.postgresql] Detected sequence named 'professors_professor_id_seq' as owned by integer column 'professors(professor_id)', assuming SERIAL and omitting
#INFO  [alembic.ddl.postgresql] Detected sequence named 'courses_course_id_seq' as owned by integer column 'courses(course_id)', assuming SERIAL and omitting
#INFO  [alembic.ddl.postgresql] Detected sequence named 'enrollments_enrollment_id_seq' as owned by integer column 'enrollments(enrollment_id)', assuming SERIAL and omitting
#Generating C:\Users\fmdaf\Documents\Cognizant Deepskilling 2027\Week 1\Module 3 - Database\Advanced\migrations\versions\efd77d508819_initial_schema.py ...  done

#C:\Users\fmdaf\Documents\Cognizant Deepskilling 2027\Week 1\Module 3 - Database\Advanced>alembic upgrade head
#INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
#INFO  [alembic.runtime.migration] Will assume transactional DDL.
#INFO  [alembic.runtime.migration] Running upgrade  -> efd77d508819, initial schema


/*
=========================================================
            ALEMBIC COMMANDS CHEAT SHEET
=========================================================

1. Install Alembic
---------------------------------------------------------
pip install alembic


2. Check Alembic Version
---------------------------------------------------------
alembic --version


3. Initialize Alembic in the Project
---------------------------------------------------------
alembic init migrations

Creates:
    alembic.ini
    migrations/
        env.py
        script.py.mako
        versions/


4. Configure Database Connection
---------------------------------------------------------
Edit alembic.ini

sqlalchemy.url =
postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost/college_db_orm


5. Configure Metadata
---------------------------------------------------------
Edit migrations/env.py

from models import Base

target_metadata = Base.metadata


6. Generate Initial Migration
---------------------------------------------------------
alembic revision --autogenerate -m "initial schema"

Purpose:
    Compare SQLAlchemy models with the database
    Generate migration file automatically


7. Apply Latest Migration
---------------------------------------------------------
alembic upgrade head

Purpose:
    Execute upgrade() function
    Apply all pending migrations
    Create alembic_version table


8. View Current Migration Version
---------------------------------------------------------
alembic current

Shows currently applied revision.


9. View Migration History
---------------------------------------------------------
alembic history

Shows all migrations.


10. Downgrade One Migration
---------------------------------------------------------
alembic downgrade -1

Roll back one migration.


11. Downgrade to Base
---------------------------------------------------------
alembic downgrade base

Roll back all migrations.


12. Upgrade to Specific Revision
---------------------------------------------------------
alembic upgrade <revision_id>

Example:
alembic upgrade 5e1d455590bb


13. Stamp Database (Without Running Migration)
---------------------------------------------------------
alembic stamp head

Marks current revision as applied without executing SQL.


14. Create a New Migration After Model Changes
---------------------------------------------------------
alembic revision --autogenerate -m "add phone_number"

Example:
Added phone_number column in Student model.


15. Apply Newly Generated Migration
---------------------------------------------------------
alembic upgrade head


=========================================================
Useful PostgreSQL Verification Commands
=========================================================

-- Check migration version
SELECT * FROM alembic_version;

-- Show all tables
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

=========================================================
Workflow
=========================================================

1. pip install alembic

2. alembic init migrations

3. Configure alembic.ini

4. Configure env.py

5. alembic revision --autogenerate -m "initial schema"

6. alembic upgrade head

7. alembic current

8. Verify using:
   SELECT * FROM alembic_version;

