#! python
import os
import shutil
from zipfile import ZipFile

import numpy as np
import requests
from tqdm import tqdm

DATA_DIR = "data/"

SET_URL = "http://epileptologie-bonn.de/cms/upload/workgroup/lehnertz/"
SET_CODES = ('Z', 'O', 'N', 'F', 'S')


def download_archive(code: str, path: str):
    response = requests.get(os.path.join(SET_URL, code + '.zip'))
    with open(path, "wb") as f:
        f.write(response.content)


def extract_archive(archive_path: str, dest_path: str):
    shutil.rmtree(dest_path, ignore_errors=True)
    os.makedirs(dest_path)
    with ZipFile(archive_path) as zf:
        zf.extractall(dest_path)


def load_set(code: str):
    archive_path = os.path.join(DATA_DIR, code + '.zip')
    download_archive(code, path=archive_path)

    set_dir = os.path.join(DATA_DIR, code)
    extract_archive(archive_path, dest_path=set_dir)

    segments = np.stack([
        np.loadtxt(os.path.join(set_dir, file))
        for file in sorted(os.listdir(set_dir))
    ])

    with open(os.path.join(DATA_DIR, f"{code}.npy"), "wb") as f:
        np.save(f, segments)

    os.remove(archive_path)
    shutil.rmtree(set_dir)


if __name__ == '__main__':
    for code in tqdm(SET_CODES, desc="loading subsets"):
        load_set(code)
