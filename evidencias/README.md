# Evidências do experimento

Transcrições parciais de três capturas originais do VS Code. Caminhos locais e informações de interface foram omitidos. Não são novas execuções.

## 1. Testes unitários do agente

Fonte: evidencia_original_1.png. O terminal mostra:

```text
Ran 9 tests in 0.002s
OK
```

O tempo acima corresponde à execução dos testes, não ao desenvolvimento.

## 2. Validação de prazo — agente

Fonte: evidencia_original_2.png.

```text
Escolha uma opção: 1
Título: B
Prioridade (baixa, média ou alta): alta
Prazo (AAAA-MM-DD): 2026-02-30
Erro: Prazo inválido. Use o formato AAAA-MM-DD.
```

## 3. Validação de prazo — IA assistiva

Fonte: evidencia_original_3.png.

```text
Escolha uma opção: 1
Título: A
Prioridade (alta, média, baixa): alta
Prazo (AAAA-MM-DD): 2026-02-30
Erro: Prazo inválido. Use uma data válida no formato AAAA-MM-DD.
```

Ambas rejeitaram a data inexistente. As capturas não demonstram, isoladamente, todos os cenários de aceitação nem os tempos de desenvolvimento.

As capturas das validações manuais acima permanecem apenas transcritas.

## Capturas dos testes automatizados

- [Copilot Ask — 5/5 aprovados](testes_ask.png).
- [Copilot Agent — 9/9 aprovados](testes_agent.png).
- [Testes padronizados — 40/40 aprovados em 6,313 segundos](testes_padronizados.png).

Os tempos de execução dos testes não correspondem aos tempos de desenvolvimento.
