# Current Version
alembic current

# Rollback One Step
alembic downgrade -1

# Rollback Completely
alembic downgrade base

# Apply All Migrations Again
alembic upgrade head

# View History
alembic history --verbose

# Install Alembic
pip install alembic

# Initialize
alembic init migrations

# Create Initial Migration
alembic revision --autogenerate -m "initial schema"

# Apply Migration
alembic upgrade head

# Check Version
alembic current

# Add New Column
alembic revision --autogenerate -m "add is_active to students"

# Apply Migration
alembic upgrade head

# Add New Table
alembic revision --autogenerate -m "add course schedules"

# Apply Migration
alembic upgrade head

# View History
alembic history --verbose

# Rollback One Revision
alembic downgrade -1

# Rollback All Revisions
alembic downgrade base

# Reapply All Migrations
alembic upgrade head