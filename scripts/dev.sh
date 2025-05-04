#!/bin/bash

echo "🔄 Ativando ambiente virtual..."
source venv/bin/activate

echo "📦 Instalando dependências (se houver alterações)..."
pip install -r requirements.txt

echo "🛠️ Aplicando migrações..."
python manage.py makemigrations
python manage.py migrate

echo "🚀 Iniciando servidor Django em http://127.0.0.1:8000 ..."
python manage.py runserver
