#!/usr/bin/env bash

# Instalar dependências Python
echo "Instalando dependências Python..."
pip install -r requirements.txt

# Coletar arquivos estáticos (output.css já incluso no Git)
echo "Coletando arquivos estáticos..."
python ./backend/manage.py collectstatic --noinput

# Aplicar migrações
echo "Aplicando migrações..."
python ./backend/manage.py migrate
