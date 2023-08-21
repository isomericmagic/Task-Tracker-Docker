import uuid
from flask import Blueprint, current_app, render_template, request, redirect, url_for

pages = Blueprint("tasks", __name__, template_folder="templates", static_folder="static")

@pages.route("/")
def task():
    current_tasks = current_app.db.tasks.find()

    completions = [
        task["task"]
        for task in current_app.db.completions.find()
    ]

    return render_template("index.html", tasks=current_tasks, title="Task Tracker - Home", completions=completions)

@pages.route("/add", methods=["GET", "POST"])
def add_task():
    if request.form:
        current_app.db.tasks.insert_one(
            {"_id": uuid.uuid4().hex, "name": request.form.get("task")}
        )
    return render_template("add_task.html", title="Task Tracker - Add Item")

@pages.route("/complete", methods=["POST"])
def complete():
    task = request.form.get("taskId")
    current_app.db.completions.insert_one({"task": task})

    return redirect(url_for(".task"))