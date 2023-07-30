from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Function to add a new task to the tasks.txt file
def add_task(task_description):
    with open("tasks.txt", "a") as file:
        file.write(f"{task_description}\n")

# Function to view all tasks stored in the tasks.txt file
def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
    except FileNotFoundError:
        tasks = []

    return tasks

# Function to remove a task from the tasks.txt file by its index
def remove_task(task_index):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt", "w") as file:
            if 1 <= task_index <= len(tasks):
                tasks.pop(task_index - 1)
                file.writelines(tasks)
                return True
    except FileNotFoundError:
        pass

    return False

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
            tasks = view_tasks()
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task.strip()}")
        elif choice == "3":
            try:
                task_index = int(input("Enter the index of the task to remove: "))
                if remove_task(task_index):
                    print("Task removed successfully!")
                else:
                    print("Invalid task index.")
            except ValueError:
                print("Invalid input. Please enter a valid task index.")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Move the route declarations here
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    task_description = request.form.get("task_description")
    add_task(task_description)
    return redirect(url_for("home"))

@app.route("/view", methods=["GET"])
def view():
    tasks = view_tasks()
    print(tasks)  # Add this line to check the tasks list
    return render_template("tasks.html", tasks=tasks)


@app.route("/remove", methods=["POST"])
def remove():
    task_index = int(request.form.get("task_index"))
    if remove_task(task_index):
        return redirect(url_for("view"))
    else:
        return "Invalid task index."

# Run the app here
if __name__ == "__main__":
    app.run(debug=True)
