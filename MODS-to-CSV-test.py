# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 s2018

@author: chos
"""

import os
from xml.etree import ElementTree
import csv

## Ask for the file, set up dictionary for output
path = input("what directory do you want to test?: ").replace("'","")
titles = {}

## Loop through the subdirectories, find the XMLs, then use ET
## to establish a python XML object, then look for the titles,
## then pull out the title text
for dirpath, dirnames, filenames in os.walk(path):
    for filename in [f for f in filenames if f.endswith(".xml")]:
        path = os.path.join(dirpath, filename)
        values = []
        tree = ElementTree.parse(path)
        root = tree.getroot()

        for title in root.findall('{http://www.loc.gov/mods/v3}titleInfo'):
            for value in title.findall('{http://www.loc.gov/mods/v3}title'):
                 values.append(value.text)
        titles[filename] = values
        print(filename, values)

## Write the titles into a csv that includes both filename and the title
with open ('output.txt', 'w') as output:
    fieldnames = ['Filename', "Titles"]
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    for filename, titlez in titles.items():
        writer.writerow({
            'Filename': filename,
            'Titles': titlez,
           })

print(titles)
