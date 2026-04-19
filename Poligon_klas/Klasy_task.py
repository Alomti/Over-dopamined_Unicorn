from enum import Enum
from abc import ABC, abstractmethod
from datetime import datetime
class Priority(Enum):
    High = 1
    Medium = 2
    Low = 3

class Task(ABC):
    def __init__(self, id, name, description, priority, creation_time, deadline):
        self.id = id
        self.name = name
        self.description = description
        self.status = "InComplete"
        self.priority = Priority(priority)
        self.creation_time = creation_time
        self.deadline = deadline

    def is_overdue(self):
        if self.status == "Complete":
            return False
        elif self.deadline and datetime.now() > self.deadline:
            return True
        return False

    def task_completed(self):
        self.status = "Complete"

    def task_incomplete(self):
        self.status = "InComplete"

    def __str__(self):
        creation_time = self.creation_time.strftime("%Y-%m-%d %H:%M")
        deadline = self.deadline.strftime("%Y-%m-%d %H:%M") if self.deadline else "-"


        extra = self.extra_info()
        base = f"\n{self.id},\n Task: {self.name},\n Description: {self.description},\n Status: {self.status},\n Priority: {self.priority.name},\n Creation Time: {creation_time},\n Deadline: {deadline}\n"
        if extra:
            return base + "\n" + f"\n{extra}" + "\n"
        return base + "\n"
    @abstractmethod
    def extra_info(self):
        pass

class JustTask(Task):
    def __init__(self, id, name, description, priority, creation_time, deadline):
        super().__init__(id, name, description, priority, creation_time, deadline)
    def extra_info(self):
        return ""

class WorkTask(Task):
    def __init__(self, id, name, description, priority, company, creation_time, deadline):
        super().__init__(id, name, description, priority, creation_time, deadline)
        self.company = company
    
    def change_company(self, new_company):
        self.company = new_company

    def extra_info(self):
        return f"Company: {self.company}"

class HomeTask(Task):
    def __init__(self, id, name, description, priority, room, creation_time, deadline):
        super().__init__(id, name, description, priority, creation_time, deadline)
        self.room = room
    
    def change_room(self, new_room):
        self.room = new_room
    
    def extra_info(self):
        return f"Room: {self.room}"