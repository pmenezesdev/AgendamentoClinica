# 🏥 Sistema de Agendamento Inteligente em Clínicas de Caruaru

Este projeto acadêmico visa desenvolver um sistema de agendamento de consultas médicas otimizado, focado em clínicas da cidade de Caruaru. O objetivo principal é reduzir filas e otimizar o tempo de atendimento, tanto para pacientes quanto para profissionais de saúde.

## 📝 Contexto e Problema

A gestão de agendamentos em clínicas pode ser um desafio, resultando em longos tempos de espera, ociosidade de profissionais e insatisfação dos pacientes. Em Caruaru, como em muitas cidades, a otimização desse processo é crucial para melhorar a eficiência do sistema de saúde. Este projeto acadêmico, identificado como **ID 4**, foca na resolução desses problemas através de uma abordagem de **Backend e Algoritmos de Otimização (Scheduling)**.

## 🚀 Abordagem Técnica e Lógica Inteligente

*   **Framework:** O projeto é desenvolvido utilizando **Django**, um poderoso framework web em Python, que garante rapidez no desenvolvimento e segurança.
*   **Banco de Dados:** Para simplicidade e prototipagem rápida, utilizamos o **SQLite**, que é o banco de dados padrão do Django.
*   **Lógica Inteligente (Otimização):** A inteligência do sistema reside na sua capacidade de agendamento automático. Ao solicitar uma consulta para um médico em uma data específica, o sistema irá buscar o **primeiro horário disponível** naquele dia, respeitando um intervalo fixo de **30 minutos** por consulta. Essa lógica garante o preenchimento eficiente da agenda do médico.

## 📦 Estrutura do Projeto (Modelos Principais)

O coração do sistema é composto pelos seguintes modelos Django no app `core`:

*   **`Medico`**: Representa um profissional de saúde.
    *   `nome`: Nome completo do médico.
    *   `especialidade`: Área de atuação do médico.
    *   `horario_inicio_atendimento`: Horário em que o médico inicia o atendimento (ex: 08:00).
    *   `horario_fim_atendimento`: Horário em que o médico encerra o atendimento (ex: 18:00).

*   **`Consulta`**: Representa uma consulta agendada.
    *   `medico`: Chave estrangeira para o médico da consulta.
    *   `paciente_nome`: Nome do paciente agendado.
    *   `data`: Data da consulta.
    *   `horario`: Horário exato da consulta (definido pela lógica inteligente).
    *   `status`: Estado atual da consulta ('Agendada', 'Cancelada', 'Realizada').

## ▶️ Como Executar o Projeto (Instruções de Instalação)

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local:

1.  **Clonar o repositório:**

    ```bash
    git clone <URL_DO_SEU_REPOSITÓRIO>
    cd Sistema-Agendamento-Caruaru/AgendamentoClinica
    ```

2.  **Criar e ativar um ambiente virtual:**

    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instalar as dependências:**

    ```bash
    pip install django
    ```

4.  **Executar as migrações do banco de dados:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Criar um superusuário (para acessar o Admin do Django):**

    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções no terminal para criar seu usuário e senha.

6.  **Executar o servidor local:**

    ```bash
    python manage.py runserver
    ```

7.  **Acessar o sistema:**
    *   Abra seu navegador e acesse: `http://127.0.0.1:8000/admin/` para o painel administrativo do Django.
    *   Acesse as URLs da aplicação:
        *   `http://127.0.0.1:8000/api/medicos/` para listar os médicos.
        *   `http://127.0.0.1:8000/api/agendar/` para acessar o formulário de agendamento.
        *   `http://127.0.0.1:8000/api/agendar/<medico_id>/` para agendar com um médico pré-selecionado.

## 🤝 Contribuições e Autoria

Este projeto é um esforço acadêmico. Contribuições na forma de issues e pull requests são bem-vindas!

Autor: Pedro Lucas Menezes de Oliveira
