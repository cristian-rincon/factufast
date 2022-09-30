# Factufast

Simple invoice service

## Install dependencies

You need to install the following packages before running the code:
```bash
pip install poetry
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true
poetry install

sudo apt update
sudo apt install wkhtmltopdf
```

## Run the server

```bash
poetry run python manage.py runserver
```
