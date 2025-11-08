# Projeto Conta Bancária com TDD

Este é um pequeno projeto que demonstra a implementação de uma classe `ContaBancaria` em Python, utilizando a metodologia de Desenvolvimento Guiado por Testes (TDD).

## O que é TDD?

O TDD é uma prática de desenvolvimento de software que inverte a lógica tradicional de programação. Em vez de escrever o código da funcionalidade primeiro e os testes depois, o TDD segue um ciclo curto e repetitivo:

1.  **Fase Vermelha (Red):** Escrever um teste automatizado para uma nova funcionalidade que ainda não existe. Como a funcionalidade não foi implementada, o teste irá falhar (ficar "vermelho").
2.  **Fase Verde (Green):** Escrever a quantidade mínima de código necessária para fazer o teste passar (ficar "verde"). Nesta fase, o foco é apenas fazer o teste funcionar, sem se preocupar com a qualidade do código.
3.  **Fase de Refatoração (Refactor):** Com a garantia dos testes, o código pode ser melhorado e "limpo" (refatorado) sem alterar seu comportamento externo.

## Funcionalidades da `ContaBancaria`

- Uma nova conta é criada com saldo inicial de R$ 0,00.
- É possível depositar valores positivos, que são somados ao saldo.
- É possível sacar valores positivos, que são subtraídos do saldo.
- O sistema impede depósitos de valores nulos ou negativos.
- O sistema impede saques de valores nulos ou negativos.
- O sistema impede saques de valores maiores que o saldo disponível.


## Como Rodar o Projeto

Siga os passos abaixo para configurar e executar os testes do projeto.

### 1. Pré-requisitos

- Python 3.x instalado.
- `pip` (gerenciador de pacotes do Python).


### 2. Instale o pytest

- pip install pytest

### 3. Como rodar os testes?

- No prompt de comando escreva `pytest`


