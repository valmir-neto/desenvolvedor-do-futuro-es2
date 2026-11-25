import unittest
from datetime import date

from task_manager import TaskManager


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_and_list_task(self):
        task = self.manager.add_task("Estudar Python", "alta", "2026-12-01")

        self.assertEqual(self.manager.list_tasks(), [task])
        self.assertEqual(task.title, "Estudar Python")
        self.assertEqual(task.priority, "alta")
        self.assertEqual(task.deadline, date(2026, 12, 1))
        self.assertFalse(task.completed)

    def test_add_task_trims_title_and_normalizes_medium_priority(self):
        task = self.manager.add_task("  Revisar  ", "MEDIA", "2026-12-01")

        self.assertEqual(task.title, "Revisar")
        self.assertEqual(task.priority, "média")

    def test_add_task_rejects_empty_title(self):
        with self.assertRaisesRegex(ValueError, "título"):
            self.manager.add_task("  ", "baixa", "2026-12-01")

    def test_add_task_rejects_invalid_priority(self):
        with self.assertRaisesRegex(ValueError, "Prioridade"):
            self.manager.add_task("Tarefa", "urgente", "2026-12-01")

    def test_add_task_rejects_invalid_deadline(self):
        with self.assertRaisesRegex(ValueError, "Prazo"):
            self.manager.add_task("Tarefa", "baixa", "01/12/2026")

    def test_add_task_rejects_deadline_without_iso_separators(self):
        with self.assertRaisesRegex(ValueError, "Prazo"):
            self.manager.add_task("Tarefa", "baixa", "20261201")

    def test_complete_task_marks_task_completed(self):
        task = self.manager.add_task("Enviar relatório", "média", "2026-12-01")

        self.manager.complete_task(1)

        self.assertTrue(task.completed)

    def test_complete_task_rejects_unknown_task_number(self):
        with self.assertRaisesRegex(ValueError, "Número"):
            self.manager.complete_task(1)

    def test_empty_manager_lists_no_tasks(self):
        self.assertEqual(self.manager.list_tasks(), [])


if __name__ == "__main__":
    unittest.main()
