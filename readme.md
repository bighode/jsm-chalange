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
CRIANDO PROJETO E DEFININDO SUPERUSER
------------------------------------------------------------

``
django-admin startproject jsmchalange .
python manage.py migrate
python manage.py createsuperuser
``
------------------------------------------------------------
``
1) incluir linhas 40 e 41 no arquivo /jsmchalange/settings.py
2) modificar linhas 17 e 21 do arquivo /jsmchalange/urls.py
3) criar pasta /api
4) criar arquivo /api/urls.py
5) criar arquivo /api/jsmutil.py
6) criar arquivo /api/jsmcsv.py
7) criar arquivo /api/jsmjson.py
8) criar arquivo /api/__init__.py
``