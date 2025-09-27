import os
from datetime import datetime

# ---------------- Classes ----------------
class Task:
    def __init__(self, title, description, due_date, status="Incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.folder = f"projects/{self.name}"
        os.makedirs(self.folder, exist_ok=True)
        self.load_tasks()

    def add_task(self, task):
        # مايزيدش التاسك إلا ماكانش موجود
        if not any(t.title == task.title for t in self.tasks):
            self.tasks.append(task)
            self.save_task(task)

    def delete_task(self, title):
        self.tasks = [t for t in self.tasks if t.title != title]
        file_path = os.path.join(self.folder, f"{title}.txt")
        if os.path.exists(file_path):
            os.remove(file_path)

    def save_task(self, task):
        try:
            with open(os.path.join(self.folder, f"{task.title}.txt"), "w") as f:
                f.write(f"{task.title}\n{task.description}\n{task.due_date}\n{task.status}")
        except Exception as e:
            print("Error saving task:", e)

    def load_tasks(self):
        try:
            for file_name in os.listdir(self.folder):
                path = os.path.join(self.folder, file_name)
                with open(path, "r") as f:
                    lines = f.read().splitlines()
                    if len(lines) == 4:
                        if not any(t.title == lines[0] for t in self.tasks):
                            t = Task(lines[0], lines[1], lines[2], lines[3])
                            self.tasks.append(t)
        except Exception as e:
            pass

    def search_tasks(self, keyword):
        return list(filter(lambda t: keyword.lower() in t.title.lower() or keyword.lower() in t.description.lower(), self.tasks))

class ProjectManager:
    def __init__(self):
        self.projects = []
        os.makedirs("projects", exist_ok=True)
        self.load_projects()

    def add_project(self, project):
        if not any(p.name == project.name for p in self.projects):
            self.projects.append(project)

    def delete_project(self, name):
        self.projects = [p for p in self.projects if p.name != name]
        folder_path = f"projects/{name}"
        if os.path.exists(folder_path):
            for file in os.listdir(folder_path):
                os.remove(os.path.join(folder_path, file))
            os.rmdir(folder_path)

    def load_projects(self):
        for folder in os.listdir("projects"):
            path = os.path.join("projects", folder)
            if os.path.isdir(path):
                if not any(p.name == folder for p in self.projects):
                    self.projects.append(Project(folder))

    def search_projects(self, keyword):
        return list(filter(lambda p: keyword.lower() in p.name.lower(), self.projects))

# ---------------- Example Usage ----------------
if __name__ == "__main__":
    pm = ProjectManager()

    # Add project if not exists
    existing = next((p for p in pm.projects if p.name == "PythonApp"), None)
    if existing:
        p1 = existing
    else:
        p1 = Project("PythonApp")
        pm.add_project(p1)

    # Add tasks (only if not exists)
    p1.add_task(Task("Setup", "Install Python and libraries", "2025-08-25"))
    p1.add_task(Task("Code", "Write core functions", "2025-08-26"))

    # Search example
    print("Search projects for 'Python':", [p.name for p in pm.search_projects("Python")])
    print("Search tasks for 'code':", [t.title for t in p1.search_tasks("code")])

    # Show all tasks in project
    print("\nAll tasks in project:", p1.name)
    for task in p1.tasks:
        print(f"- {task.title} | {task.description} | {task.due_date} | {task.status}")
# ---------------- Classes ----------------
