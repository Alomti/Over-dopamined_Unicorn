from datetime import datetime
from Klasy_taskmanager import TaskManager
from Klasy_task import JustTask, WorkTask, HomeTask
def menu(taskmanager):
    print("1. Add task")
    print("2. Remove task")
    print("3. Complete task")
    print("4. Exit")
    if len(taskmanager.tasks) == 0:
        print("No tasks to display.")
    else:
        print("Tasks:")
        taskmanager.show_tasks()
if __name__ == "__main__":
    taskmanager = TaskManager()
    while True:
        menu(taskmanager)
        choice = int(input("Choice an option: \n"))
        if choice == 1:
            task_types = {1: "Just Task", 2: "Work Task", 3: "Home Task"}
            task_type = int(input("Enter task type (1-Just Task, 2-Work Task, 3-Home Task): \n"))
            if task_type not in task_types:
                print("Invalid task type. Please enter a number between 1 and 3.")
                continue
            new_id = len(taskmanager.tasks) + 1
            name = input("Enter task name: \n").capitalize()
            if any(t.name == name for t in taskmanager.tasks):
                print(f"Task with name '{name}' already exists. Please choose a different name.")
                continue
            description = input("Enter task description: \n").capitalize()
            priority = int(input("Enter task priority (1-High, 2-Medium, 3-Low): \n"))
            if priority not in [1, 2, 3]:
                print("Invalid priority. Please enter a number between 1 and 3.")
                continue
            while True:
                deadline = input("Enter task deadline (YYYY-MM-DD HH:MM) or leave blank for no deadline: \n")

                if not deadline:
                    deadline = None
                    break

                try:
                    deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
                    break
                except ValueError:
                    print(f"Invalid format! Use: YYYY-MM-DD HH:MM. Example: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
            if task_type == 1:
                task = JustTask(new_id, name, description, priority, datetime.now(), deadline)
            elif task_type == 2:
                company = input("Enter company name: \n").capitalize()
                task = WorkTask(new_id, name, description, priority, company, datetime.now(), deadline)
            elif task_type == 3:
                room = input("Enter room: \n").capitalize()
                task = HomeTask(new_id, name, description, priority, room, datetime.now(), deadline)
            else:
                print("Invalid task type. Please enter a number between 1 and 3.")
                continue
            taskmanager.add_task(task)
            print("Task added successfully.")
        elif choice == 2:
            id = int(input("Enter task ID: \n"))
            taskmanager.remove_task(id)
            print("Task removed successfully.")
        elif choice == 3:
            id = int(input("Enter task ID: \n"))
            task_found = False
            for t in taskmanager.tasks:
                if t.id == id:
                    if t.status == "InComplete":
                        t.task_completed()
                        print(f"{t}")
                    else:
                        t.task_incomplete()
                        print(f"{t}")
                    task_found = True
            if not task_found:
                print(f"Task with ID '{id}' not found. \n")
        elif choice == 4:
            break
        else:
            print("Invalid option, try again.")