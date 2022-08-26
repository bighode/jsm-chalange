------------------------------------------------------------
PREPARANDO O AMBIENTE
------------------------------------------------------------

- Linux

   * mkdir jsm-chalange
   * cd jsm-chalange
   * virtualenv venv
   * source venv/bin/activate
   * pip install django
   * pip install djangorestframework

- Windows

   * md jsm-chalange
   * cd jsm-chalange
   * pipenv install django
   * pipenv install djangorestframework
   * pipenv shell

------------------------------------------------------------
CRIANDO PROJETO, APP E DEFININDO SUPERUSER
------------------------------------------------------------

django-admin startproject jsmchalange .
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp api

------------------------------------------------------------

1) incluí linhas 40 e 41 do arquivo /jsmchalange/settings.py
2) modificar linhas 17 e 21 do arquivo /jsmchalange/urls.py
3) criar arquivo /api/models.py
4) [opcional] acrescentar linhas 2 e 4 do arquivo admin.py
5) criar arquivo /api/serializer.py
6) modificar arquivo /api/views.py
7) criar arquivo /api/urls.py
8) testar o projeto neste ponto: 
   - python manage.py makemigrations
   - python manage.py migrate
   - python manage.py runserver
   - acessar a url http://127.0.0.1:8000   
   - clicar no link e http://127.0.0.1:8000/clientes/ e cadastrar um cliente
   
