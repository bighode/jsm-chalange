import urllib.request, json 
import api.jsmutil as jsmutil

def get_jsonfile():
    url = "https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json"
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    return data

def parse_json():
    
    clientes = get_jsonfile()

    mail_list = []

    for cliente in clientes['results']:
        
        #  type
        lon = cliente['location']['coordinates']['longitude']
        lat = cliente['location']['coordinates']['latitude']
        cliente['type'] = jsmutil.get_type(lon, lat)

        # region
        cliente['region'] = jsmutil.get_region(cliente['location']['state'])

        # gender
        cliente['gender'] = jsmutil.abreviate_gender(cliente['gender'])

        # birthday
        cliente['birthday'] = cliente['dob']['date']
        del(cliente['dob'])

        # registered
        registered = cliente['registered']['date']
        del(cliente['registered'])
        cliente['registered'] = registered

        # nationality
        if not 'nationality' in cliente:
            cliente['nationality'] = 'BR'

        # telephoneNumbers
        cliente['telephoneNumbers'] = [
            jsmutil.parse_phone(cliente['phone'], cliente['nationality'])
        ]
        del(cliente['phone'])

        # mobileNumbers
        cliente['mobileNumbers'] = [
            jsmutil.parse_phone(cliente['cell'], cliente['nationality'])
        ]
        del(cliente['cell']) 

        #  cria lista de email
        mail_list.append(cliente['email'])
    
    # salva lista de emails
    jsmutil.save_json(mail_list, 'mail_list.json')

    return clientes['results']