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
import io

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
file_path_name = file_path.rsplit('/',1)[1]
file_name = file_path_name.rsplit('.',1)[0]
file_path_directory = file_path.rsplit('/',1)[0]
CSV_directory = file_path_directory + "/" + "CSVs"


def unzip(f):
    with ZipFile(f, 'r') as zipObj:
        if os.path.isdir(CSV_directory) == False:
            os.mkdir(CSV_directory)
        listOfFileNames = zipObj.namelist()
        for member in listOfFileNames:
            filename = os.path.basename(member)
            if not filename:
                continue
            if member.endswith('.csv'):
                source = zipObj.open(member)
                target = open(os.path.join(CSV_directory, file_name + "_" + filename), "wb")
                with source, target:
                    shutil.copyfileobj(source, target)
            if member.endswith('.zip'):
                content = io.BytesIO(zipObj.read(member))
                with ZipFile(content, 'r') as zipObj1:
                    for i in zipObj1.namelist():
                        filename1 = os.path.basename(member)
                        if not filename1:
                            continue
                        if i.endswith('.csv'):
                            source = zipObj1.open(i)
                            target = open(os.path.join(CSV_directory, file_name + "_" + filename1), "wb")
                            with source, target:
                                shutil.copyfileobj(source, target)

unzip(file_path)
