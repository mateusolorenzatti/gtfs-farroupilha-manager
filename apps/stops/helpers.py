from apps.stops.models import Stops

def paradas_proximas(lat, lon, dif = -0.000500):
    '''
    Encontrar as paradas compreendidas na área de um quadrado 
    de 'DIF' em relação ao ponto enviado. 
    '''    

    coo_lt = { 'lat': lat - dif, 'lon': lon + dif }
    coo_rb = { 'lat': lat + dif, 'lon': lon - dif }

    paradas = Stops.objects.filter( 
        stop_lat__gte = coo_rb['lat'],
        stop_lat__lte = coo_lt['lat'],
        stop_lon__gte = coo_lt['lon'],  
        stop_lon__lte = coo_rb['lon']
    )

    return paradas