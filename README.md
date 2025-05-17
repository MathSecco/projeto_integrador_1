# 🐄 Projeto Integrador 1 - UNIVESP

Este repositório contém o desenvolvimento do **Projeto Integrador - DRP13-PJI110-SALA-001GRUPO-012** da UNIVESP.

📌 Tema proposto neste semestre:  
**"Criar um sistema framework web versionado com noções de banco de dados."**

---

## 🎯 Objetivo

Criar um sistema web com interface visual **intuitiva**, **linguagem simplificada** e **uso de ícones e campos diretos**, com foco na **área rural**.

A proposta é facilitar o **registro e gestão de dados** relacionados a:

- 🥛 Ordenha
- 🌾 Alimentação
- 🏥 Saúde
- 🐮 Reprodução animal

---

## 🧱 Tecnologias utilizadas

- Python 3.10
- Django 5.2
- Tailwind CSS 4
- PostgreSQL
- VS Code + WSL (Ubuntu)
- Render --> web site
- Supabase --> banco de dados

---

## 📁 Estrutura do projeto

```
projeto_integrador_1/
├── backend/
│   ├── apps/
│   │   ├── alimentacao/
│   │   ├── ordenha/
│   │   ├── reproducao/
│   │   ├── saude/
│   │   └── usuarios/
│   ├── sistemarural/     # settings, urls, wsgi, etc.
│   ├── static/
│   │   ├── css/
│   │   └── src/
│   ├── templates/
│   ├── manage.py
│   └── db.sqlite3
├── scripts/
│   ├── dev.sh
│   └── setup.sh
├── .vscode/
│   └── settings.json
├── staticfiles/
├── node_modules/
├── venv/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── package.json
├── package-lock.json
├── tailwind.config.js
└── postcss.config.js
```

---

## 🚧 Status do projeto

🛠️ **Finalizado**  
Online em:

- https://sistemarural.onrender.com/

---

## 👥 Colaboradores

- Matheus Seco Bezerra – Desenvolvedor
- Bruno Diana
- Danieli Gimenez Siqueira
- Vinicius Leite Reis
- Josiane Rachopi da Silva
- Gabriel Santana da Rocha
- Bruno Thiago da Silva Brandino
- Carlos Vinicius

---

## ▶️ Como executar localmente

### ✅ Iniciar o projeto em DEV

```bash
npm i
npm run venv
npm run requirements
npm run freeze
npm run makemigrations
npm run migrate
npm run dev
```

Feito com 💙 para a disciplina de **Projeto Integrador** da UNIVESP.