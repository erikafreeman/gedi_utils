
# Import packages
import urllib.request, json

class GEDI_request(object):

    lpdaac_base_url = 'https://lpdaacsvc.cr.usgs.gov/services/gedifinder?'

    def __init__(self, p='GEDI01_B', v='001', bbox='[]'):
        self.product = p
        self.version = v
        self.bbox = str(bbox).replace(' ','')
        self.output = 'json'

    def process_request(self):

        # Crete URL to access LP DAAC GEDI-Finder
        url = self.lpdaac_base_url + 'product=' + self.product
        url += '&version=' + self.version
        url += '&bbox=' + self.bbox
        url += '&output=' + self.output
        
        # Read data as a JSON file
        with urllib.request.urlopen(url) as webPage:
            data = json.loads(webPage.read().decode())
        
        # Return list of HTTPS links for download steps 
        return data['data']