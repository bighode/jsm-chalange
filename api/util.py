def find_point(minlon, maxlon, minlat, maxlat, lon, lat) :
    if (lon <= minlon and lon >= maxlon and
        lat >= minlat and lat <= maxlat):
        return True
    else :
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
