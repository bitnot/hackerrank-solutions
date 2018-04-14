from math import acos,sin,cos,radians

def calc_dist(a,b):
    lat1, lon1, lat2, lon2 = a['lat'],a['lon'],b['lat'],b['lon'] 
    if ((lat1 == lat2) and (lon1 == lon2)):
        return 0
    degree2radians = radians
    EARTH_RADIUS = 6371 #in km
    point1_lat_in_radians = degree2radians( lat1 )
    point2_lat_in_radians = degree2radians( lat2 )
    point1_long_in_radians = degree2radians( lon1 )
    point2_long_in_radians = degree2radians( lon2)
    return acos( sin( point1_lat_in_radians ) * sin( point2_lat_in_radians ) +
                 cos( point1_lat_in_radians ) * cos( point2_lat_in_radians ) *
                 cos( point2_long_in_radians - point1_long_in_radians) ) * EARTH_RADIUS

nr_guests = int(input().strip())
group_passions = set()
for g0 in range(nr_guests):
    m, *passions = input().strip().split(' ')
    group_passions |= set(passions)
    
nr_places = int(input().strip())
places = []
for p0 in range(nr_places):
    name, lat, lon, z, *passions = input().strip().split(' ')
    places.append({
        'name': name,
        'lat': float(lat),
        'lon': float(lon),
        'passions': set(passions)
    })
    
vacations = [] # nr_places*(nr_places-1)/2
for i in range(0, nr_places - 1):
    for j in range(i+1, nr_places):
        vacations.append({
                'names': ' '.join(sorted([places[i]['name'],places[j]['name']])),
                'score': len( group_passions & (places[i]['passions'] | places[j]['passions']) ),
                'dist': calc_dist(places[i], places[j])
            })
    
vacations = sorted(vacations, key = lambda x: [-x['score'], x['dist']])
if len(vacations) > 0:
    print(vacations[0]['names'])