import csv, urllib.request, codecs
from . import jsmutil

def get_csvfile():
    url = "https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv"
    ftpstream = urllib.request.urlopen(url)
    csvfile = csv.DictReader(codecs.iterdecode(ftpstream, 'utf-8'))
    return csvfile

def adjust_gender_key(row):
    row_dict = dict(row)
    new_dict = {}
    for key, value in row_dict.items():
        if 'gender' in key:
            new_dict['gender'] = jsmutil.abreviate_gender(value)
        else:
            new_dict[key] = value
    return new_dict

def parse_csv():

    # 1) baixa o arquivo csv e salva em csvfile
    csvfile = get_csvfile()

    mail_list = jsmutil.open_json('mail_list.json')

    # cria um dicionario vazio
    client_list = []        
    
    # percorrer a lista de clientes obtida em 1
    for row in csvfile:

        # corrige caracter inválido na chave gender
        cliente = adjust_gender_key(row)

        if not cliente['email'] in mail_list:

            # cria um dicionário vazio
            new_client = dict()

            #  coordinates
            coordinates = {
                'latitude': cliente['location__coordinates__latitude'],
                'longitude': cliente['location__coordinates__longitude']
            }

            #  others
            new_client['type'] = jsmutil.get_type(coordinates['latitude'], coordinates['longitude'])
            new_client['region'] = jsmutil.get_region(cliente['location__state'])
            new_client['gender'] = cliente['gender']
            new_client['email'] = cliente['email']
            new_client['birthday'] = cliente['dob__date']
            new_client['registered'] = cliente['registered__date']

            # nationality
            if not 'nationality' in cliente:
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
                'postcode': int(cliente['location__postcode']),
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
            new_client['telephoneNumbers'] = [jsmutil.parse_phone(cliente['phone'], new_client['nationality'])]
            new_client['mobileNumbers'] = [jsmutil.parse_phone(cliente['cell'], new_client['nationality'])]

            # picture
            picture = {
                'large': cliente['picture__large'],
                'medium': cliente['picture__medium'],
                'thumbnail': cliente['picture__thumbnail']
            }
            new_client['picture'] = picture
                    
            client_list.append(new_client)

    return client_list
