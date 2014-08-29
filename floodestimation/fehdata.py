from urllib.request import urlopen
from appdirs import AppDirs
import os
import shutil
from zipfile import ZipFile

DOWNLOAD_URL = 'http://www.ceh.ac.uk/data/nrfa/peak_flow/WINFAP-FEH_v3.3.4.zip'
CACHE_FOLDER = AppDirs(__name__, appauthor='OpenHydrology').user_cache_dir
os.makedirs(CACHE_FOLDER, exist_ok=True)
CACHE_ZIP = 'FEH_data.zip'


def download_data():
    """
    Downloads complete station dataset including catchment descriptors and amax records. And saves it into a cache
    folder.
    """
    with urlopen(DOWNLOAD_URL) as f:
        with open(os.path.join(CACHE_FOLDER, CACHE_ZIP), "wb") as local_file:
            local_file.write(f.read())


def unzip_data():
    with ZipFile(os.path.join(CACHE_FOLDER, CACHE_ZIP), 'r') as zf:
        zf.extractall(path=CACHE_FOLDER)


def clear_cache():
    shutil.rmtree(CACHE_FOLDER)
    os.makedirs(CACHE_FOLDER)


def amax_files():
    return [os.path.join(dp, f) for dp, dn, filenames in os.walk(CACHE_FOLDER)
            for f in filenames if os.path.splitext(f)[1].lower() == '.am']

def cd3_files():
    return [os.path.join(dp, f) for dp, dn, filenames in os.walk(CACHE_FOLDER)
            for f in filenames if os.path.splitext(f)[1].lower() == '.am']

def update_database():
    """

    :return:
    """