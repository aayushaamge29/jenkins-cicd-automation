from app.models.task_model import Task

tasks = []

class TaskService:

    def get_tasks(self):
        return [task.to_dict() for task in tasks]

    def create_task(self, title):

        task = Task(len(tasks) + 1, title)

        tasks.append(task)

        return task.to_dict()

    def delete_task(self, task_id):

        global tasks

        tasks = [t for t in tasks if t.id != task_id]

        return {"message": "Task deleted"}