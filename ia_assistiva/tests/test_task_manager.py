import unittest

from task_manager import (
    TaskManager,
    TaskNotFoundError,
    TaskValidationError,
)


class TaskManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manager = TaskManager()

    def test_add_task(self) -> None:
        task = self.manager.add_task(
            "  Preparar relatório  ",
            "MÉDIA",
            "2025-12-01",
        )

        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Preparar relatório")
        self.assertEqual(task.priority, "média")
        self.assertEqual(task.deadline.isoformat(), "2025-12-01")
        self.assertFalse(task.completed)

    def test_list_tasks(self) -> None:
        self.manager.add_task("Primeira", "alta", "2025-12-01")
        self.manager.add_task("Segunda", "baixa", "2025-12-02")

        tasks = self.manager.list_tasks()

        self.assertEqual(len(tasks), 2)
        self.assertEqual([task.id for task in tasks], [1, 2])

    def test_complete_task(self) -> None:
        task = self.manager.add_task("Estudar", "baixa", "2025-12-03")

        completed_task = self.manager.complete_task(task.id)

        self.assertTrue(completed_task.completed)
        self.assertTrue(self.manager.list_tasks()[0].completed)

    def test_reject_invalid_task_data(self) -> None:
        invalid_tasks = [
            ("   ", "alta", "2025-12-01"),
            ("Tarefa", "urgente", "2025-12-01"),
            ("Tarefa", "alta", "2025-02-30"),
            ("Tarefa", "alta", "01-12-2025"),
        ]

        for title, priority, deadline in invalid_tasks:
            with self.subTest(
                title=title,
                priority=priority,
                deadline=deadline,
            ):
                with self.assertRaises(TaskValidationError):
                    self.manager.add_task(title, priority, deadline)

        self.assertEqual(self.manager.list_tasks(), [])

    def test_reject_invalid_or_unknown_id(self) -> None:
        with self.assertRaises(TaskValidationError):
            self.manager.complete_task(0)

        with self.assertRaises(TaskNotFoundError):
            self.manager.complete_task(99)


if __name__ == "__main__":
    unittest.main()