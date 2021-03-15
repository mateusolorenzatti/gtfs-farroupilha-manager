from bs4 import BeautifulSoup

def extract_stops(bs_data):
    '''
    Recebe o objeto BeautifulSoup e processa as paradas presentes no KML 
    '''

    # Extraindo as Paradas
    stops_kml = bs_data.find_all('Placemark')
    del stops_kml[-1] # Remover a última, que se refere aos Shapes
    print('Quantidade de Paradas Encontradas:', len(stops_kml))

    # print(stops_kml[0].prettify())

    stops = []
    for stop in stops_kml:
        '''
        print(stop.prettify()
        # Dados da parada (X, Y e Z)
        print(stop('Point')[0]('coordinates')[0].contents)
        # float(stop('Point')[0]('coordinates')[0].contents[0].split(',')[1]) -> Latitude
        # float(stop('Point')[0]('coordinates')[0].contents[0].split(',')[0]) -> Longitude
        '''

        stops.append(
            {
                'lat': float(stop('Point')[0]('coordinates')[0].contents[0].split(',')[1]), 
                'lon': float(stop('Point')[0]('coordinates')[0].contents[0].split(',')[0]), 
                'timestamp': stop('TimeStamp')[0]('when')[0].contents[0]
            }
        )
    
    return stops

def extract_shapes(bs_data):
    '''
    Recebe o objeto BeautifulSoup e processa as shapes presentes no KML 
    '''

    shapes_kml = bs_data.find_all('Placemark', {'id': 'tour'})
    shapes_kml = shapes_kml[0]('gx:MultiTrack')[0]('gx:Track')[0].find_all('gx:coord')
    print('Quantidade de Pontos de Shape encontrados:', len(shapes_kml))

    shapes = []
    seq = 1

    for shape in shapes_kml:
        '''
        # float(shape.contents[0].split()[1]) -> Latitude
        # float(shape.contents[0].split()[0]) -> Longitude
        ''' 

        shapes.append(
            {
                'lat': float(shape.contents[0].split()[1]), 
                'lon': float(shape.contents[0].split()[0]),
                'sequence': seq
            }
        )

        seq += 1

    return shapes

def KML(arquivo_entrada):
    '''
    Processa o arquivo KML para retornar dados em formato Python.
     - Requer como parâmetro o nome do arquivo KML no servidor
     - Retorna uma tupla com (1) as paradas do arquivo e (2) a shape do arquivo.
    '''

    with open(arquivo_entrada, 'r') as f: 
        data = f.read() 
    
    bs_data = BeautifulSoup(data, "xml")
    stops = extract_stops(bs_data)
    shapes = extract_shapes(bs_data)

    return stops, shapes