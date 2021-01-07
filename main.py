__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
from zipfile import ZipFile


def clean_cache():
    if not os.path.exists('./files/cache'):
        os.makedirs('./files/cache')
    else:
        for f in os.listdir('./files/cache'):
            os.remove(os.path.join('./files/cache', f))


def cache_zip(file_path, cache_dir_path):
    file = file_path
    path = os.path.abspath(cache_dir_path)
    with ZipFile(file, 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        # Apart dat ik die variabelen file en path moest introduceren omdat het anders
        # niet lekker loopt.
        zipObj.extractall(path)


def cached_files():
    return os.listdir("./files/cache")


def find_password(cached_files, path):
    for file in cached_files:
        path = os.path.abspath(path)
        searchfile = open(path+"/"+file, "r")
        for line in searchfile:
            if "password".upper() in line.upper():
                print("In file : "+file+" staat "+line)
        searchfile.close()

def cleanup(): 
    # doel was om paswoord te vinden en niet om de harddisk te vervuilen 
    if os.path.exists('./files/cache'):
       for f in os.listdir('./files/cache'):
           os.remove(os.path.join('./files/cache', f)) 

try:
    clean_cache()
    cache_zip('./files/data.zip', './files/cache')
    cached_files = cached_files()
    # als de list cached_files leeg is, gebeurt er ook niets in find_password. Er is
    # geen directe aanleiding voor de try. Er kan door een ander proces natuurlijk wel
    # roet in het eten worden gegooid. bv. als er nog een ander proces draait die de files in onze
    # cache directory benaderen.
    find_password(cached_files, "./files/cache")
    cleanup()
except:
    print("An error occurred")
else : print("")