import json, re, phonenumbers

def save_json(json_content, filename):
    with open(filename, 'w+') as json_file:
        json.dump(json_content, json_file)

def open_json(filename):
    with open(filename) as json_file:
        data = json.load(json_file)    
    return data

def find_point(minlon, maxlon, minlat, maxlat, lon, lat):
    if (lon <= minlon and lon >= maxlon and
        lat >= minlat and lat <= maxlat):
        return True
    else:
        return False

def get_region(state):
    regions = open_json('region.json')
    for reg in regions:
        if state in reg['states']:
            return reg['name']
    return "NDA"    

def get_type(longitude, latitude):

    lon = float(longitude)
    lat = float(latitude)

    b_box = open_json('bbox.json')

    for i in range(len(b_box)):
        result = find_point(b_box[i]['minlon'], b_box[i]['maxlon'], 
            b_box[i]['minlat'], b_box[i]['maxlat'], lon, lat)
        if result:
            return b_box[i]['class']
    
    return 'trabalhoso'

def abreviate_gender(gender):
    return gender[0]

def parse_phone(phone, country):
    only_numbers = ''.join(re.findall(r'\d+', phone))
    my_number = phonenumbers.parse(only_numbers, country)
    e164_f=phonenumbers.format_number(my_number, phonenumbers.PhoneNumberFormat.E164)
    return e164_f