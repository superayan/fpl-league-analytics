#!/usr/bin/env python3
import json
import os
from datetime import datetime

## Reads the file path and converts the read data to json
def readFileAndConvertToJSON(filePath):
    print("reading " + filePath)
    file = open(filePath, mode='r', encoding='utf-8')
    fileRead = file.read()
    file.close()
    return json.loads(fileRead)

# creates the output directory, and returns the path to it
def createOutPutDirectory():
    if not os.path.exists('output'):
        os.makedirs('output')
    now = datetime.now()
    outputPath = "output/" + str(now)
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)
    return outputPath

def writeJsonData(path, data, fileName):
    with open(path + fileName, 'w') as outfile:
        json.dump(data, outfile, indent="\t")
        outfile.close()

def writeTextData(path, data):
    with open(path + '/analytics.txt', 'w') as outfile:
        outfile.write(data)
        outfile.close()
