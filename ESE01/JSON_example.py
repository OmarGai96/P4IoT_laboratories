import json 

data = {
    "country": "Germany",
    "vehicle": {
        "name": "Volkswagen",
        "model": "T-Roc"
    }
}

file1 = open("fileJSON.json", "w")
json.dump(data, file1,indent=4)  #write the dictionary data on file 1
file1.close()

file2=open("fileJSON.json")
myDict=json.load(file2)
print("Dictionary content:")
print(myDict)
file2.close()

stringaDict = json.dumps(myDict) #this will return a string by converting the dictionary
print("String content:")
print(stringaDict)

myNewDict = json.loads(stringaDict) #this will return a dictionary obtained by converting the string

print("New dictionary content:")
print(myNewDict)
