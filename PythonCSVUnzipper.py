# -----------------------------------------------------------
# Absolute work-in-progress! Not working at the moment...
# (C) 2022 Kyle McKenzie, Colorado
# Released under GNU Public License (GPL)
# -----------------------------------------------------------

from zipfile import ZipFile
import tkinter as tk
from tkinter import filedialog
import shutil
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
unzip_path = os.path.dirname(file_path) + "/" + os.path.basename(file_path).rsplit('.',1)[0]
csv_path = os.path.dirname(file_path) + "/" + "CSV"

def unzip(f,l):
    with ZipFile(f, 'r') as zipObj:
        for i in zipObj.namelist():
            filename = os.path.basename(i)
            if i.endswith('.zip'):
                zipObj.extract(i,l)
            if i.endswith('.csv'):
                source = zipObj.open(i)
                target = open(os.path.join(csv_path, i + "_" + filename).replace("\\","/"), "wb")
                with source, target:
                    shutil.copyfileobj(source, target)
    for x in os.listdir(unzip_path):
        with ZipFile(os.path.join(unzip_path, x).replace("\\","/"), 'r') as newZipObj:
            for y in newZipObj.namelist():
                filename1 = os.path.basename(y)
                if not filename:
                    continue
            if y.endswith('.csv'):
                if os.path.isdir(csv_path) == False:
                    os.mkdir(csv_path)
                source = newZipObj.open(y)
                target = open(os.path.join(csv_path, x + "_" + filename1).replace("\\","/"), "wb")
                with source, target:
                    shutil.copyfileobj(source, target)

unzip(file_path, unzip_path)
shutil.rmtree(unzip_path)