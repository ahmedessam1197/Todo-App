from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import os
import logging

# Logging Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "dev-secret")

# Database Environment Variables
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = os.environ.get('DB_DATABASE')

# Validate environment variables
if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE]):
    raise ValueError("Database environment variables are not set properly")

# Database Connection
params = quote_plus(
    f"DRIVER=ODBC Driver 17 for SQL Server;"
    f"SERVER={DB_HOST};"
    f"DATABASE={DB_DATABASE};"
    f"UID={DB_USER};"
    f"PWD={DB_PASSWORD}"
)

connection_string = f"mssql+pyodbc:///?odbc_connect={params}"

db_connection = create_engine(
    connection_string,
    pool_pre_ping=True,
    pool_recycle=1433
)
# Routes
@app.route('/')
def index():
    try:
        with db_connection.connect() as conn:
            result = conn.execute(text("SELECT * FROM tasks"))
            tasks = result.fetchall()
    except Exception as e:
        logger.error(f"Error loading tasks: {e}")
        tasks = []

    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')

    if title:
        try:
            with db_connection.begin() as conn:
                conn.execute(
                    text("INSERT INTO tasks (title, description) VALUES (:title, :description)"),
                    {"title": title, "description": description}
                )
            logger.info("Task added successfully")
        except Exception as e:
            logger.error(f"Error adding task: {e}")

    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    try:
        with db_connection.begin() as conn:
            conn.execute(
                text("DELETE FROM tasks WHERE id = :id"),
                {"id": task_id}
            )
        logger.info(f"Task {task_id} deleted")
    except Exception as e:
        logger.error(f"Error deleting task: {e}")

    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    try:
        with db_connection.begin() as conn:
            conn.execute(
                text("UPDATE tasks SET is_complete = 1 WHERE id = :id"),
                {"id": task_id}
            )
        logger.info(f"Task {task_id} completed")
    except Exception as e:
        logger.error(f"Error completing task: {e}")

    return redirect(url_for('index'))

# Health Check (for Docker/K8s)
@app.route('/health')
def health():
    return {"status": "ok"}, 200

# Run App (local only)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)