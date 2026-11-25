# O Desenvolvedor do Futuro: Programador ou Orquestrador de Agentes?

Seminário de Engenharia de Software II — estudo comparativo exploratório entre GitHub Copilot Ask (IA assistiva) e GitHub Copilot Agent.

## Objetivo

Investigar diferenças de produtividade e intervenção humana no desenvolvimento de um gerenciador de tarefas em Python.

## Metodologia

As duas abordagens receberam os mesmos requisitos funcionais: cadastrar, listar e concluir tarefas, validar entradas e executar testes unitários. Foi realizada uma execução de desenvolvimento por abordagem.

- **Ask:** geração assistida de código, com integração e execução pelo desenvolvedor.
- **Agent:** implementação com acesso a arquivos e execução de comandos, sob supervisão humana.

## Resultados observados

| Métrica | IA assistiva | Agente |
| --- | ---: | ---: |
| Tempo de desenvolvimento | 13min45s | 5min11s |
| Testes originais aprovados | 5/5 | 9/9 |
| Cenários comuns de aceitação | 5/5 | 5/5 |

Diferença de tempo: 8min34s. Redução observada: 62,3% em relação à abordagem assistiva (514/825 segundos).

## Estrutura

- [ia_assistiva/](ia_assistiva): implementação e testes da abordagem assistiva.
- [agente_ia/](agente_ia): implementação e testes do agente.
- [REQUISITOS.md](REQUISITOS.md): requisitos do experimento.
- [REGISTRO.md](REGISTRO.md): registro de intervenção humana.
- [evidencias/](evidencias): registros textuais do experimento.

## Reprodução

Requer Python 3, sem bibliotecas externas.

```sh
git clone https://github.com/valmir-neto/desenvolvedor-do-futuro-es2.git
cd desenvolvedor-do-futuro-es2
cd ia_assistiva
python -m unittest discover -s tests -v
python main.py
```

Após sair da aplicação:

```sh
cd ../agente_ia
python -m unittest discover -s tests -v
python main.py
```

## Limitações

- Uma execução por abordagem não permite generalização estatística.
- As suítes originais são distintas; a quantidade de testes não mede isoladamente a qualidade.
- A redução de tempo é descritiva, não uma garantia de produtividade.
- Testes padronizados e novas execuções são etapas futuras.

## Conclusão

O agente apresentou menor tempo nesta execução. O desenvolvedor permanece responsável por especificar requisitos, supervisionar, revisar e validar o software.
