import os
import urllib
import ssl
import pickle
import pandas as pd

rootdir = "./images"
root_dirname="/Users/arpita/Downloads"
csv_filename = os.path.join(root_dirname, 'wikiart.csv.gz')
df = pd.read_csv(csv_filename, index_col=0, compression='gzip')
for row in df.iterrows():
    name = row[0]
    url = row[1]['image_url']
    print url
    path = os.path.join(rootdir,name+".jpg")
    urllib.urlretrieve(url, path)
    print "fetched",name