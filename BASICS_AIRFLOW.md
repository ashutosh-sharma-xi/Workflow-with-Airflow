# Apache Airflow Learning Documentation

A workflow-as-code platform for batch processing tasks in data engineering. Also known as a **workflow orchestrator**.

---

## 📁 1. DAGs (Directed Acyclic Graphs)

* Workflows are defined in Python as DAGs—graphs of **Tasks** connected by dependencies.
* Each DAG outlines the execution order (e.g., Task A → Task B → Task C).
* Stored in the `dags/` folder with `.py` extension ([airflow.apache.org][1]).

---

## 🛠️ 2. Tasks & Operators

### Core Concepts
* **Tasks** are individual units of work in a DAG.
* Defined using **Operators** (pre-built/custom) that determine what gets executed.

### Common Operators
| Operator | Purpose |
|----------|---------|
| `BashOperator` | Executes bash commands |
| `PythonOperator` | Runs Python functions |
| `EmailOperator` | Sends emails |
| `SimpleHttpOperator` | Makes HTTP requests |

* Custom operators can be built by extending `BaseOperator` ([medium.com][2], [docs.arenadata.io][3]).

---

## 👁️ 3. Sensors (Specialized Operators)
* Wait for specific conditions before proceeding.
* Available in `airflow.sensors` and `airflow.providers.*.sensors`.

### Modes of Operation:
1. **Poke** (default): Continuously checks (occupies worker slot)
2. **Reschedule**: Checks intermittently (frees worker between checks)

### Example Sensors:
| Sensor | Purpose |
|--------|---------|
| `FileSensor` | Waits for file existence |
| `ExternalTaskSensor` | Waits for another DAG's task |
| `HttpSensor` | Checks web endpoint |
| `SqlSensor` | Monitors database conditions |

---

## ⚙️ 4. Executors
Determine how and where tasks are executed. Configured via `airflow.cfg` or `airflow info`.

### Types:
| Executor | Characteristics | Use Case |
|----------|-----------------|----------|
| `SequentialExecutor` | Single-task execution | Debugging |
| `LocalExecutor` | Parallel on single machine | Development |
| `CeleryExecutor` | Distributed across workers | Production |
| `KubernetesExecutor` | Dynamic pod creation | Scalable workloads |

---

## 🗓️ 5. Scheduler
* Continuously scans DAG files to:
  - Determine due tasks
  - Check dependency satisfaction
  - Enqueue ready tasks via Executor ([deepwiki.com][4], [reddit.com][5])

---

## 🧑‍💻 6. Worker(s)
* Execute assigned tasks in:
  - Separate processes (`LocalExecutor`)
  - Different machines (`CeleryExecutor`)
  - Kubernetes pods (`KubernetesExecutor`) ([reddit.com][7], [airflow.apache.org][1])

---

## 🗃️ 7. Metadata Database
Stores workflow state in relational DBs (Postgres/MySQL recommended):

| Data Type | Examples |
|-----------|----------|
| DAG Definitions | Schedule intervals, task graphs |
| Runtime Metadata | Task instances, execution dates |
| Historical Data | Run durations, success/failure logs |

---

## 🌐 8. Web Server (UI)
Flask-based interface providing:

| Feature | Description |
|---------|-------------|
| DAG Visualization | Graph/Tree views of workflows |
| Run Management | Manual triggers, task retries |
| Monitoring | SLA misses, audit logs |
| Debugging | Task logs, rendered templates |

---

## 🛠️ Optional Components
* **Triggerer**: Handles deferred tasks via asyncio (for sensors/deferrable operators)
* **Plugins**: Extend functionality via custom operators/hooks/UI components
* **XComs**: Cross-task communication mechanism
* **Pools**: Limit concurrent task execution

---

## ⏳ Core Workflow
1. **Author**: Write DAGs in Python (`dags/` folder)
2. **Schedule**: Scheduler parses DAGs and creates DagRuns
3. **Execute**: Executor assigns tasks to Workers
4. **Monitor**: Web UI displays real-time status
5. **Track**: Metadata DB records all execution details

---

## 🔍 Debugging Guide

### Common Issues & Solutions:

| Problem | Diagnostic Steps | Solutions |
|---------|------------------|-----------|
| DAG not running on schedule | 1. Check scheduler logs<br>2. Verify `start_date`/`schedule_interval` | 1. Adjust executor resources<br>2. Modify scheduling parameters |
| DAG not loading | 1. Run `airflow dags list-import-errors`<br>2. Check absolute path in `airflow.cfg` | 1. Fix Python syntax errors<br>2. Verify DAG folder location |
| Task failures | 1. Examine task logs<br>2. Test with `airflow tasks test` | 1. Add error handling<br>2. Check dependencies |

---

## 📈 SLA & Reporting

### Service Level Agreements
```python
task = PythonOperator(
    task_id='process_data',
    python_callable=process,
    sla=timedelta(minutes=30)  # Max allowed runtime
)

## 📈 SLA & Reporting

### Service Level Agreements
* View misses: **Browse → SLA Misses** in UI

### Reporting Options
1. Email notifications (using `EmailOperator`)
2. Webhook callbacks
3. Integration with monitoring tools (Prometheus, Datadog)

---

## 🎨 Advanced Features

### Templating
Uses Jinja2 syntax for dynamic values:
```python
BashOperator(
    task_id='render_template',
    bash_command='echo {{ ds }}'  # Execution date
)

## Branching
Control flow with BranchPythonOperator:
```python
def decide_path(**context):
    return 'task_a' if condition else 'task_b'

## Production Commands
```bash
# Single task test
airflow tasks test my_dag transform_data 2024-01-01
# Full DAG run
airflow dags trigger -e 2024-01-01 my_dag

|💡 Key Advantages|
|Feature |	Benefit|
|Python-native|	Dynamic workflow generation|
|Extensible|	Custom operators/hooks/plugins|
|Scalable|	Multiple executor options|
|Observable|	Rich UI and logging|
