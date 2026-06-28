# Modify Student model

# Generate migration
alembic revision --autogenerate -m "add is_active to students"

# Apply migration
alembic upgrade head

# Add CourseSchedule model

# Generate migration
alembic revision --autogenerate -m "add course schedules"

# Apply migration
alembic upgrade head

# Show migration history
alembic history --verbose

# Check current applied revision
alembic current