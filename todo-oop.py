class Task:
    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title}: {self.description} [{status}]"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task_index: int):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)

    def get_tasks(self):
        return self.tasks

class MainApp:
    def __init__(self):
        self.todo_list = ToDoList()

    def display_menu(self):
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Complete")
        print("4. View All Tasks")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.remove_task()
            elif choice == '3':
                self.mark_task_complete()
            elif choice == '4':
                self.view_all_tasks()
            elif choice == '5':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description (optional): ")
        task = Task(title, description)
        self.todo_list.add_task(task)
        print("Task added successfully.")

    def remove_task(self):
        self.view_all_tasks()
        task_index = int(input("Enter task number to remove: ")) - 1
        self.todo_list.remove_task(task_index)
        print("Task removed successfully.")

    def mark_task_complete(self):
        self.view_all_tasks()
        task_index = int(input("Enter task number to mark as complete: ")) - 1
        tasks = self.todo_list.get_tasks()
        if 0 <= task_index < len(tasks):
            tasks[task_index].mark_complete()
            print("Task marked as complete.")
        else:
            print("Invalid task number.")

    def view_all_tasks(self):
        tasks = self.todo_list.get_tasks()
        if tasks:
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("No tasks available.")

if __name__ == "__main__":
    app = MainApp()
    app.run()
