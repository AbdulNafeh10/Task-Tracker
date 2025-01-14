# Task Tracker Program

# File to store tasks
TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    try:
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
            return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_menu():
    """Display the menu to the user."""
    print("\nTask Tracker Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Exit")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter the new task: ")
    tasks.append(f"[ ] {task}")  # [ ] indicates a pending task
    print(f"Task '{task}' added!")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks available.")
        return
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def complete_task(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as completed: "))
        if task_num < 1 or task_num > len(tasks):
            print("Invalid task number.")
            return
        tasks[task_num - 1] = tasks[task_num - 1].replace("[ ]", "[X]")  # Mark as completed
        print("Task marked as completed!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
 
