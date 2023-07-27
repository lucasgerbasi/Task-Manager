# Function to add a new task to the tasks.txt file
def add_task(task_description):
    with open("tasks.txt", "a") as file:
        file.write(f"{task_description}\n")
    print("Task added successfully!")

# Function to view all tasks stored in the tasks.txt file
def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.")

# Function to remove a task from the tasks.txt file by its index
def remove_task(task_index):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt", "w") as file:
            if 1 <= task_index <= len(tasks):
                tasks.pop(task_index - 1)
                file.writelines(tasks)
                print("Task removed successfully!")
            else:
                print("Invalid task index.")
    except FileNotFoundError:
        print("No tasks found.")

# Main function to provide a command-line interface for the task manager
def main():
    while True:
        print("\nCommand Options:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task by its index")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_description = input("Enter task description: ")
            add_task(task_description)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_index = int(input("Enter the index of the task to remove: "))
                remove_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a valid task index.")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
