# Experimento: IA assistiva versus agente de IA

Implemente em Python 3, sem dependências externas, um gerenciador de tarefas em terminal.

Requisitos:
1. Cadastrar tarefa com título não vazio, prioridade (alta, média, baixa) e prazo (AAAA-MM-DD válido).
2. Listar tarefas com ID, título, prioridade, prazo e situação.
3. Concluir tarefa pelo ID; rejeitar ID inexistente.
4. Validar entradas inválidas sem encerrar o programa inesperadamente.
5. Criar testes automatizados com unittest para cadastro, listagem, conclusão e entradas inválidas.

Critérios de aceitação: executar `python -m unittest discover -s tests -v` e iniciar a aplicação com `python main.py`.

Regras do experimento: mesmas instruções, ambiente e tempo de medição para as duas abordagens; não copiar a implementação de uma para a outra. Registrar número de prompts, intervenções, testes e tempo. O agente deve ter acesso real a arquivos e execução de comandos; chat com resposta de código não é suficiente.

