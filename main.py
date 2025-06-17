def load_tasks(filename="todo.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="todo.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n==== TO-DO LIST ====")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark task as complete")
    print("4. Save & Exit")

def display_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter a new task: ")
            tasks.append("[ ] " + new_task)
            print("✅ Task added.")
        elif choice == "3":
            display_tasks(tasks)
            num = input("Enter the task number to mark complete: ")
            if num.isdigit():
                index = int(num) - 1
                if 0 <= index < len(tasks):
                    if tasks[index].startswith("[ ]"):
                        tasks[index] = tasks[index].replace("[ ]", "[x]", 1)
                        print("✅ Task marked as complete.")
                    else:
                        print("⚠️ Task is already marked complete.")
                else:
                    print("⚠️ Invalid task number.")
            else:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Try again.")

main()
