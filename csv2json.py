import csv 
import json
import time

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        print("db.market.insertMany([")
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
            id = row.get("_id").strip()
            name = row.get("NAME").strip()
            translate = row.get("TRANSLATE").strip()
            #print("{_id:\"", id,"\",name: \"", name,"\", translate:\"", translate, "\"},")
            print("{", f"_id: \"{id}\", name: \"{name}\", translate: \"{translate}\"", "},")
        print("])")
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
csvFilePath = r'file.csv'
jsonFilePath = r'mongoimport_data.json'

start = time.perf_counter()
csv_to_json(csvFilePath, jsonFilePath)
finish = time.perf_counter()
