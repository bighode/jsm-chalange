from rest_framework.response import Response
from rest_framework.decorators import api_view

# meus imports
import csv, urllib.request, codecs, json
from api.util import get_type

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

def parse_csv():

    csvfile = get_csvfile()

    client_list = []        
    
    for row in csvfile:
        cliente = adjust_gender_key(row)
        new_client = dict()

        #  coordinates
        coordinates = {
            'latitude': cliente['location__coordinates__latitude'],
            'longitude': cliente['location__coordinates__longitude']
        }

        #  others
        new_client['type'] = get_type(coordinates['latitude'], coordinates['longitude'])
        new_client['gender'] = cliente['gender']
        new_client['email'] = cliente['email'],
        new_client['birthday'] = cliente['dob__date'],
        new_client['registered'] = cliente['registered__date']
        new_client['nationality'] = 'BR'
        
        #  name
        name = {
            'title': cliente['name__title'],
            'first': cliente['name__first'],
            'last': cliente['name__last']
        }
        new_client['name'] = name

        #  location
        location = {
            'street': cliente['location__street'],
            'city': cliente['location__city'],
            'state': cliente['location__state'],
            'postcode': cliente['location__postcode'],
            'cordinates': coordinates,
        }
        new_client['location'] = location

        #  timezone
        timezone = {
            'offset': cliente['location__timezone__offset'],
            'description': cliente['location__timezone__description'],
        }
        new_client['timezone'] = timezone 

        # phones
        new_client['telephoneNumbers'] = [cliente['phone']]
        new_client['mobileNumbers'] = [cliente['cell']]

        # picture
        picture = {
            'large': cliente['picture__large'],
            'medium': cliente['picture__medium'],
            'thumbnail': cliente['picture__thumbnail']
        }
        new_client['picture'] = picture
                
        client_list.append(new_client)
    return client_list  

@api_view(['GET'])
def getData(request):

    # 1) vou tratar o CSV
    # criar um novo json com o formato especificado no desafio
    csv_list = parse_csv()


    # # 2) vou tratar o json

    return Response(csv_list)    



