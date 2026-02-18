import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({'id': task_id, 'description': description, 'done': False})
    save_tasks(tasks)
    print(f"Task '{description}' added with ID {task_id}.")

def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} deleted.")
            return
    print(f"Task {task_id} not found.")

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as done.")
            return
    print(f"Task {task_id} not found.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "[Done]" if task['done'] else "[Pending]"
        print(f"{task['id']}. {task['description']} {status}")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Done")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            desc = input("Enter task description: ")
            add_task(desc)
        elif choice == '2':
            try:
                tid = int(input("Enter task ID to delete: "))
                delete_task(tid)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '3':
            try:
                tid = int(input("Enter task ID to mark as done: "))
                mark_done(tid)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '4':
            list_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()