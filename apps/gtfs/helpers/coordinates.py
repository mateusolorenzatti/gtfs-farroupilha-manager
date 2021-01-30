
from apps.shapes.models import Shapes

def shape_midpoint(shape_list):
    lon = [ float(shape.shape_pt_lon) for shape in shape_list ]
    lat = [ float(shape.shape_pt_lat) for shape in shape_list ]

    return [(max(lon) + min(lon)) / 2, (max(lat) + min(lat)) / 2]