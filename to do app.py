tasks = []

def menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == "3":
        task_no = int(input("Enter task number to delete: "))
        if 0 < task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("🗑️ Task deleted!")
        else:
            print("❌ Invalid task number")

    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice, try again.")
