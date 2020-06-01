
# # --- Find GEDI files of interest

# Use LP DAAC GEDI Finder to find GEDI orbits of interest

# https://lpdaacsvc.cr.usgs.gov/services/gedifinder

# # --- Prep data with LP DAAC Data Prep Scripts

# https://git.earthdata.nasa.gov/projects/LPDUR/repos/gedi-subsetter/browse

# Available GEDI products and versions
gedi_products_list = ['GEDI01_B', 'GEDI02_A', 'GEDI02_B']
gedi_versions_list = ['001']

# Import packages
import urllib.request, json, sys
from utils import numbers, strings, classes, downloader

# Options for main menu
mainMenu_options = [
        'Retrieve new GEDI Data from LP_DAAC/NASA',
        'Subset GEDI Data for a given ROI',
        'Exit system'
    ]

def gedi_finder():
    """
    Create a GEDI Finder request
    """
    while True:
        # Read user inputs to process a query for GEDI HTTPS Links
        usr_product = downloader.gedi_products(gedi_products_list)
        usr_version = downloader.gedi_version(gedi_versions_list)
        usr_bbox = downloader.gedi_bbox()
        
        # Print inputs
        print(
            '\nSelected GEDI Product = {} [{}]'.format(
                usr_product, gedi_products_list[usr_product - 1]
            )
        )
        print(
            'Selected GEDI Version = {} [{}]'.format(
                usr_version, gedi_versions_list[usr_version - 1]
            )
        )
        print(f'Defined Bounding Box = {usr_bbox}')

        while True:
            conf = str(input('Confirm search [y/n]?').strip().lower())

            if conf in 'yn':
                break
            print(strings.colors('[ERROR] Either confirm or decline [y/n]', 1))
        
        if conf == 'y':
            break
        print('Redefining terms of the search\n')


    # Calls request - Use LP DAAC GEDI-Finder to define files to download    
    obj = classes.GEDI_request(
        p = gedi_products_list[usr_product - 1], 
        v = gedi_versions_list[usr_version - 1], 
        bbox = usr_bbox
        )
    gedi_data = obj.process_request()
    
    print(gedi_data)

    # # Save HTTPS Links as a Text file
    # with open('gedi_downloadLinks.txt', 'a+') as f:
    #     for gedi_file in gedi_data:
    #         f.write(f'{gedi_file}\n')


def subsetter():
    """
    Create a GEDI Finder request
    """
    pass


def main():
    
    # Printout a greeting message
    strings.greeting()

    for pos, options in enumerate(mainMenu_options):
        print(
            '{} - {}'.format(
                strings.colors(pos+1, 3), strings.colors(options, 2)
            )
        )
    
    while True:

        # Identifying next action
        usr_option = numbers.readOption(
            'Select an option: ', 
            len(mainMenu_options)
        ) 
        
        if usr_option == 1:
            gedi_finder()
        elif usr_option == 2:
            subsetter()
        elif usr_option == 3:
            sys.exit('\n' + strings.colors('Goodbye, see you!', 1) + '\n')
    
    
# Only run code when invoked from command-line
if __name__ == '__main__':
    main()