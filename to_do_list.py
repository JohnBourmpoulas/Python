import json

FILENAME = "todo_list.json"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(FILENAME, "w") as file:
            json.dump(tasks, file)
    except:
        print("Failed to save.")

def view_tasks(tasks):
    print()
    if not tasks["tasks"]:
        print("No tasks to display.")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks["tasks"], 1):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx}. {task['description']} | {status}")

def create_task(tasks):
    desc = input("Enter the task description: ").strip()
    if desc:
        tasks["tasks"].append({"description": desc, "complete": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Description cannot be empty.")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as complete: ").strip())
        if 1 <= num <= len(tasks["tasks"]):
            tasks["tasks"][num - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def remove_task(tasks):
    if not tasks["tasks"]:
        print("\nNo tasks to remove.")
        return

    view_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: ").strip())
        if 1 <= num <= len(tasks["tasks"]):
            removed = tasks["tasks"].pop(num - 1)
            save_tasks(tasks)
            print(f"Task '{removed['description']}' removed.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Manager")
        print("1. View tasks")
        print("2. Add new task")
        print("3. Mark task as complete")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
