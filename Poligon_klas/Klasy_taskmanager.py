from pathlib import Path
import json
from datetime import datetime
from Klasy_task import JustTask, WorkTask, HomeTask, Priority
plik = Path.cwd() / "Empty_Tasks_folder" / "tasks.json"
plik.parent.mkdir(parents=True, exist_ok=True)
def load_tasks():
    if not plik.exists():
        return []
    with open(plik, "r", encoding="utf-8") as f:
        raw = json.load(f)
        tasks= []
        for d in raw:
            company = d.get("company")
            room = d.get("room")
            if not company and not room:
                t = JustTask(d["id"], d["name"], d["description"], d["priority"], datetime.strptime(d["creation_time"], "%Y-%m-%d %H:%M"), datetime.strptime(d["deadline"], "%Y-%m-%d %H:%M") if d["deadline"] else None)
                t.status = d["status"]
                tasks.append(t)
            elif company:
                t = WorkTask(d["id"], d["name"], d["description"], d["priority"], d["company"], datetime.strptime(d["creation_time"], "%Y-%m-%d %H:%M"), datetime.strptime(d["deadline"], "%Y-%m-%d %H:%M") if d["deadline"] else None)
                t.status = d["status"]
                tasks.append(t)
            elif room:
                t = HomeTask(d["id"], d["name"], d["description"], d["priority"], d["room"], datetime.strptime(d["creation_time"], "%Y-%m-%d %H:%M"), datetime.strptime(d["deadline"], "%Y-%m-%d %H:%M") if d["deadline"] else None)
                t.status = d["status"]
                tasks.append(t)
        return tasks

def save_tasks(tasks):
    with open(plik, "w", encoding="utf-8") as f:
        data = [{"id": t.id, "name": t.name, "description": t.description, "status": t.status, "priority": t.priority.value, "creation_time": t.creation_time.strftime("%Y-%m-%d %H:%M"), "deadline": t.deadline.strftime("%Y-%m-%d %H:%M") if t.deadline else None, "company": getattr(t, 'company', None), "room": getattr(t, 'room', None)} for t in tasks]
        json.dump(data, f, indent=2, ensure_ascii=False)
    
class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()
        self.priority_order = {Priority.High: 1, Priority.Medium: 2, Priority.Low: 3}

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: self.priority_order[x.priority])
        self.reassign_ids()
    
    def reassign_ids(self):
        for i, task in enumerate(self.tasks, start=1):
            task.id = i
        save_tasks(self.tasks)
    
    def change_place(self, new_place):
        for t in self.tasks:
            if type(t) == WorkTask:
                t.change_company(new_place)
            elif type(t) == HomeTask:
                t.change_room(new_place)
        self.sort_tasks()
        self.show_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.sort_tasks()
        save_tasks(self.tasks)
    
    def remove_task(self, task):
        self.tasks = [t for t in self.tasks if t.id != task]
        self.sort_tasks()
        save_tasks(self.tasks)
    
    def show_tasks(self):
        for task in self.tasks:
            print(task)