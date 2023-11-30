# this is where well import the API data into the program. define the functions here so the main file doesnt get messy
import json
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
        self.url = ""
        self.Api_Key = ""
    
    def Api_Data(self):
        pass

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
    def updateData(self,data):
        with open("output.txt","a") as file:
            pass

t = ClientData()
print(t.LoadData())


from datetime import datetime
from typing import Any
def timestamp():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%B %d, %Y %H:%M:%S")
    return formatted_datetime

print(timestamp())
