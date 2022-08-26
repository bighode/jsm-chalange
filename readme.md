Solução para o Desafio
======================
- https://github.com/juntossomosmais/code-challenge

Tecnologias Adotadas
--------------------
* Python
* Django
* djangorestframework

Preparação do ambiente
----------------------

- Linux
```
mkdir jsm-chalange
cd jsm-chalange
virtualenv venv
source venv/bin/activate
pip install django
pip install djangorestframework
```
- Windows
```
md jsm-chalange
cd jsm-chalange
pipenv install django
pipenv install djangorestframework
pipenv shell
```
Criando o Projeto e Definindo 'superuser'
------------------------------------------------------------
```
django-admin startproject jsmchalange .
python manage.py migrate
python manage.py createsuperuser
```
------------------------------------------------------------
Passos
------------------------------------------------------------

1) incluir linhas 40 e 41 no arquivo /jsmchalange/settings.py
2) modificar linhas 17 e 21 do arquivo /jsmchalange/urls.py
3) criar pasta /api
4) criar arquivo /api/urls.py
5) criar arquivo /api/jsmutil.py
6) criar arquivo /api/jsmcsv.py
7) criar arquivo /api/jsmjson.py
8) criar arquivo /api/__init__.py

------------------------------------------------------------
Executando
------------------------------------------------------------

```
python manage.py runserver
```
------------------------------------------------------------
Acessando a API
------------------------------------------------------------
* http://127.0.0.1:8000/clientes

    Retorna todos os clientes (2000)

* http://127.0.0.1:8000/clientes?type=especial

    Retorna apenas os clientes cujo tipo foi especificado em **'type'**