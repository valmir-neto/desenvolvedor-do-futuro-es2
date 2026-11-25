from task_manager import (
    TaskManager,
    TaskNotFoundError,
    TaskValidationError,
)


def show_tasks(manager: TaskManager) -> None:
    tasks = manager.list_tasks()

    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nID   | Título | Prioridade | Prazo      | Situação")
    print("-" * 65)

    for task in tasks:
        status = "Concluída" if task.completed else "Pendente"
        print(
            f"{task.id:<4} | {task.title} | {task.priority} | "
            f"{task.deadline.isoformat()} | {status}"
        )


def main() -> None:
    manager = TaskManager()

    try:
        while True:
            print("\n=== Gerenciador de tarefas ===")
            print("1. Cadastrar tarefa")
            print("2. Listar tarefas")
            print("3. Concluir tarefa")
            print("0. Sair")

            choice = input("Escolha uma opção: ").strip()

            if choice == "1":
                title = input("Título: ")
                priority = input("Prioridade (alta, média, baixa): ")
                deadline = input("Prazo (AAAA-MM-DD): ")

                try:
                    task = manager.add_task(title, priority, deadline)
                    print(f"Tarefa {task.id} cadastrada com sucesso.")
                except TaskValidationError as exc:
                    print(f"Erro: {exc}")

            elif choice == "2":
                show_tasks(manager)

            elif choice == "3":
                raw_task_id = input("ID da tarefa: ").strip()

                try:
                    task_id = int(raw_task_id)
                except ValueError:
                    print("Erro: o ID deve ser um número inteiro.")
                    continue

                try:
                    manager.complete_task(task_id)
                    print(f"Tarefa {task_id} concluída.")
                except (TaskValidationError, TaskNotFoundError) as exc:
                    print(f"Erro: {exc}")

            elif choice == "0":
                print("Até logo!")
                break

            else:
                print("Opção inválida. Escolha uma opção do menu.")
    except EOFError:
        print("\nEntrada encerrada.")


if __name__ == "__main__":
    main()