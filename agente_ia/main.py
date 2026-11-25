from task_manager import TaskManager


def run_cli():
    manager = TaskManager()
    print("Gerenciador de tarefas")

    while True:
        print("\n1. Cadastrar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("0. Sair")
        choice = input("Escolha uma opção: ").strip()

        if choice == "0":
            print("Até logo!")
            return
        if choice == "1":
            _add_task(manager)
        elif choice == "2":
            _list_tasks(manager)
        elif choice == "3":
            _complete_task(manager)
        else:
            print("Opção inválida.")


def _add_task(manager):
    title = input("Título: ")
    priority = input("Prioridade (baixa, média ou alta): ")
    deadline = input("Prazo (AAAA-MM-DD): ")
    try:
        manager.add_task(title, priority, deadline)
    except ValueError as error:
        print(f"Erro: {error}")
    else:
        print("Tarefa cadastrada com sucesso.")


def _list_tasks(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "concluída" if task.completed else "pendente"
        print(
            f"{number}. {task.title} | Prioridade: {task.priority} | "
            f"Prazo: {task.deadline.isoformat()} | Status: {status}"
        )


def _complete_task(manager):
    try:
        raw_task_number = input("Número da tarefa: ").strip()
        task_number = int(raw_task_number)
    except ValueError:
        print("Erro: informe um número de tarefa válido.")
        return

    try:
        manager.complete_task(task_number)
    except ValueError as error:
        print(f"Erro: {error}")
    else:
        print("Tarefa marcada como concluída.")


if __name__ == "__main__":
    run_cli()
