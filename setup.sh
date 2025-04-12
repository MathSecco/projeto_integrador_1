#!/bin/bash

echo "Criando ambiente virtual..."
python3 -m venv venv
source venv/bin/activate

echo "Instalando dependências..."
pip install -r requirements.txt

echo "Executando migrações..."
python manage.py makemigrations
python manage.py migrate

echo "Pronto! Para iniciar o servidor, use:"
echo "source venv/bin/activate && python manage.py runserver"
