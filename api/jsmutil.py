import json, re

def save_json(json_content, filename):
    with open(filename, 'w') as json_file:
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

def get_type(longitude, latitude):

    lon = float(longitude)
    lat = float(latitude)

    bounding_box = [
        {
            'minlon': -2.196998,
            'minlat': -46.361899,
            'maxlon': -15.411580,
            'maxlat': -34.276938,
            'class': 'especial'
        },
        {
            'minlon': -19.766959,
            'minlat': -52.997614,
            'maxlon': -23.966413,
            'maxlat': -44.428305,
            'class': 'especial'
        },
        {
            'minlon': -26.155681,
            'minlat': -54.777426,
            'maxlon': -34.016466,
            'maxlat': -46.603598,
            'class': 'normal'
        }
    ]    

    for i in range(len(bounding_box)):
        result = find_point(bounding_box[i]['minlon'], bounding_box[i]['maxlon'], 
            bounding_box[i]['minlat'], bounding_box[i]['maxlat'], lon, lat)
        if result:
            return bounding_box[i]['class']
    
    return 'trabalhoso'

def abreviate_gender(gender):
    return gender[0]

def parse_phone(phone, country):
    only_numbers = re.findall(r'\d+', phone)
    result = '+' + get_country_code(country) + ''.join(only_numbers)
    return result

def get_country_code(country):
    cc = { 
        'AF':'93','AL':'355','DZ':'213','AS':'1-684','AD':'376','AO':'244','AI':'1-264','AQ':'672',
        'AG':'1-268','AR':'54','AM':'374','AW':'297','AU':'61','AT':'43','AZ':'994','BS':'1-242',
        'BH':'973','BD':'880','BB':'1-246','BY':'375','BE':'32','BZ':'501','BJ':'229','BM':'1-441',
        'BT':'975','BO':'591','BA':'387','BW':'267','BR':'55','IO':'246','VG':'1-284','BN':'673',
        'BG':'359','BF':'226','BI':'257','KH':'855','CM':'237','CA':'1','CV':'238','KY':'1-345',
        'CF':'236','TD':'235','CL':'56','CN':'86','CX':'61','CC':'61','CO':'57','KM':'269',
        'CK':'682','CR':'506','HR':'385','CU':'53','CW':'599','CY':'357','CZ':'420','CD':'243',
        'DK':'45','DJ':'253','DM':'1-767','TL':'670','EC':'593','EG':'20','SV':'503','GQ':'240',
        'ER':'291','EE':'372','ET':'251','FK':'500','FO':'298','FJ':'679','FI':'358','FR':'33',
        'PF':'689','GA':'241','GM':'220','GE':'995','DE':'49','GH':'233','GI':'350','GR':'30',
        'GL':'299','GD':'1-473','GU':'1-671','GT':'502','GG':'44-1481','GN':'224','GW':'245',
        'GY':'592','HT':'509','HN':'504','HK':'852','HU':'36','IS':'354','IN':'91','ID':'62','IR':'98',
        'IQ':'964','IE':'353','IM':'44-1624','IL':'972','IT':'39','CI':'225','JM':'1-876','JP':'81',
        'JE':'44-1534','JO':'962','KZ':'7','KE':'254','KI':'686','XK':'383','KW':'965','KG':'996','LA':'856',
        'LV':'371','LB':'961','LS':'266','LR':'231','LY':'218','LI':'423','LT':'370','LU':'352','MO':'853',
        'MK':'389','MG':'261','MW':'265','MY':'60','MV':'960','ML':'223','MT':'356','MH':'692','MR':'222',
        'MU':'230','YT':'262','MX':'52','FM':'691','MD':'373','MC':'377','MN':'976','ME':'382','MS':'1-664',
        'MA':'212','MZ':'258','MM':'95','NA':'264','NR':'674','NP':'977','NL':'31','AN':'599','NC':'687',
        'NZ':'64','NI':'505','NE':'227','NG':'234','NU':'683','KP':'850','MP':'1-670','NO':'47','OM':'968',
        'PK':'92','PW':'680','PS':'970','PA':'507','PG':'675','PY':'595','PE':'51','PH':'63','PN':'64','PL':'48',
        'PT':'351','QA':'974','CG':'242','RE':'262','RO':'40','RU':'7','RW':'250','BL':'590','SH':'290','KN':'1-869',
        'LC':'1-758','MF':'590','PM':'508','VC':'1-784','WS':'685','SM':'378','ST':'239','SA':'966','SN':'221',
        'RS':'381','SC':'248','SL':'232','SG':'65','SX':'1-721','SK':'421','SI':'386','SB':'677','SO':'252','ZA':'27',
        'KR':'82','SS':'211','ES':'34','LK':'94','SD':'249','SR':'597','SJ':'47','SZ':'268','SE':'46','CH':'41',
        'SY':'963','TW':'886','TJ':'992','TZ':'255','TH':'66','TG':'228','TK':'690','TO':'676','TT':'1-868',
        'TN':'216','TR':'90','TM':'993','TC':'1-649','TV':'688','VI':'1-340','UG':'256','UA':'380','AE':'971',
        'GB':'44','US':'1','UY':'598','UZ':'998','VU':'678','VA':'379','VE':'58','VN':'84','WF':'681',
        'EH':'212','YE':'967','ZM':'260','ZW':'263'
    }
    return cc[country]