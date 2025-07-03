🛠️ Apache Airflow 3.0.2 - Common Commands for Data Engineering Workflows

This guide outlines the essential steps and CLI commands to manage Airflow for local development, DAG deployment, and workflow orchestration.


✅ 1. Set Up Environment
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate

# Install Airflow with required extras (example: Postgres, Google)
pip install "apache-airflow[postgres,google]==3.0.2"

🗃️ 2.  Initialize Metadata Database
# Apply schema migrations (creates all necessary tables)
airflow db migrate

⚙️ 3. Create Admin User (First-Time Only)
airflow users create \
  --username admin \
  --firstname FIRSTNAME \
  --lastname LASTNAME \
  --role Admin \
  --email admin@example.com \
  --password admin

📂 4. Place DAGs in the DAGs Folder
# Default DAGs folder (can be customized in airflow.cfg)
~/airflow/dags/

🚀 5. Start Airflow Services
# Start scheduler (processes DAGs & tasks)
airflow scheduler

# In another terminal: start webserver (UI)
airflow webserver --port 8080

📋 6. List and Manage DAGs
# List all available DAGs
airflow dags list

# Trigger a DAG run manually
airflow dags trigger <dag_id>

# Pause/unpause a DAG
airflow dags pause <dag_id>
airflow dags unpause <dag_id>

# Show DAG details
airflow dags show <dag_id>

📊 7. Monitor DAG Runs and Tasks
# List recent DAG runs
airflow dags list-runs -d <dag_id>

# View task logs
airflow tasks logs <dag_id> <task_id> <execution_date>


🧪 8. Test DAGs and Tasks Locally
# Check if DAG file is valid (syntax + import check)
airflow dags parse <path-to-dag-file>

# Test a single task without affecting DB (debug run)
airflow tasks test <dag_id> <task_id> <execution_date>


🔄 9. Reset or Clean Metadata DB (Dangerous Ops)
# Completely wipe DB and start fresh (⚠️ Deletes all history!)
airflow db reset

# Clean old DAG/task logs and metadata
airflow db clean

🔌 10. Additional Utilities
# Start interactive DB shell (SQLAlchemy)
airflow db shell

# Check database health
airflow db check

# View Airflow configuration
airflow config list


🧾 Notes
⚠️ DAGs won't run unless unpaused.

💡 Use environment variables to override configuration:

AIRFLOW_HOME

AIRFLOW__CORE__DAGS_FOLDER

AIRFLOW__DATABASE__SQL_ALCHEMY_CONN

✅ Ensure your DAGs are idempotent and parameterized for repeatable runs.