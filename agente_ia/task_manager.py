from dataclasses import dataclass
from datetime import date


PRIORITIES = ("baixa", "média", "alta")


@dataclass
class Task:
    title: str
    priority: str
    deadline: date
    completed: bool = False


class TaskManager:
    def __init__(self):
        self._tasks = []

    def add_task(self, title, priority, deadline):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("O título não pode ficar vazio.")

        if not isinstance(priority, str):
            raise ValueError("Prioridade inválida. Use baixa, média ou alta.")
        normalized_priority = priority.strip().casefold()
        if normalized_priority == "media":
            normalized_priority = "média"
        if normalized_priority not in PRIORITIES:
            raise ValueError("Prioridade inválida. Use baixa, média ou alta.")

        parsed_deadline = self._parse_deadline(deadline)
        task = Task(title.strip(), normalized_priority, parsed_deadline)
        self._tasks.append(task)
        return task

    def list_tasks(self):
        return list(self._tasks)

    def complete_task(self, task_number):
        if (
            isinstance(task_number, bool)
            or not isinstance(task_number, int)
            or task_number < 1
            or task_number > len(self._tasks)
        ):
            raise ValueError("Número de tarefa inválido.")
        self._tasks[task_number - 1].completed = True

    @staticmethod
    def _parse_deadline(deadline):
        if isinstance(deadline, date):
            return deadline
        if not isinstance(deadline, str):
            raise ValueError("Prazo inválido. Use o formato AAAA-MM-DD.")
        try:
            parsed_deadline = date.fromisoformat(deadline.strip())
            if parsed_deadline.isoformat() != deadline.strip():
                raise ValueError
            return parsed_deadline
        except ValueError as error:
            raise ValueError("Prazo inválido. Use o formato AAAA-MM-DD.") from error
