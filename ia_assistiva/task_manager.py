from dataclasses import dataclass
from datetime import date


class TaskValidationError(ValueError):
    """Indica que os dados de uma tarefa são inválidos."""


class TaskNotFoundError(LookupError):
    """Indica que uma tarefa com o ID informado não existe."""


@dataclass
class Task:
    id: int
    title: str
    priority: str
    deadline: date
    completed: bool = False


class TaskManager:
    VALID_PRIORITIES = {"alta", "média", "baixa"}

    def __init__(self) -> None:
        self._tasks: list[Task] = []
        self._next_id = 1

    def add_task(self, title: str, priority: str, deadline: str) -> Task:
        if not isinstance(title, str) or not title.strip():
            raise TaskValidationError("O título não pode ficar vazio.")

        if not isinstance(priority, str):
            raise TaskValidationError("A prioridade deve ser alta, média ou baixa.")

        normalized_priority = priority.strip().casefold()
        if normalized_priority == "media":
            normalized_priority = "média"

        if normalized_priority not in self.VALID_PRIORITIES:
            raise TaskValidationError("A prioridade deve ser alta, média ou baixa.")

        if not isinstance(deadline, str):
            raise TaskValidationError("O prazo deve estar no formato AAAA-MM-DD.")

        try:
            parsed_deadline = date.fromisoformat(deadline)
        except ValueError as exc:
            raise TaskValidationError(
                "Prazo inválido. Use uma data válida no formato AAAA-MM-DD."
            ) from exc

        if parsed_deadline.isoformat() != deadline:
            raise TaskValidationError("O prazo deve estar no formato AAAA-MM-DD.")

        task = Task(
            id=self._next_id,
            title=title.strip(),
            priority=normalized_priority,
            deadline=parsed_deadline,
        )
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self) -> list[Task]:
        return list(self._tasks)

    def complete_task(self, task_id: int) -> Task:
        if (
            isinstance(task_id, bool)
            or not isinstance(task_id, int)
            or task_id <= 0
        ):
            raise TaskValidationError("O ID deve ser um inteiro positivo.")

        for task in self._tasks:
            if task.id == task_id:
                task.completed = True
                return task

        raise TaskNotFoundError(f"Não existe tarefa com ID {task_id}.")