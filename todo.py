import os

TODO_FILE = "task.txt"

def load_tasks():
    """Load Task from the file"""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]
    

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task)
            print("\n")


def show_tasks(tasks):
    """Show tasks"""
    if not tasks:
        print("\n No tasks found!")
    else:
        print("\n Your task")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(tasks):
    """Add task"""
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added!")


def refmove_task(tasks):
    """Remove task"""
    show_tasks(tasks)
    try:
        numb = int(input("Enter task number to remove: "))
        if 1 <= numb <=len (tasks):
            removed = tasks.pop(numb-1)
            save_tasks(tasks)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number")
        
    except ValueError:
        print("Please enter a valid task number")


def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose option: ").strip()
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            refmove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option . Try again.")

if __name__ == "__main__":
    main()