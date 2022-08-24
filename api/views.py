from rest_framework.response import Response
from rest_framework.decorators import api_view

# meus imports
import csv, urllib.request, codecs, json

def get_csvfile():
    url = "https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv"
    ftpstream = urllib.request.urlopen(url)
    csvfile = csv.DictReader(codecs.iterdecode(ftpstream, 'utf-8'))
    return csvfile

def abreviate_gender(gender):
    return gender[0]

def adjust_gender_key(row):
    row_dict = dict(row)
    new_dict = {}
    for key, value in row_dict.items():
        if 'gender' in key:
            new_dict['gender'] = abreviate_gender(value)
        else:
            new_dict[key] = value
    return new_dict

@api_view(['GET'])
def getData(request):

    # 1) vou tratar o CSV
    # criar um novo json com o formato especificado no desafio
    csvfile = get_csvfile()

    client_list = []

    for row in csvfile:
        cliente = adjust_gender_key(row)
        
        new_client = {}
        new_client['type'] = 'laborious'
        new_client['gender'] = cliente['gender']
        new_client['name'] = {
            'title': cliente['name__title'],
            'first': cliente['name__first'],
            'last': cliente['name__last']
        }
        client_list.append(new_client)

    # 2) vou tratar o json

    
    return Response(client_list)    



