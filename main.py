class Task():
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Выполнено" if self.is_completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print(f"Задача добавлена: {description}")

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                print(f"Задача выполнена: {description}")
                return
        print(f"Задача с описанием '{description}' не найдена.")

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.is_completed]
        if current_tasks:
            print("Текущие задачи:")
            for task in current_tasks:
                print(task)
        else:
            print("Все задачи выполнены.")
task_manager = TaskManager()
task_manager.add_task("Купить продукты", "2023-10-05")
task_manager.add_task("Починить машину", "2023-10-10")
task_manager.show_current_tasks()
task_manager.mark_task_completed("Купить продукты")
task_manager.show_current_tasks()