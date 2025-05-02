# 🐄 Projeto Integrador 1 - UNIVESP

Este repositório contém o desenvolvimento do **Projeto Integrador - DRP13-PJI110-SALA-001GRUPO-012** da UNIVESP.

O tema proposto neste semestre foi:  
**"Criar um sistema framework web versionado com noções de banco de dados."**

---

## 🎯 Objetivo

Criar um sistema web com interface visual **intuitiva**, **linguagem simplificada** e **uso de ícones e campos diretos**, com foco na **área rural**.

A proposta é facilitar o **registro de dados** relacionados à:

- 🥛 Ordenha
- 🌾 Alimentação
- 🏥 Saúde
- 🐮 Reprodução dos animais

---

## 🧱 Tecnologias utilizadas

- Python 3.10
- Django (Framework web principal)
- VS Code + WSL (Ubuntu)
- HTML/CSS (para a interface)
- Banco de dados (Django ORM — SQLite inicialmente, com possibilidade de PostgreSQL)

---

## 📁 Estrutura do projeto

projeto_integrador_1/ 
./
├── README.md
├── dev.sh
├── estrutura.txt
├── package-lock.json
├── package.json
├── postcss.config.js
├── requirements.txt
├── setup.sh
├── src
│   ├── modules
│   │   ├── alimentacao
│   │   ├── db.sqlite3
│   │   ├── manage.py
│   │   ├── ordenha
│   │   ├── reproducao
│   │   ├── saude
│   │   └── sistemarural
│   ├── static
│   └── templates
└── tailwind.config.js

## Status do projeto
Em desenvolvimento — Fase inicial de estruturação, criação do ambiente virtual e definição do escopo funcional com base nas pesquisas feitas ate aqui.

## Colaboradores
- Matheus Seco Bezerra - Desenvolvedor
- Bruno Diana
- Danieli Gimenez Siqueira
- Vinicius Leite Reis
- Josiane Rachopi da Silva
- Gabriel Santana da Rocha
- Bruno Thiago da Silva Brandino
- Carlos Vinicius

# Para rodar localmente
bash dev.sh

# Para preparar o projeto do zero
bash setup.sh

Feito com 💙 para a disciplina de Projeto Integrador da UNIVESP.