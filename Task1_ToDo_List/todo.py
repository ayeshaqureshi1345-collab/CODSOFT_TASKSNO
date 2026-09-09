import json


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecoderError):
        return []

    

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent = 4) 


tasks = load_tasks()   
            

def add_task():
    task = input("Enter a task: ")

    if not task.strip():
        print("Task cannot be empty.")
        return

    task_details = {
        "name": task,
        "completed": False
    }

    tasks.append(task_details)

    save_tasks()

    print("Task added successfully!")



def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start = 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['name']} - {status}")


           
def mark_completed():
    if not tasks:
        print("No tasks found.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to mark as completed: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        task = tasks[task_number - 1]

        if task["completed"]:
            print("Task is already completed.")
            return
        
        task["completed"] = True

        save_tasks()

        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number.")



def delete_task():
    if not tasks:
        print("No tasks found.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        tasks.pop(task_number - 1)

        save_tasks()

        print("Task deleted successfully!")

    except ValueError:
        print("Please enter a valid number.")

   

def main():
    while True:
        print("\n=================================")
        print("        TO DO LIST MANAGER")
        print("=================================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using To-Do List Manager!")
            break
        else:
            print("Invlaid choice. Please try again.")

main()            

