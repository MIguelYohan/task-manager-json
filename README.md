# Gerenciador de Tarefas com POO em Python

Este projeto é um **Gerenciador de Tarefas** simples desenvolvido em Python, focado na aplicação e demonstração de conceitos de Programação Orientada a Objetos (POO). Ele permite adicionar, remover, buscar, marcar como concluídas e listar tarefas, persistindo os dados em um arquivo JSON.

## Conceitos de POO Aplicados

O código foi estruturado para exemplificar os seguintes princípios de POO:

*   **Classes e Objetos:** Duas classes principais, `TaskManager` e `Task`, representam as entidades centrais do sistema. `TaskManager` gerencia uma coleção de objetos `Task`.
*   **Encapsulamento:** Atributos internos das classes (ex: `_manager` em `TaskManager`, `_text`, `_id`, `_done` em `Task`) são protegidos e acessados/modificados através de métodos e propriedades (`@property`, `@setter`), garantindo a integridade dos dados.
*   **Propriedades (`@property` e `@setter`):** Utilizadas para controlar o acesso e a modificação de atributos, como `save_to` em `TaskManager` e `text`, `done` em `Task`, permitindo validações e lógica adicional durante a atribuição.
*   **Métodos de Classe (`@classmethod`):** A classe `Task` possui um método de classe `from_dict` que permite criar uma instância de `Task` a partir de um dicionário, facilitando a desserialização de dados.
*   **Modularidade:** A separação das responsabilidades entre `TaskManager` (gerenciamento da coleção de tarefas) e `Task` (representação de uma única tarefa) promove um código mais organizado e fácil de manter.

## Funcionalidades

*   **Adicionar Tarefa:** Inclui validação para evitar tarefas duplicadas.
*   **Salvar/Carregar Tarefas:** Persistência de dados em um arquivo JSON (`taskfile.json`).
*   **Excluir Tarefa:** Remove uma tarefa específica ou sugere uma tarefa similar se houver.
*   **Buscar Tarefa:** Encontra uma tarefa pelo nome ou sugere uma similar.
*   **Marcar Tarefa como Concluída:** Altera o status de uma tarefa para concluída.
*   **Listar Tarefas:** Exibe todas as tarefas com seus status (concluída/pendente).

## Como Usar

1.  Clone o repositório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```
2.  Execute o script Python:
    ```bash
    python seu_script.py
    ```
    *(Nota: Atualmente, a interação é via código. Para ver as funcionalidades em ação, você precisará adicionar chamadas aos métodos da classe `TaskManager` no seu script.)*

## Planos Futuros

Para aprimorar a interação com o usuário, pretendo desenvolver uma **Interface Gráfica do Usuário (GUI)** para este gerenciador de tarefas. As opções consideradas para a implementação são:

*   **PyAutoGUI:** Para automação de interface e possíveis interações mais diretas com o sistema operacional.
*   **Tkinter:** Para a criação de uma interface gráfica nativa e mais tradicional em Python.

Esta adição tornará o gerenciador de tarefas mais acessível e fácil de usar para o público geral.

## Tecnologias

*   Python 3.x
*   Módulos `datetime`, `difflib`, `uuid`, `json`, `os`.
