# this is where well import the API data into the program. define the functions here so the main file doesnt get messy
import json
from datetime import datetime
from typing import Any
import requests
class User:
    def __init__(self,id) -> None:
        self.id = id

    def construct(self):
        creditScore = input("input credit Score")
        AssetsValue = input("value of your Assets")
        Liabilitys = input("value of liabilitys")
        if self.riskRatio(creditScore,AssetsValue,Liabilitys) > 10:
            pass

    

    def riskRatio(self,creditScore,assets,liabilitys):
        pass

class ClientData: # where data manipulation of user data will be done and returned
    def __init__(self) -> None:
        with open("class.json","r") as file:
            data = json.load(file)
            self.data = data
        self.url = "https://api.stlouisfed.org/fred/releases?api_key=e4e059612f107cf41d7ba42c9c357b71&file_type=json"
    
    def Api_Data(self,amount):
        if self.needsUpdate() is True:
            self.updateData()
        return [self.grabxdata(amount)] if self.grabxdata != None else "Error encounted"
    
    def grabloanrate(self):
        data = 4
        file = json.loads("apidata.json")
        pass
        return data
    def grabxdata(self,amount):
        try:
            with open("Apidata.json", 'r') as file:
                # Read the first `amount` lines from the file
                lines = [next(file) for _ in range(amount)]
                data = [json.loads(line) for line in lines]
                return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

    def LoadData(self,count):
        with open("class.json","r") as file:
            data = json.load(file)
            size = len(data)
            Userdata = []
            if count > size:
                raise Exception(IndexError)
            for i in range(count):
                Userdata.append(data[i])
            file.close()
            return Userdata
        
    def updateData(self): # this is called when we have to absolutly update 
        pulldata(self.url)
        with open("output.txt","r+") as file:
            file.write(timestamp())
        return
    def needsUpdate(self) -> bool: # check if the data needs to be updated
        with open("output.txt","r+") as file:
            first_line = file.readline().strip()
            if timestamp() != first_line:
                return True
            else:
                return False
            

def pulldata(url,*key):
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()
        # Specify the filename to save the JSON data
        filename = "apidata.json"
        # Write the JSON data to a file
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
        print(f"Data successfully written to {filename}")
    else:
        print(response.status_code)

t = ClientData()
#print(t.updateData(5))
#pulldata("https://api.stlouisfed.org/fred/releases?api_key=e4e059612f107cf41d7ba42c9c357b71&file_type=json")
#"https://api.stlouisfed.org/fred/releases?api_key=e4e059612f107cf41d7ba42c9c357b71&file_type=json"


def timestamp():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%B %d, %Y" ) #%H:%M:%S
    return formatted_datetime

