import gzip 
import shutil

with gzip.open('dataset2.json.gz', 'rb') as f_in:
    with open('dataset2.json', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)