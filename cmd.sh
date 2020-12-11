#!/bin/sh
set -e
echo "Atualizando depedências do projeto..."
python -m pip install --upgrade pip && pip install -r /requirements.txt
echo "Configurando ambiente de desenvolvimento..."
export FLASK_ENV=development && export FLASK_APP=/app/app.py
echo "Iniciando ambiente de desenvolvimento..."
exec flask run
