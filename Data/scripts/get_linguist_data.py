import os
import urllib.request
import time

base_url = 'http://listserv.linguistlist.org/pipermail/linglite/'
years = [str(year) for year in range(1997,2016)]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

for year in years:
    path = os.path.join('..', 'linguistlist', year)
    # Make the necessary folder.
    os.makedirs(path)
    
    for month in months:
        # Update variables.
        filename = '{}-{}.txt.gz'.format(year, month)
        path_with_file = os.path.join(path, filename)
        url = base_url + filename
        
        # Write the data to disk.
        with urllib.request.urlopen(url) as response:
            with open(path_with_file, 'wb') as outfile:
                data = response.read()
                outfile.write(data)
        
        # Be nice to the server.
        time.sleep(2)
