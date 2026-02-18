# To-Do List Application

A simple command-line to-do list application built in Python. Users can add, delete, mark tasks as done, and list all tasks. Tasks are stored in a JSON file for persistence.

## Features

- Add new tasks
- Delete existing tasks
- Mark tasks as completed
- List all tasks with their status
- Basic error handling (e.g., invalid task IDs, non-existent tasks)
- Persistent storage using JSON format

## Requirements

- Python 3.x (uses only standard library modules: `json` and `os`)

## Installation

1. Clone or download the repository.
2. Ensure Python 3.x is installed on your system.

## Usage

Run the application from the command line:

```bash
python todo_app.py
```

The application will display a menu with the following options:

1. **Add Task**: Enter a task description to add a new task.
2. **Delete Task**: Enter the task ID to delete a task.
3. **Mark Task as Done**: Enter the task ID to mark a task as completed.
4. **List Tasks**: Display all tasks with their IDs, descriptions, and status ([Done] or [Pending]).
5. **Exit**: Quit the application.

Tasks are automatically saved to `tasks.json` in the same directory.

## Example

```
To-Do List Application
1. Add Task
2. Delete Task
3. Mark Task as Done
4. List Tasks
5. Exit
Choose an option: 1
Enter task description: Buy groceries
Task 'Buy groceries' added with ID 1.

Choose an option: 4
1. Buy groceries [Pending]

Choose an option: 3
Enter task ID to mark as done: 1
Task 1 marked as done.

Choose an option: 4
1. Buy groceries [Done]
```

## File Structure

- `todo_app.py`: Main application script
- `tasks.json`: JSON file for storing tasks (created automatically)
- `README.md`: This file
- `LICENSE`: License information

## License

This project is licensed under the terms specified in the [LICENSE](LICENCE) file.
