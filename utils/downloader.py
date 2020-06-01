

from utils import numbers, strings, classes

def gedi_products(products, colorId=3, colorStr=2):
    print('\n' + '--- Select Desired GEDI Product:')
    for pos, prod in enumerate(products):
        print(
            '{} - {}'.format(
                strings.colors(pos+1, colorId), strings.colors(prod, colorStr)
            )
        )
    
    # Read GEDI Product
    return numbers.readOption('GEDI Product: ', len(products))


def gedi_version(versions, colorId=3, colorStr=2):
    print('\n' + '--- Select Desired GEDI Version:')
    for pos, vers in enumerate(versions):
        print(
            '{} - {}'.format(
                strings.colors(pos+1, colorId), strings.colors(vers, colorStr)
            )
        )
    
    # Read GEDI Version
    return numbers.readOption('GEDI Version: ', len(versions))


def check_bbox(bbox):
    """
    Function to check if the bounding box is a valid one
    """
    # if Upper_left_lat > Lower_right_lat
    # and Upper_left_long < Lower_right_long
    if bbox[0] > bbox[2] and bbox[1] < bbox[3]:
        return True
    else:
        return False 


def gedi_bbox():
    
    while True:
        print('\n' + '--- Enter Bounding Box Coordinates [WGS84 lat/long]:')
        coords = [
            'Upper-Left Latitude: ',
            'Upper-Left Longitude: ',
            'Lower-Right Latitude: ',
            'Lower-Right Longitude: '
            ]
        bbox = [
            numbers.readFloat(strings.colors(coords[i], 2)) for i in range(4)
        ]

        if check_bbox(bbox):
            return bbox
        print(strings.colors('[ERROR] Enter a valid Bounding Box!', 1))

        # Return results
