import json

if __name__=="__main__":
##ESERCIZIO 8
    print("\nEsercizio 8\n")
##Set all the keys and the empty values and then fill the dictionary
    personal_data={
        "projectName": "",
        "company": "",
        "deviceList": [
            {
                "deviceID": "",
                "deviceName": "",
                "deviceType": ""   
           }
        ]
    }

    personal_data['projectName']=input("Write the name of your project: ")
    personal_data['company']=input("Write the name of your company: ")
    personal_data['deviceList'][0]['deviceID']=input("\tWrite the ID of your device: ")
    personal_data['deviceList'][0]['deviceName']=input("\tWrite the name of your device: ")
    personal_data['deviceList'][0]['deviceType']=input("\tWrite the type of your device: ")

    json.dump(personal_data,open("dictionaryOutput.json","w"),indent=4)

##additional feature
#    f=open("dict_content.txt", 'w')
#    f.write(f"Project name: {personal_data['projectName']}\n")
#    f.write(f"Company:      {personal_data['company']}\n")
#    f.write(f"\tDevice ID:    {personal_data['deviceList'][0]['deviceID']}\n")
#    f.write(f"\tDevice Name:  {personal_data['deviceList'][0]['deviceName']}\n")
#    f.write(f"\tDevice type:  {personal_data['deviceList'][0]['deviceType']}")
#
#    f.close()