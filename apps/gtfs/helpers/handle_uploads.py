import datetime
from pathlib import Path

TEMP_DATA_PATH = '{}/data/'.format(Path(__file__).parent.absolute())

def handle_uploaded_file(f, user):
    '''
    Faz a transferência do arquivo para uma área temporársia
    Retorna o caminho absoluto do arquivo gerado
    '''

    new_file = '{}{}_{}'.format(TEMP_DATA_PATH, user, f.name)

    with open(new_file , 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
    return new_file
